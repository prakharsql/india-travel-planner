"""
API views for the India Travel Planner.
Includes universal city search, dynamic city data, AI itinerary, PDF, weather, chatbot, and AI image generation.
"""
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse

from .models import City, Place, Food
from .serializers import CityListSerializer, CityDetailSerializer
from .ai_planner import generate_ai_itinerary, generate_dynamic_city_data, chat_with_ai
from .itinerary_logic import build_fallback_itinerary
from .pdf_generator import generate_itinerary_pdf
from .cities_data import search_cities, find_city
from .ai_image_generator import generate_city_image

import os
import requests


# ── City Endpoints ──

@api_view(['GET'])
def city_list(request):
    """List cities. Combines DB cities + matching cities from dataset."""
    search = request.query_params.get('search', '').strip()

    if search:
        # Search DB first
        db_cities = City.objects.filter(name__icontains=search)
        db_results = CityListSerializer(db_cities, many=True).data

        # Replace image with AI-generated for DB cities
        for c in db_results:
            city_name = c.get('name', '')
            c['image'] = generate_city_image(city_name)

        # Also search the dataset for cities not in DB
        dataset_results = search_cities(search)
        db_names = {c['name'].lower() for c in db_results}

        for city in dataset_results:
            if city['name'].lower() not in db_names:
                db_results.append({
                    'id': f"dynamic_{city['name'].lower().replace(' ', '_')}",
                    'name': city['name'],
                    'state': city['state'],
                    'description': f"Explore {city['name']} in {city['state']} — a beautiful destination in India.",
                    'best_time_to_visit': 'October to March',
                    'image': generate_city_image(city['name']),
                    'latitude': city['lat'],
                    'longitude': city['lng'],
                    'is_dynamic': True,
                })

        return Response(db_results)
    else:
        cities = City.objects.all()
        data = CityListSerializer(cities, many=True).data
        # Replace images with AI-generated
        for c in data:
            c['image'] = generate_city_image(c.get('name', ''))
        return Response(data)


@api_view(['GET'])
def city_detail(request, pk):
    """Get city details. Supports both DB IDs and dynamic city names."""
    # Check if it's a dynamic city
    if isinstance(pk, str) and pk.startswith('dynamic_'):
        city_name = pk.replace('dynamic_', '').replace('_', ' ').title()
        city_info = find_city(city_name)

        if not city_info:
            return Response({'error': 'City not found'}, status=status.HTTP_404_NOT_FOUND)

        # Generate dynamic data using AI
        ai_data = generate_dynamic_city_data(city_info['name'], city_info['state'])

        return Response({
            'id': pk,
            'name': city_info['name'],
            'state': city_info['state'],
            'description': ai_data.get('description', ''),
            'best_time_to_visit': ai_data.get('best_time_to_visit', ''),
            'image': generate_city_image(city_info['name']),
            'latitude': city_info['lat'],
            'longitude': city_info['lng'],
            'travel_tips': ai_data.get('travel_tips', ''),
            'places': [
                {
                    'id': f'dp_{i}',
                    'name': p['name'],
                    'description': p['description'],
                    'category': p.get('category', 'cultural'),
                    'timing': p.get('timing', 'Open all day'),
                    'entry_fee': p.get('entry_fee', 'Free'),
                    'image': generate_city_image(p['name']),
                    'latitude': None,
                    'longitude': None,
                }
                for i, p in enumerate(ai_data.get('places', []))
            ],
            'foods': [
                {
                    'id': f'df_{i}',
                    'name': f['name'],
                    'description': f['description'],
                }
                for i, f in enumerate(ai_data.get('foods', []))
            ],
            'is_dynamic': True,
        })

    # DB city
    try:
        city = City.objects.get(pk=pk)
    except City.DoesNotExist:
        return Response({'error': 'City not found'}, status=status.HTTP_404_NOT_FOUND)

    data = CityDetailSerializer(city).data
    # Replace images with AI-generated
    data['image'] = generate_city_image(city.name)
    if 'places' in data:
        for p in data['places']:
            p['image'] = generate_city_image(p.get('name', ''))
    return Response(data)


@api_view(['GET'])
def city_places(request, pk):
    """Get places for a city."""
    if isinstance(pk, str) and pk.startswith('dynamic_'):
        city_name = pk.replace('dynamic_', '').replace('_', ' ').title()
        city_info = find_city(city_name)
        if not city_info:
            return Response([])
        ai_data = generate_dynamic_city_data(city_info['name'], city_info['state'])
        places = [
            {
                'id': f'dp_{i}',
                'name': p['name'],
                'description': p['description'],
                'category': p.get('category', 'cultural'),
                'timing': p.get('timing', 'Open all day'),
                'entry_fee': p.get('entry_fee', 'Free'),
                'image': generate_city_image(p['name']),
            }
            for i, p in enumerate(ai_data.get('places', []))
        ]
        return Response(places)

    places = Place.objects.filter(city_id=pk)
    from .serializers import PlaceSerializer
    data = PlaceSerializer(places, many=True).data
    for p in data:
        p['image'] = generate_city_image(p.get('name', ''))
    return Response(data)


@api_view(['GET'])
def city_foods(request, pk):
    """Get foods for a city."""
    if isinstance(pk, str) and pk.startswith('dynamic_'):
        city_name = pk.replace('dynamic_', '').replace('_', ' ').title()
        city_info = find_city(city_name)
        if not city_info:
            return Response([])
        ai_data = generate_dynamic_city_data(city_info['name'], city_info['state'])
        foods = [
            {'id': f'df_{i}', 'name': f['name'], 'description': f['description']}
            for i, f in enumerate(ai_data.get('foods', []))
        ]
        return Response(foods)

    foods = Food.objects.filter(city_id=pk)
    from .serializers import FoodSerializer
    return Response(FoodSerializer(foods, many=True).data)


# ── AI Image Generation ──

@api_view(['GET'])
def generate_image_view(request):
    """Generate an AI image for a city on demand."""
    city_name = request.query_params.get('city', '').strip()
    force = request.query_params.get('force', '').lower() == 'true'

    if not city_name:
        return Response({'error': 'city parameter required'}, status=status.HTTP_400_BAD_REQUEST)

    image_path = generate_city_image(city_name, force_regenerate=force)
    return Response({
        'city': city_name,
        'image_url': image_path,
    })


# ── AI Itinerary ──

@api_view(['POST'])
def generate_itinerary_view(request):
    """Generate a travel itinerary — supports both DB and dynamic cities."""
    city_id = request.data.get('city_id')
    num_days = int(request.data.get('num_days', 3))
    budget = request.data.get('budget', 'medium')
    interests = request.data.get('interests', [])

    if not city_id:
        return Response({'error': 'city_id is required'}, status=status.HTTP_400_BAD_REQUEST)

    # Dynamic city
    if isinstance(city_id, str) and city_id.startswith('dynamic_'):
        city_name = city_id.replace('dynamic_', '').replace('_', ' ').title()
        city_info = find_city(city_name)

        if not city_info:
            return Response({'error': 'City not found'}, status=status.HTTP_404_NOT_FOUND)

        ai_data = generate_dynamic_city_data(city_info['name'], city_info['state'])

        city_data = {
            'name': city_info['name'],
            'state': city_info['state'],
            'places': ai_data.get('places', []),
            'foods': ai_data.get('foods', []),
        }
    else:
        # DB city
        try:
            city = City.objects.get(pk=city_id)
        except City.DoesNotExist:
            return Response({'error': 'City not found'}, status=status.HTTP_404_NOT_FOUND)

        city_data = {
            'name': city.name,
            'state': city.state,
            'places': [
                {'name': p.name, 'description': p.description, 'category': p.category,
                 'timing': p.timing, 'entry_fee': p.entry_fee}
                for p in city.places.all()
            ],
            'foods': [
                {'name': f.name, 'description': f.description}
                for f in city.foods.all()
            ],
        }

    itinerary = generate_ai_itinerary(city_data, num_days, budget, interests)
    return Response(itinerary)


# ── PDF Download ──

@api_view(['POST'])
def download_pdf_view(request):
    """Generate and download itinerary PDF."""
    city_id = request.data.get('city_id')
    itinerary = request.data.get('itinerary', {})

    if not city_id or not itinerary:
        return Response({'error': 'city_id and itinerary required'}, status=status.HTTP_400_BAD_REQUEST)

    city_name = itinerary.get('city', 'Unknown')
    city_state = ''

    if isinstance(city_id, str) and city_id.startswith('dynamic_'):
        cn = city_id.replace('dynamic_', '').replace('_', ' ').title()
        city_info = find_city(cn)
        if city_info:
            city_name = city_info['name']
            city_state = city_info['state']
    else:
        try:
            city = City.objects.get(pk=city_id)
            city_name = city.name
            city_state = city.state
        except (City.DoesNotExist, ValueError):
            pass

    itinerary['city'] = city_name
    if city_state:
        itinerary['state'] = city_state

    pdf_buffer = generate_itinerary_pdf(itinerary)

    response = HttpResponse(pdf_buffer.getvalue(), content_type='application/pdf')
    filename = f"{city_name.replace(' ', '_')}_Itinerary.pdf"
    response['Content-Disposition'] = f'attachment; filename="{filename}"'
    return response


# ── Weather ──

@api_view(['GET'])
def weather_view(request):
    """Get weather for a city — uses OpenWeatherMap API with smart fallback."""
    city = request.query_params.get('city', '')
    if not city:
        return Response({'error': 'city parameter required'}, status=status.HTTP_400_BAD_REQUEST)

    api_key = os.environ.get('OPENWEATHER_API_KEY', '')

    if api_key:
        try:
            url = f"https://api.openweathermap.org/data/2.5/weather?q={city},IN&appid={api_key}&units=metric"
            resp = requests.get(url, timeout=5)
            data = resp.json()

            if resp.status_code == 200:
                return Response({
                    'city': city,
                    'temperature': round(data['main']['temp']),
                    'feels_like': round(data['main']['feels_like']),
                    'humidity': data['main']['humidity'],
                    'description': data['weather'][0]['description'].title(),
                    'wind_speed': data['wind']['speed'],
                })
        except Exception:
            pass

    # Smart mock data
    mock = {
        'delhi': {'temp': 28, 'feels': 31, 'humidity': 55, 'desc': 'Hazy Sunshine', 'best': 'October to March'},
        'jaipur': {'temp': 30, 'feels': 33, 'humidity': 40, 'desc': 'Sunny', 'best': 'October to March'},
        'goa': {'temp': 31, 'feels': 34, 'humidity': 70, 'desc': 'Partly Cloudy', 'best': 'November to February'},
        'varanasi': {'temp': 27, 'feels': 30, 'humidity': 60, 'desc': 'Clear Sky', 'best': 'October to March'},
        'udaipur': {'temp': 29, 'feels': 32, 'humidity': 45, 'desc': 'Sunny', 'best': 'September to March'},
        'mumbai': {'temp': 30, 'feels': 35, 'humidity': 75, 'desc': 'Humid & Warm', 'best': 'November to February'},
        'shimla': {'temp': 15, 'feels': 13, 'humidity': 50, 'desc': 'Cool & Pleasant', 'best': 'March to June, December'},
        'manali': {'temp': 12, 'feels': 10, 'humidity': 45, 'desc': 'Cool Mountain Air', 'best': 'April to June, December'},
        'leh': {'temp': 8, 'feels': 5, 'humidity': 30, 'desc': 'Clear & Crisp', 'best': 'June to September'},
    }

    city_lower = city.lower()
    data = mock.get(city_lower, {'temp': 27, 'feels': 29, 'humidity': 55, 'desc': 'Pleasant', 'best': 'October to March'})

    return Response({
        'city': city,
        'temperature': data['temp'],
        'feels_like': data['feels'],
        'humidity': data['humidity'],
        'description': data['desc'],
        'wind_speed': 12,
        'best_months': data.get('best', 'October to March'),
    })


# ── Chatbot ──

@api_view(['POST'])
def chat_view(request):
    """Travel chatbot endpoint."""
    message = request.data.get('message', '').strip()
    city_context = request.data.get('city_context', '')

    if not message:
        return Response({'error': 'message is required'}, status=status.HTTP_400_BAD_REQUEST)

    reply = chat_with_ai(message, city_context)

    return Response({'reply': reply})
