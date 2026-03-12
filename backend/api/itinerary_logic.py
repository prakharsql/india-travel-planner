"""
Smart itinerary distribution logic.
Distributes N places across D days, assigns morning/afternoon/evening slots.
"""


def distribute_places(places, num_days):
    """
    Distribute a list of places across the given number of days.
    Returns a list of dicts: [{"day": 1, "morning": [...], "afternoon": [...], "evening": [...]}, ...]
    """
    if not places:
        return []

    num_days = max(1, min(num_days, 7))
    total = len(places)

    # Calculate base and remainder for even distribution
    base_count = total // num_days
    remainder = total % num_days

    itinerary = []
    idx = 0

    for day in range(1, num_days + 1):
        # Distribute remainder across first days
        day_count = base_count + (1 if day <= remainder else 0)
        day_places = places[idx:idx + day_count]
        idx += day_count

        # Assign to morning / afternoon / evening slots
        morning = []
        afternoon = []
        evening = []

        for i, place in enumerate(day_places):
            slot = i % 3
            if slot == 0:
                morning.append(place)
            elif slot == 1:
                afternoon.append(place)
            else:
                evening.append(place)

        itinerary.append({
            "day": day,
            "morning": morning,
            "afternoon": afternoon,
            "evening": evening,
        })

    return itinerary


def build_fallback_itinerary(city_data, num_days, budget, interests):
    """
    Build a rule-based itinerary when AI is not available.
    city_data: dict with 'name', 'places' (list of place dicts), 'foods' (list of food dicts)
    """
    places = city_data.get('places', [])
    foods = city_data.get('foods', [])

    # Filter places by interest if provided
    if interests:
        interest_set = set(i.lower() for i in interests)
        filtered = [p for p in places if p.get('category', '').lower() in interest_set]
        if filtered:
            places = filtered

    distribution = distribute_places(places, num_days)

    # Budget multipliers (in INR)
    budget_map = {
        'low': {'hotel': 800, 'food': 300, 'transport': 200, 'misc': 100},
        'medium': {'hotel': 2500, 'food': 800, 'transport': 500, 'misc': 300},
        'luxury': {'hotel': 8000, 'food': 2000, 'transport': 1500, 'misc': 1000},
    }
    budget_key = (budget or 'medium').lower()
    daily_budget = budget_map.get(budget_key, budget_map['medium'])
    daily_total = sum(daily_budget.values())

    days_output = []
    for day_data in distribution:
        day_num = day_data['day']
        activities = []

        for slot_name, slot_places in [('Morning', day_data['morning']),
                                        ('Afternoon', day_data['afternoon']),
                                        ('Evening', day_data['evening'])]:
            for place in slot_places:
                name = place.get('name', place) if isinstance(place, dict) else place
                desc = place.get('description', '') if isinstance(place, dict) else ''
                activities.append({
                    'time': slot_name,
                    'activity': f"Visit {name}",
                    'description': desc,
                    'type': place.get('category', 'sightseeing') if isinstance(place, dict) else 'sightseeing',
                })

        # Add food recommendation for the evening
        if foods and day_num <= len(foods):
            food = foods[day_num - 1]
            food_name = food.get('name', food) if isinstance(food, dict) else food
            activities.append({
                'time': 'Night',
                'activity': f"Try {food_name}",
                'description': food.get('description', '') if isinstance(food, dict) else '',
                'type': 'food',
            })

        days_output.append({
            'day': day_num,
            'activities': activities,
        })

    return {
        'city': city_data.get('name', ''),
        'num_days': num_days,
        'budget_type': budget_key,
        'estimated_daily_budget': daily_total,
        'estimated_total_budget': daily_total * num_days,
        'currency': 'INR',
        'days': days_output,
    }
