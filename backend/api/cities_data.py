"""
Comprehensive dataset of major Indian cities for universal search.
"""

INDIAN_CITIES = [
    {"name": "Delhi", "state": "Delhi", "lat": 28.6139, "lng": 77.2090},
    {"name": "Mumbai", "state": "Maharashtra", "lat": 19.0760, "lng": 72.8777},
    {"name": "Bangalore", "state": "Karnataka", "lat": 12.9716, "lng": 77.5946},
    {"name": "Hyderabad", "state": "Telangana", "lat": 17.3850, "lng": 78.4867},
    {"name": "Chennai", "state": "Tamil Nadu", "lat": 13.0827, "lng": 80.2707},
    {"name": "Kolkata", "state": "West Bengal", "lat": 22.5726, "lng": 88.3639},
    {"name": "Pune", "state": "Maharashtra", "lat": 18.5204, "lng": 73.8567},
    {"name": "Ahmedabad", "state": "Gujarat", "lat": 23.0225, "lng": 72.5714},
    {"name": "Jaipur", "state": "Rajasthan", "lat": 26.9124, "lng": 75.7873},
    {"name": "Lucknow", "state": "Uttar Pradesh", "lat": 26.8467, "lng": 80.9462},
    {"name": "Chandigarh", "state": "Chandigarh", "lat": 30.7333, "lng": 76.7794},
    {"name": "Bhopal", "state": "Madhya Pradesh", "lat": 23.2599, "lng": 77.4126},
    {"name": "Indore", "state": "Madhya Pradesh", "lat": 22.7196, "lng": 75.8577},
    {"name": "Nagpur", "state": "Maharashtra", "lat": 21.1458, "lng": 79.0882},
    {"name": "Patna", "state": "Bihar", "lat": 25.6093, "lng": 85.1376},
    {"name": "Kochi", "state": "Kerala", "lat": 9.9312, "lng": 76.2673},
    {"name": "Thiruvananthapuram", "state": "Kerala", "lat": 8.5241, "lng": 76.9366},
    {"name": "Goa", "state": "Goa", "lat": 15.2993, "lng": 74.1240},
    {"name": "Varanasi", "state": "Uttar Pradesh", "lat": 25.3176, "lng": 83.0068},
    {"name": "Udaipur", "state": "Rajasthan", "lat": 24.5854, "lng": 73.7125},
    {"name": "Jodhpur", "state": "Rajasthan", "lat": 26.2389, "lng": 73.0243},
    {"name": "Jaisalmer", "state": "Rajasthan", "lat": 26.9157, "lng": 70.9083},
    {"name": "Agra", "state": "Uttar Pradesh", "lat": 27.1767, "lng": 78.0081},
    {"name": "Amritsar", "state": "Punjab", "lat": 31.6340, "lng": 74.8723},
    {"name": "Shimla", "state": "Himachal Pradesh", "lat": 31.1048, "lng": 77.1734},
    {"name": "Manali", "state": "Himachal Pradesh", "lat": 32.2396, "lng": 77.1887},
    {"name": "Dharamshala", "state": "Himachal Pradesh", "lat": 32.2190, "lng": 76.3234},
    {"name": "Rishikesh", "state": "Uttarakhand", "lat": 30.0869, "lng": 78.2676},
    {"name": "Haridwar", "state": "Uttarakhand", "lat": 29.9457, "lng": 78.1642},
    {"name": "Dehradun", "state": "Uttarakhand", "lat": 30.3165, "lng": 78.0322},
    {"name": "Mussoorie", "state": "Uttarakhand", "lat": 30.4598, "lng": 78.0644},
    {"name": "Nainital", "state": "Uttarakhand", "lat": 29.3919, "lng": 79.4542},
    {"name": "Darjeeling", "state": "West Bengal", "lat": 27.0360, "lng": 88.2627},
    {"name": "Gangtok", "state": "Sikkim", "lat": 27.3389, "lng": 88.6065},
    {"name": "Shillong", "state": "Meghalaya", "lat": 25.5788, "lng": 91.8933},
    {"name": "Guwahati", "state": "Assam", "lat": 26.1445, "lng": 91.7362},
    {"name": "Imphal", "state": "Manipur", "lat": 24.8170, "lng": 93.9368},
    {"name": "Aizawl", "state": "Mizoram", "lat": 23.7271, "lng": 92.7176},
    {"name": "Kohima", "state": "Nagaland", "lat": 25.6751, "lng": 94.1086},
    {"name": "Itanagar", "state": "Arunachal Pradesh", "lat": 27.0844, "lng": 93.6053},
    {"name": "Agartala", "state": "Tripura", "lat": 23.8315, "lng": 91.2868},
    {"name": "Coorg", "state": "Karnataka", "lat": 12.3375, "lng": 75.8069},
    {"name": "Mysore", "state": "Karnataka", "lat": 12.2958, "lng": 76.6394},
    {"name": "Hampi", "state": "Karnataka", "lat": 15.3350, "lng": 76.4600},
    {"name": "Ooty", "state": "Tamil Nadu", "lat": 11.4102, "lng": 76.6950},
    {"name": "Kodaikanal", "state": "Tamil Nadu", "lat": 10.2381, "lng": 77.4892},
    {"name": "Madurai", "state": "Tamil Nadu", "lat": 9.9252, "lng": 78.1198},
    {"name": "Pondicherry", "state": "Puducherry", "lat": 11.9416, "lng": 79.8083},
    {"name": "Alleppey", "state": "Kerala", "lat": 9.4981, "lng": 76.3388},
    {"name": "Munnar", "state": "Kerala", "lat": 10.0889, "lng": 77.0595},
    {"name": "Wayanad", "state": "Kerala", "lat": 11.6854, "lng": 76.1320},
    {"name": "Leh", "state": "Ladakh", "lat": 34.1526, "lng": 77.5771},
    {"name": "Srinagar", "state": "Jammu & Kashmir", "lat": 34.0837, "lng": 74.7973},
    {"name": "Gulmarg", "state": "Jammu & Kashmir", "lat": 34.0484, "lng": 74.3805},
    {"name": "Pahalgam", "state": "Jammu & Kashmir", "lat": 34.0161, "lng": 75.3150},
    {"name": "Jammu", "state": "Jammu & Kashmir", "lat": 32.7266, "lng": 74.8570},
    {"name": "Ranchi", "state": "Jharkhand", "lat": 23.3441, "lng": 85.3096},
    {"name": "Bhubaneswar", "state": "Odisha", "lat": 20.2961, "lng": 85.8245},
    {"name": "Puri", "state": "Odisha", "lat": 19.8135, "lng": 85.8312},
    {"name": "Konark", "state": "Odisha", "lat": 19.8876, "lng": 86.0945},
    {"name": "Raipur", "state": "Chhattisgarh", "lat": 21.2514, "lng": 81.6296},
    {"name": "Visakhapatnam", "state": "Andhra Pradesh", "lat": 17.6868, "lng": 83.2185},
    {"name": "Tirupati", "state": "Andhra Pradesh", "lat": 13.6288, "lng": 79.4192},
    {"name": "Vijayawada", "state": "Andhra Pradesh", "lat": 16.5062, "lng": 80.6480},
    {"name": "Aurangabad", "state": "Maharashtra", "lat": 19.8762, "lng": 75.3433},
    {"name": "Nashik", "state": "Maharashtra", "lat": 19.9975, "lng": 73.7898},
    {"name": "Lonavala", "state": "Maharashtra", "lat": 18.7546, "lng": 73.4062},
    {"name": "Mahabaleshwar", "state": "Maharashtra", "lat": 17.9307, "lng": 73.6477},
    {"name": "Ajmer", "state": "Rajasthan", "lat": 26.4499, "lng": 74.6399},
    {"name": "Pushkar", "state": "Rajasthan", "lat": 26.4898, "lng": 74.5511},
    {"name": "Mount Abu", "state": "Rajasthan", "lat": 24.5926, "lng": 72.7156},
    {"name": "Ranthambore", "state": "Rajasthan", "lat": 26.0173, "lng": 76.5026},
    {"name": "Bikaner", "state": "Rajasthan", "lat": 28.0229, "lng": 73.3119},
    {"name": "Mathura", "state": "Uttar Pradesh", "lat": 27.4924, "lng": 77.6737},
    {"name": "Vrindavan", "state": "Uttar Pradesh", "lat": 27.5830, "lng": 77.7010},
    {"name": "Allahabad", "state": "Uttar Pradesh", "lat": 25.4358, "lng": 81.8463},
    {"name": "Ayodhya", "state": "Uttar Pradesh", "lat": 26.7922, "lng": 82.1998},
    {"name": "Khajuraho", "state": "Madhya Pradesh", "lat": 24.8318, "lng": 79.9199},
    {"name": "Orchha", "state": "Madhya Pradesh", "lat": 25.3520, "lng": 78.6408},
    {"name": "Ujjain", "state": "Madhya Pradesh", "lat": 23.1765, "lng": 75.7885},
    {"name": "Gwalior", "state": "Madhya Pradesh", "lat": 26.2183, "lng": 78.1828},
    {"name": "Bodh Gaya", "state": "Bihar", "lat": 24.6961, "lng": 84.9869},
    {"name": "Rajgir", "state": "Bihar", "lat": 25.0283, "lng": 85.4218},
    {"name": "Vaishali", "state": "Bihar", "lat": 25.9840, "lng": 85.1376},
    {"name": "Surat", "state": "Gujarat", "lat": 21.1702, "lng": 72.8311},
    {"name": "Vadodara", "state": "Gujarat", "lat": 22.3072, "lng": 73.1812},
    {"name": "Dwarka", "state": "Gujarat", "lat": 22.2394, "lng": 68.9678},
    {"name": "Somnath", "state": "Gujarat", "lat": 20.8880, "lng": 70.4013},
    {"name": "Kutch", "state": "Gujarat", "lat": 23.7337, "lng": 69.8597},
    {"name": "Diu", "state": "Daman & Diu", "lat": 20.7144, "lng": 70.9874},
    {"name": "Port Blair", "state": "Andaman & Nicobar", "lat": 11.6234, "lng": 92.7265},
    {"name": "Lakshadweep", "state": "Lakshadweep", "lat": 10.5667, "lng": 72.6417},
    {"name": "Coimbatore", "state": "Tamil Nadu", "lat": 11.0168, "lng": 76.9558},
    {"name": "Thanjavur", "state": "Tamil Nadu", "lat": 10.7870, "lng": 79.1378},
    {"name": "Kanyakumari", "state": "Tamil Nadu", "lat": 8.0883, "lng": 77.5385},
    {"name": "Rameswaram", "state": "Tamil Nadu", "lat": 9.2876, "lng": 79.3129},
    {"name": "Mamallapuram", "state": "Tamil Nadu", "lat": 12.6269, "lng": 80.1927},
    {"name": "Mangalore", "state": "Karnataka", "lat": 12.9141, "lng": 74.8560},
    {"name": "Badami", "state": "Karnataka", "lat": 15.9200, "lng": 75.6800},
    {"name": "Hospet", "state": "Karnataka", "lat": 15.2689, "lng": 76.3909},
    {"name": "Panaji", "state": "Goa", "lat": 15.4909, "lng": 73.8278},
    {"name": "Margao", "state": "Goa", "lat": 15.2832, "lng": 73.9862},
    {"name": "Vasco da Gama", "state": "Goa", "lat": 15.3982, "lng": 73.8113},
    {"name": "Auroville", "state": "Tamil Nadu", "lat": 12.0062, "lng": 79.8107},
    {"name": "Spiti Valley", "state": "Himachal Pradesh", "lat": 32.2461, "lng": 78.0349},
    {"name": "Tawang", "state": "Arunachal Pradesh", "lat": 27.5860, "lng": 91.8698},
    {"name": "Cherrapunji", "state": "Meghalaya", "lat": 25.2975, "lng": 91.7320},
    {"name": "Kaziranga", "state": "Assam", "lat": 26.5775, "lng": 93.1711},
    {"name": "Sundarbans", "state": "West Bengal", "lat": 21.9497, "lng": 89.1833},
    {"name": "Jim Corbett", "state": "Uttarakhand", "lat": 29.5300, "lng": 78.7747},
    {"name": "Valley of Flowers", "state": "Uttarakhand", "lat": 30.7275, "lng": 79.6050},
    {"name": "Zanskar", "state": "Ladakh", "lat": 33.5000, "lng": 76.8500},
    {"name": "Turtuk", "state": "Ladakh", "lat": 34.8476, "lng": 76.8219},
    {"name": "Kasol", "state": "Himachal Pradesh", "lat": 32.0101, "lng": 77.3150},
    {"name": "McLeod Ganj", "state": "Himachal Pradesh", "lat": 32.2426, "lng": 76.3213},
    {"name": "Bir Billing", "state": "Himachal Pradesh", "lat": 31.8800, "lng": 76.7200},
]


def search_cities(query):
    """Search for Indian cities matching the query string."""
    if not query:
        return []
    q = query.strip().lower()
    matches = []
    for city in INDIAN_CITIES:
        if q in city["name"].lower() or q in city["state"].lower():
            matches.append(city)
    return matches[:20]


def find_city(name):
    """Find a city by exact or close name match."""
    if not name:
        return None
    q = name.strip().lower()
    # Exact match first
    for city in INDIAN_CITIES:
        if city["name"].lower() == q:
            return city
    # Partial match
    for city in INDIAN_CITIES:
        if q in city["name"].lower():
            return city
    return None
