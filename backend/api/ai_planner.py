"""
AI-powered itinerary generation and travel chatbot using Google Gemini API.
Enhanced with comprehensive fallback logic for offline use.
"""
import json
import os
import re

from .itinerary_logic import build_fallback_itinerary


SYSTEM_CONTEXT = """You are "Namaste AI", a friendly, knowledgeable, and enthusiastic India travel assistant 
for the India Travel Planner platform. You specialize in Indian travel, culture, food, history, and tourism.

Key traits:
- You are warm and use a mix of English with occasional Hindi/Indian phrases (like "Namaste", "Bhai", "Arre")
- You give structured, concise but informative answers
- You recommend specific places, foods, and experiences
- You know Indian geography, festivals, weather patterns, and local customs
- You provide practical tips (budget, safety, transport, best times)
- You can create mini-itineraries when asked
- You use emojis sparingly for friendliness (🕌 🏖️ 🍛 🏔️ 🎉)

Response format:
- Keep answers to 3-5 sentences for simple questions
- Use bullet points for lists
- For itinerary requests, structure by day/time
- Always be helpful and encourage exploration of India"""


def _call_gemini(prompt, system=SYSTEM_CONTEXT):
    """Call Gemini API with the given prompt."""
    api_key = os.environ.get('GEMINI_API_KEY', '')
    if not api_key:
        return None

    try:
        import google.generativeai as genai
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-1.5-flash')
        full_prompt = f"{system}\n\n{prompt}"
        response = model.generate_content(full_prompt)
        return response.text.strip()
    except Exception:
        return None


def generate_ai_itinerary(city_data, num_days, budget, interests):
    """Generate a travel itinerary using Gemini AI with fallback."""
    api_key = os.environ.get('GEMINI_API_KEY', '')

    if not api_key:
        return build_fallback_itinerary(city_data, num_days, budget, interests)

    try:
        import google.generativeai as genai
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-1.5-flash')

        city_name = city_data.get('name', '')
        places_list = ', '.join([p['name'] for p in city_data.get('places', [])])
        foods_list = ', '.join([f['name'] for f in city_data.get('foods', [])])
        interests_str = ', '.join(interests) if interests else 'general sightseeing'

        prompt = f"""Create a detailed {num_days}-day travel itinerary for {city_name}, India.

Budget level: {budget}
Interests: {interests_str}

Available tourist places: {places_list if places_list else 'Use your knowledge of popular places in ' + city_name}
Famous foods to try: {foods_list if foods_list else 'Use your knowledge of famous foods in ' + city_name}

Return ONLY a valid JSON object (no markdown, no code fences) with this exact structure:
{{
  "city": "{city_name}",
  "num_days": {num_days},
  "budget_type": "{budget}",
  "estimated_daily_budget": <number in INR>,
  "estimated_total_budget": <number in INR>,
  "currency": "INR",
  "days": [
    {{
      "day": 1,
      "activities": [
        {{
          "time": "Morning",
          "activity": "Visit <place name>",
          "description": "<brief 1-line description>",
          "type": "<sightseeing|food|adventure|cultural|nature|shopping>"
        }}
      ]
    }}
  ]
}}

Rules:
- Distribute activities across Morning, Afternoon, Evening, and Night slots
- Include food recommendations for Evening/Night slots
- Make the itinerary realistic and well-paced
- Budget estimates: low=₹1000-2500/day, medium=₹3000-6000/day, luxury=₹8000-20000/day
- Include local experiences and hidden gems"""

        response = model.generate_content(prompt)
        text = response.text.strip()
        text = re.sub(r'^```(?:json)?\s*', '', text)
        text = re.sub(r'\s*```$', '', text)
        result = json.loads(text)
        return result

    except Exception:
        return build_fallback_itinerary(city_data, num_days, budget, interests)


def generate_dynamic_city_data(city_name, state=''):
    """Generate city data dynamically using AI for cities not in the database."""
    api_key = os.environ.get('GEMINI_API_KEY', '')

    location = f"{city_name}, {state}" if state else f"{city_name}, India"

    if not api_key:
        return _fallback_dynamic_city(city_name, state)

    try:
        import google.generativeai as genai
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-1.5-flash')

        prompt = f"""Generate comprehensive travel data for {location}.

Return ONLY a valid JSON object (no markdown, no code fences) with this structure:
{{
  "description": "<2-3 sentence description of the city for tourists>",
  "best_time_to_visit": "<best months/seasons to visit with brief reason>",
  "travel_tips": "<5-6 practical travel tips, separated by newlines>",
  "places": [
    {{
      "name": "<place name>",
      "description": "<1-2 sentence description>",
      "category": "<historical|nature|religious|cultural|adventure|beach>",
      "timing": "<opening hours>",
      "entry_fee": "<entry fee or Free>"
    }}
  ],
  "foods": [
    {{
      "name": "<food name>",
      "description": "<1 sentence description of the dish>"
    }}
  ]
}}

Include 6-8 tourist places and 4-5 famous local foods.
Make data accurate and helpful for travelers."""

        response = model.generate_content(prompt)
        text = response.text.strip()
        text = re.sub(r'^```(?:json)?\s*', '', text)
        text = re.sub(r'\s*```$', '', text)
        result = json.loads(text)
        return result

    except Exception:
        return _fallback_dynamic_city(city_name, state)


def _fallback_dynamic_city(city_name, state=''):
    """Generate basic city data without AI."""
    return {
        "description": f"{city_name} is a beautiful destination in {state or 'India'}, offering a unique blend of culture, history, and natural beauty. It's a wonderful place to explore Indian heritage and hospitality.",
        "best_time_to_visit": "October to March — Pleasant weather ideal for sightseeing and outdoor activities.",
        "travel_tips": "Carry comfortable walking shoes for sightseeing.\nTry local street food from popular stalls.\nUse local transport like autos and buses for an authentic experience.\nCarry cash as some places may not accept cards.\nRespect local customs and dress modestly at religious sites.\nDrink bottled water and carry sunscreen.",
        "places": [
            {"name": f"{city_name} Old Town", "description": f"Explore the historic heart of {city_name} with its charming streets and architecture.", "category": "cultural", "timing": "Open all day", "entry_fee": "Free"},
            {"name": f"{city_name} Main Temple", "description": f"Visit the most prominent temple in {city_name}, known for its spiritual significance.", "category": "religious", "timing": "6:00 AM - 8:00 PM", "entry_fee": "Free"},
            {"name": f"Local Market", "description": f"Browse through the vibrant local bazaar for handicrafts, spices, and souvenirs.", "category": "cultural", "timing": "9:00 AM - 9:00 PM", "entry_fee": "Free"},
            {"name": f"City Park", "description": f"A peaceful green space perfect for morning walks and relaxation.", "category": "nature", "timing": "6:00 AM - 7:00 PM", "entry_fee": "Free"},
            {"name": f"Heritage Walk", "description": f"Take a guided heritage walk through the historical quarters of {city_name}.", "category": "historical", "timing": "Flexible", "entry_fee": "₹200-500"},
        ],
        "foods": [
            {"name": "Local Thali", "description": f"A traditional platter offering a variety of {state or 'regional'} dishes in one meal."},
            {"name": "Street Chaat", "description": "Savory snacks like pani puri, bhel puri, and sev puri from local vendors."},
            {"name": "Regional Sweet", "description": f"Try the famous local sweet specialty of {city_name}."},
            {"name": "Chai & Snacks", "description": "Enjoy cutting chai with local savory snacks at a popular tea stall."},
        ],
    }


def chat_with_ai(message, city_context=None):
    """Handle chatbot queries about travel in India — enhanced version."""
    context = ""
    if city_context:
        context = f"\nThe user is currently browsing information about {city_context}. Tailor your response accordingly."

    prompt = f"""{SYSTEM_CONTEXT}{context}

User question: {message}

Provide a helpful, concise, and well-structured response. If the question is about a specific city, 
include practical details like best places, foods, budget tips, and best time to visit.
If asked for an itinerary, provide a brief day-by-day plan.
Keep the response under 200 words but make it informative."""

    result = _call_gemini(prompt, system="")

    if result:
        return result

    return _enhanced_fallback_chat(message)


def _enhanced_fallback_chat(message):
    """Comprehensive keyword-based fallback for chatbot."""
    msg = message.lower().strip()

    # ── Best time questions ──
    if any(w in msg for w in ['best time', 'when to visit', 'when should', 'which month', 'season']):
        city_responses = {
            'goa': "🏖️ **Best time to visit Goa: November to February**\n\nThe weather is perfect (25-32°C) for beaches and water sports. December-January is peak season with Christmas and New Year parties.\n\n**Monsoon (June-Sept):** Off-season but the lush green Goa is beautiful. Great deals on hotels!\n\n**Avoid:** April-May (extremely hot, 35°C+)",
            'varanasi': "🕌 **Best time to visit Varanasi: October to March**\n\nCool, comfortable weather perfect for exploring ghats and temples.\n\n**Special times:**\n• Dev Deepawali (Nov) — Million lamps on the ghats\n• Mahashivaratri — Grand celebrations\n• Holi — Colorful festivities in the holy city",
            'jaipur': "🏰 **Best time to visit Jaipur: October to March**\n\nPleasant winters (8-25°C) ideal for fort exploration.\n\n**Don't miss:**\n• January — Jaipur Literature Festival & Kite Festival\n• March — Elephant Festival\n• Evening visits to Nahargarh Fort for sunset views",
            'delhi': "🏛️ **Best time to visit Delhi: October to March**\n\nWinters are cool (5-20°C) and perfect for monuments.\n\n**Tips:**\n• October-November: Perfect weather, festive season\n• December-January: Cold but magical (foggy mornings)\n• Avoid April-June: Extreme heat (45°C+)",
            'udaipur': "🌅 **Best time to visit Udaipur: September to March**\n\n**Sept-Oct:** Lakes are full after monsoon, lush greenery\n**Nov-Feb:** Cool weather, perfect for boat rides and palace visits\n**March:** Pleasant before the heat sets in",
            'shimla': "🏔️ **Best time to visit Shimla:**\n• **Summer (Mar-Jun):** Cool escape from plains heat\n• **Winter (Dec-Feb):** Snowfall! Magical white landscapes\n• **Autumn (Sep-Nov):** Clear skies, gorgeous views",
            'manali': "🏔️ **Best time to visit Manali:**\n• **Summer (Apr-Jun):** Ideal for trekking and Rohtang Pass\n• **Winter (Dec-Feb):** Heavy snowfall, skiing at Solang Valley\n• **Monsoon:** Avoid due to landslides",
            'kerala': "🌴 **Best time to visit Kerala: September to March**\n\n• **Sep-Nov:** Post-monsoon green beauty, Onam festival\n• **Dec-Feb:** Peak season, perfect backwater cruises\n• **Jun-Aug:** Monsoon — great for Ayurveda retreats",
            'leh': "🏔️ **Best time to visit Leh-Ladakh: June to September**\n\nRoads are open and weather is pleasant (15-30°C).\n\n**Tips:**\n• June: Hemis Festival\n• July-Aug: Best weather but touristy\n• Acclimatize for 1-2 days due to high altitude",
            'rishikesh': "🧘 **Best time to visit Rishikesh:**\n• **Sept-Nov:** Perfect weather, river rafting season\n• **Feb-Apr:** Pleasant, International Yoga Festival (March)\n• **Avoid:** Jul-Aug (monsoon floods)",
        }

        for city, response in city_responses.items():
            if city in msg:
                return response

        return "🇮🇳 **Best time to visit India (generally):**\n\n• **Oct-Mar:** Best for most of India (pleasant winters)\n• **Apr-Jun:** Good for hill stations (Shimla, Manali, Darjeeling)\n• **Jul-Sep:** Monsoon — beautiful for Kerala, Northeast India\n\nWhich city are you planning to visit? I can give specific advice! 😊"

    # ── Food questions ──
    if any(w in msg for w in ['food', 'eat', 'try', 'cuisine', 'dish', 'restaurant', 'street food']):
        city_food = {
            'jaipur': "🍛 **Must-try foods in Jaipur:**\n\n• **Dal Baati Churma** — The king of Rajasthani cuisine\n• **Laal Maas** — Fiery red mutton curry\n• **Pyaaz Kachori** — Best at Rawat Mishtan Bhandar\n• **Ghewar** — Traditional disc-shaped sweet\n• **Lassi** — The legendary Lassiwala on MI Road (go before 2 PM!)\n\n**Where to eat:** Chokhi Dhani (authentic experience), Spice Court, LMB Hotel",
            'delhi': "🍛 **Must-try foods in Delhi:**\n\n• **Chole Bhature** — Sita Ram Diwan Chand, Paharganj\n• **Butter Chicken** — Moti Mahal, Daryaganj (the original!)\n• **Paranthas** — Paranthe Wali Gali, Chandni Chowk\n• **Kebabs** — Karim's near Jama Masjid\n• **Daulat Ki Chaat** — Winter-only milk froth delicacy\n• **Chaat** — Bengali Market or Haldiram's\n\n**Pro tip:** Old Delhi food walk is a must! 🤤",
            'goa': "🍛 **Must-try foods in Goa:**\n\n• **Fish Curry Rice** — The everyday Goan staple\n• **Pork Vindaloo** — Indo-Portuguese fiery classic\n• **Bebinca** — Multi-layered Goan dessert\n• **Prawn Balchão** — Spicy pickled prawns\n• **Feni** — Local cashew/coconut spirit\n\n**Where to eat:** Fisherman's Wharf, Britto's (Baga), Gunpowder",
            'varanasi': "🍛 **Must-try foods in Varanasi:**\n\n• **Kachori Sabzi** — Breakfast at Kachori Gali\n• **Banarasi Paan** — A cultural must-try!\n• **Thandai** — Refreshing cold drink (try the special Bhaang version during Holi)\n• **Malaiyo** — Winter morning delicacy of milk froth\n• **Tamatar Chaat** — Unique tomato-based chaat\n\n**Don't miss:** Blue Lassi near Manikarnika Ghat",
            'mumbai': "🍛 **Must-try foods in Mumbai:**\n\n• **Vada Pav** — Mumbai's iconic burger! (Ashok Vada Pav)\n• **Pav Bhaji** — Juhu Beach or Cannon Pav Bhaji\n• **Bombay Sandwich** — Street-side grilled classic\n• **Misal Pav** — Spicy sprouted lentil curry\n• **Seafood** — Gajalee or Trishna for crab\n• **Kulfi Falooda** — Bademiya or K. Rustom\n\n**Best areas:** Mohammed Ali Road, Carter Road, Khau Galli",
            'hyderabad': "🍛 **Must-try foods in Hyderabad:**\n\n• **Hyderabadi Biryani** — Paradise or Bawarchi\n• **Haleem** — Rich meat and wheat stew (Ramadan special)\n• **Irani Chai** — Nimrah Café near Charminar\n• **Double Ka Meetha** — Bread pudding Hyderabadi style\n• **Boti Kebab** — At Shah Ghouse\n\n**Must visit:** Gokul Chat, Munshi Naan",
        }

        for city, response in city_food.items():
            if city in msg:
                return response

        return "🍛 **India is a food paradise!** Each region has unique flavors:\n\n• **North:** Rich curries, tandoor breads, kebabs\n• **South:** Dosa, idli, coconut-based curries\n• **East:** Fish, sweets (rasgulla, sandesh)\n• **West:** Pav bhaji, dhokla, Goan seafood\n• **Street food:** Chaat, pani puri, samosas everywhere!\n\nWhich city are you visiting? I'll give you specific food recommendations! 🤤"

    # ── Places questions ──
    if any(w in msg for w in ['places', 'visit', 'see', 'attraction', 'tourist', 'sightseeing', 'explore', 'things to do']):
        city_places = {
            'jaipur': "🏰 **Top places to visit in Jaipur:**\n\n1. **Amber Fort** — Stunning hilltop fort with Mirror Palace\n2. **Hawa Mahal** — Iconic Palace of Winds (953 windows!)\n3. **City Palace** — Royal Rajasthani architecture\n4. **Jantar Mantar** — UNESCO astronomical instruments\n5. **Nahargarh Fort** — Best sunset point!\n6. **Jal Mahal** — Beautiful water palace\n7. **Albert Hall Museum** — Night illumination is spectacular\n\n**Pro tip:** Get a composite ticket for multiple monuments! 🎫",
            'delhi': "🏛️ **Top places to visit in Delhi:**\n\n1. **Red Fort** — Mughal masterpiece (Sound & Light show!)\n2. **India Gate** — War memorial, beautiful at night\n3. **Qutub Minar** — Tallest brick minaret\n4. **Humayun's Tomb** — Precursor to Taj Mahal\n5. **Lotus Temple** — Stunning Bahai temple\n6. **Akshardham** — Must-see temple complex\n7. **Chandni Chowk** — Old Delhi food & shopping\n\n**Pro tip:** Use Delhi Metro — it's cheap and covers everywhere!",
            'goa': "🏖️ **Top places to visit in Goa:**\n\n1. **Baga Beach** — Lively, water sports, nightlife\n2. **Palolem Beach** — Serene, crescent-shaped beauty\n3. **Fort Aguada** — Portuguese fort with ocean views\n4. **Basilica of Bom Jesus** — UNESCO World Heritage\n5. **Dudhsagar Falls** — 310m waterfall in the jungle\n6. **Anjuna Flea Market** — Wednesday market with live music\n7. **Chapora Fort** — The famous \"Dil Chahta Hai\" fort\n\n**Pro tip:** Rent a scooter to explore! 🛵",
            'varanasi': "🕌 **Top places to visit in Varanasi:**\n\n1. **Dashashwamedh Ghat** — Evening Ganga Aarti (7 PM daily)\n2. **Kashi Vishwanath Temple** — One of 12 Jyotirlingas\n3. **Sarnath** — Where Buddha gave his first sermon\n4. **Manikarnika Ghat** — Sacred cremation ghat\n5. **Assi Ghat** — Morning yoga, sunset views\n6. **Ramnagar Fort** — 18th century museum\n7. **Sunrise Boat Ride** — Life-changing experience!\n\n**Pro tip:** The morning boat ride is unmissable! 🛶",
        }

        for city, response in city_places.items():
            if city in msg:
                return response

        return "🇮🇳 **India has incredible destinations across every region!**\n\n• **Heritage:** Jaipur, Agra, Delhi, Hampi\n• **Beaches:** Goa, Kerala, Andaman Islands\n• **Mountains:** Manali, Shimla, Leh-Ladakh, Darjeeling\n• **Spiritual:** Varanasi, Rishikesh, Amritsar, Tirupati\n• **Nature:** Munnar, Coorg, Valley of Flowers\n• **Culture:** Kolkata, Udaipur, Jaisalmer\n\nWhich type of destination interests you? I can recommend specific places! 🗺️"

    # ── Safety questions ──
    if any(w in msg for w in ['safe', 'safety', 'danger', 'crime', 'solo', 'female', 'woman']):
        return "🛡️ **Safety tips for traveling in India:**\n\n**General:**\n• India is generally safe for tourists — millions visit each year!\n• Use trusted transport (Uber/Ola, prepaid taxis)\n• Keep copies of important documents\n• Stay in well-reviewed hotels (check Google reviews)\n\n**For solo/female travelers:**\n• Stick to popular tourist areas\n• Avoid isolated places after dark\n• Dress conservatively at religious sites\n• Share your itinerary with someone back home\n• Trust your instincts — locals are usually very helpful!\n\n**Emergency:** Tourist helpline: 1363 | Women helpline: 1091\n\nWhich city are you planning to visit? I can give specific safety advice! 😊"

    # ── Budget questions ──
    if any(w in msg for w in ['budget', 'cost', 'cheap', 'expensive', 'money', 'price', 'afford']):
        return "💰 **India travel budget guide (per person/day):**\n\n**Budget (₹1,000-2,500):**\n• Hostels/guesthouses\n• Street food & local eateries\n• Public transport & shared autos\n\n**Mid-range (₹3,000-8,000):**\n• 3-star hotels\n• Mix of restaurants & street food\n• Private taxis occasionally\n\n**Luxury (₹10,000+):**\n• 5-star hotels & heritage stays\n• Fine dining\n• Private cars with drivers\n\n**Money-saving tips:**\n• Book trains on IRCTC early\n• Eat where locals eat\n• Visit monuments on free entry days\n• Bargain at markets (30-50% of asking price)\n\nWhich city & budget range? I can plan accordingly! 😊"

    # ── Itinerary/plan questions ──
    if any(w in msg for w in ['plan', 'itinerary', 'trip', 'day', 'schedule', 'tour']):
        for city in ['goa', 'delhi', 'jaipur', 'varanasi', 'udaipur', 'mumbai', 'kerala']:
            if city in msg:
                return f"🗺️ I'd love to help plan your {city.title()} trip!\n\nFor a personalized day-by-day itinerary, head to our **AI Planner** page:\n1. Select {city.title()} as your destination\n2. Choose number of days (1-7)\n3. Set your budget (Budget/Comfort/Luxury)\n4. Pick your interests\n5. Click 'Generate AI Itinerary'!\n\nYou'll get a complete day-wise plan with Morning/Afternoon/Evening activities, food recommendations, and a downloadable PDF! 📥\n\nWant me to share some quick highlights for {city.title()} instead?"

        return "🗺️ **I can help you plan a trip!**\n\nUse our **AI Trip Planner** for a detailed itinerary:\n1. Choose your city\n2. Select days (1-7)\n3. Set budget\n4. Pick interests\n5. Get a complete plan!\n\nOr tell me which city you're interested in and I'll share some quick tips! 😊"

    # ── Transport questions ──
    if any(w in msg for w in ['transport', 'train', 'flight', 'bus', 'how to reach', 'getting', 'travel to']):
        return "🚂 **Getting around India:**\n\n**Between cities:**\n• **Trains:** Book on IRCTC (irctc.co.in) — AC classes recommended\n• **Flights:** IndiGo, SpiceJet, Air India for budget options\n• **Buses:** Redbus.in for bookings, Volvo sleeper for overnight\n\n**Within cities:**\n• **Metro:** Delhi, Mumbai, Bangalore, Hyderabad, Kolkata\n• **Uber/Ola:** Available in all major cities\n• **Auto-rickshaws:** Insist on meter or negotiate before\n• **Local trains:** Mumbai's lifeline!\n\n**Pro tips:**\n• Book trains 2-3 months in advance\n• Download Ola/Uber before arriving\n• For Rajasthan, hire a car with driver (₹2000-3000/day)"

    # ── Greeting ──
    if any(w in msg for w in ['hi', 'hello', 'hey', 'namaste', 'help', 'start']):
        return "🙏 **Namaste! Welcome to India Travel Planner!**\n\nI'm your AI travel assistant for India. I can help with:\n\n• 🏙️ **City recommendations** — \"Best places in Jaipur?\"\n• 🍛 **Food suggestions** — \"What to eat in Delhi?\"\n• 📅 **Best time to visit** — \"When to visit Goa?\"\n• 💰 **Budget planning** — \"How much for a Rajasthan trip?\"\n• 🗺️ **Trip itineraries** — \"Plan a 3-day trip to Kerala\"\n• 🛡️ **Safety tips** — \"Is Varanasi safe for solo travel?\"\n\nJust type your question and I'll help you plan the perfect Indian adventure! 🇮🇳"

    # ── Default ──
    return "🙏 **I'm your India Travel Assistant!**\n\nI can help you with:\n• 🏙️ Best places to visit in any Indian city\n• 🍛 Famous local foods and where to eat\n• 📅 Best time to visit\n• 💰 Budget planning and tips\n• 🗺️ Trip itineraries\n• 🛡️ Safety advice\n\nTry asking something like:\n• \"What should I see in Jaipur?\"\n• \"Best food in Delhi?\"\n• \"Plan a trip to Goa\"\n\nI'm here to help! 😊"
