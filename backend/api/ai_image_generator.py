"""
AI Image Generator for India Travel Planner.
Generates unique city images using OpenAI DALL-E API.
Pre-generated AI images are served from the generated_images directory.
"""
import os
import hashlib
import requests
import time
from pathlib import Path


# Directory for generated images
IMAGES_DIR = Path(__file__).resolve().parent.parent / 'generated_images'
IMAGES_DIR.mkdir(exist_ok=True)


def _get_city_slug(city_name):
    """Create a filesystem-safe slug from city name."""
    return city_name.strip().lower().replace(' ', '_').replace("'", "")


def _get_cached_image_path(city_name):
    """Check if a cached image exists for this city."""
    slug = _get_city_slug(city_name)
    for ext in ['.png', '.jpg', '.webp']:
        path = IMAGES_DIR / f"{slug}{ext}"
        if path.exists() and path.stat().st_size > 1000:
            return path
    return None


def _build_prompt(city_name):
    """Build a cinematic AI image prompt for the city."""
    city_prompts = {
        'delhi': "Cinematic ultra-realistic travel photograph of Delhi, India. Show the iconic Red Fort with its magnificent red sandstone walls, India Gate, bustling Chandni Chowk, Mughal architecture, golden hour sunset lighting, professional travel photography, 4k",
        'jaipur': "Cinematic photograph of Jaipur Pink City, Rajasthan, India. Show the magnificent Hawa Mahal palace with its pink honeycomb facade, colorful bazaars, traditional Rajasthani architecture, warm sunset lighting, ultra realistic 4k travel photography",
        'goa': "Cinematic travel photograph of Goa, India. Show pristine golden beach with coconut palms, colorful fishing boats on turquoise waters, Portuguese colonial architecture, tropical sunset with orange and pink sky, ultra realistic 4k photography",
        'varanasi': "Cinematic travel photograph of Varanasi ghats at golden sunrise with wooden boats on the sacred Ganges river, ancient stone steps, morning prayer rituals, Hindu temples, mist rising from the river, spiritual atmosphere, ultra realistic 4k",
        'udaipur': "Cinematic photograph of Udaipur, City of Lakes, Rajasthan, India. Show the majestic Lake Palace floating on Lake Pichola, City Palace, Aravalli hills, beautiful reflections in calm water, romantic sunset golden lighting, ultra realistic 4k",
        'mumbai': "Cinematic photograph of Mumbai, India. Show the iconic Gateway of India monument, Art Deco buildings along Marine Drive, Arabian Sea, bustling street life, dramatic golden hour lighting, ultra realistic 4k travel photography",
        'agra': "Cinematic travel photograph of the Taj Mahal in Agra, India. White marble monument reflected in the long reflecting pool, Mughal gardens, sunrise painting the dome in pink and gold, ultra realistic 4k photography",
        'shimla': "Cinematic photograph of Shimla, Himachal Pradesh, India. Colonial British-era architecture along Mall Road, Christ Church, snow-capped Himalayan mountains, pine forests, cool misty atmosphere, ultra realistic 4k travel photography",
        'manali': "Cinematic photograph of Manali, Himachal Pradesh, India. Snow-covered Himalayan peaks, Beas River valley, traditional wooden houses, pine and deodar forests, clear blue sky, ultra realistic 4k travel photography",
        'kolkata': "Cinematic photograph of Kolkata, India. Iconic Howrah Bridge over the Hooghly River, Victoria Memorial, yellow taxis, flower markets, colonial architecture, warm golden light, ultra realistic 4k photography",
        'hyderabad': "Cinematic photograph of Hyderabad, India. Magnificent Charminar monument with four minarets, bustling Old City bazaars, Golconda Fort, warm evening lighting, ultra realistic 4k travel photography",
        'kochi': "Cinematic photograph of Kochi, Kerala, India. Chinese fishing nets at Fort Kochi waterfront, colonial architecture, colorful spice markets, backwater houseboats, coconut palms, tropical sunset, ultra realistic 4k photography",
        'rishikesh': "Cinematic photograph of Rishikesh, Uttarakhand, India. Lakshman Jhula suspension bridge over turquoise Ganges, yoga ashrams, Himalayan foothills, temple bells, spiritual atmosphere, golden evening light, ultra realistic 4k",
        'amritsar': "Cinematic photograph of the Golden Temple in Amritsar, Punjab, India. Gold-plated gurdwara reflected in sacred pool, devotees, marble walkway, night illumination, spiritual atmosphere, ultra realistic 4k photography",
        'darjeeling': "Cinematic photograph of Darjeeling, West Bengal, India. Green tea plantations on misty hillsides, Darjeeling Himalayan Railway toy train, Kanchenjunga peak, colonial hill station, morning mist, ultra realistic 4k photography",
        'leh': "Cinematic photograph of Leh, Ladakh, India. Ancient Leh Palace on hilltop, dramatic mountain landscape, Buddhist monasteries, prayer flags, crystal clear blue sky, Pangong Lake, ultra realistic 4k travel photography",
        'jodhpur': "Cinematic photograph of Jodhpur, the Blue City, Rajasthan, India. Massive Mehrangarh Fort overlooking blue-painted old city houses, carved windows, colorful textiles, warm desert sunset, ultra realistic 4k photography",
        'jaisalmer': "Cinematic photograph of Jaisalmer, the Golden City, Rajasthan, India. Golden sandstone Jaisalmer Fort rising from the Thar Desert, ornate havelis, camel caravans on sand dunes at sunset, warm golden light, ultra realistic 4k",
        'mysore': "Cinematic photograph of Mysore Palace illuminated with thousands of lights at night, Indo-Saracenic architecture, Chamundi Hills, flower markets, royal grandeur, ultra realistic 4k travel photography",
    }

    city_lower = city_name.lower().strip()
    if city_lower in city_prompts:
        return city_prompts[city_lower]

    return f"Cinematic ultra-realistic travel photograph of {city_name}, India. Show iconic architecture, vibrant streets, traditional culture, local markets, landmarks, golden hour lighting, travel photography, 4k, highly detailed"


def generate_city_image(city_name, force_regenerate=False):
    """
    Get or generate an AI image for the given city.
    Returns the URL path to the image.
    
    Priority:
    1. Serve existing cached AI image (pre-generated or previously generated)
    2. Generate via OpenAI DALL-E API if key available
    3. Return None (frontend handles missing images)
    """
    slug = _get_city_slug(city_name)

    # Check cache first (pre-generated AI images take priority)
    if not force_regenerate:
        cached = _get_cached_image_path(city_name)
        if cached:
            return f"/generated_images/{cached.name}"

    # Try OpenAI DALL-E API
    api_key = os.environ.get('OPENAI_API_KEY', '')
    if api_key:
        result = _generate_with_openai(city_name, api_key, slug)
        if result:
            return result

    # No cached image and no API key — return None
    # Frontend will show a styled placeholder
    return None


def _generate_with_openai(city_name, api_key, slug):
    """Generate image using OpenAI DALL-E API."""
    prompt = _build_prompt(city_name)

    for attempt in range(2):  # Retry once on failure
        try:
            headers = {
                'Authorization': f'Bearer {api_key}',
                'Content-Type': 'application/json',
            }
            data = {
                'model': 'dall-e-3',
                'prompt': prompt,
                'n': 1,
                'size': '1792x1024',
                'quality': 'hd',
                'style': 'vivid',
            }

            resp = requests.post(
                'https://api.openai.com/v1/images/generations',
                headers=headers,
                json=data,
                timeout=60,
            )

            if resp.status_code == 200:
                image_url = resp.json()['data'][0]['url']

                # Download and cache the image
                img_resp = requests.get(image_url, timeout=30)
                if img_resp.status_code == 200:
                    filepath = IMAGES_DIR / f"{slug}.png"
                    with open(filepath, 'wb') as f:
                        f.write(img_resp.content)
                    return f"/generated_images/{slug}.png"

        except Exception:
            if attempt == 0:
                time.sleep(1)

    return None
