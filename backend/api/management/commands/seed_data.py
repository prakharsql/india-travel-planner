"""
Management command to seed the database with Indian cities, places, and foods.
"""
from django.core.management.base import BaseCommand
from api.models import City, Place, Food


class Command(BaseCommand):
    help = 'Seed the database with Indian cities, tourist places, and famous foods'

    def handle(self, *args, **options):
        self.stdout.write('Seeding database...')

        # Clear existing data
        Food.objects.all().delete()
        Place.objects.all().delete()
        City.objects.all().delete()

        cities_data = [
            {
                'name': 'Delhi',
                'state': 'Delhi',
                'description': 'Delhi, India\'s capital territory, is a massive metropolitan area in the country\'s north. It is a city that bridges two different worlds — Old Delhi, the historic capital of Muslim India, a labyrinth of narrow lanes lined with crumbling havelis, and New Delhi, the imperial city created by the British Raj, full of wide tree-lined boulevards and grand colonial architecture.',
                'best_time_to_visit': 'October to March — Cool and pleasant weather, perfect for sightseeing. Avoid the scorching summers (April-June) and monsoon (July-September).',
                'image': 'https://images.unsplash.com/photo-1587474260584-136574528ed5?w=800&auto=format',
                'latitude': 28.6139,
                'longitude': 77.2090,
                'travel_tips': 'Use the Delhi Metro for convenient travel — it covers most tourist spots.\nCarry a water bottle and sunscreen, especially during warm months.\nBargain at street markets like Chandni Chowk and Sarojini Nagar.\nTry street food but stick to busy stalls for better hygiene.\nBook monument tickets online to skip queues at popular sites.\nKeep valuables secure in crowded areas.',
                'places': [
                    {'name': 'Red Fort', 'description': 'The iconic Mughal fortress built in 1638 by Emperor Shah Jahan, known for its massive red sandstone walls. It served as the main residence of the Mughal emperors for nearly 200 years.', 'category': 'historical', 'timing': '9:30 AM - 4:30 PM (Closed Monday)', 'entry_fee': '₹35 (Indians), ₹500 (Foreigners)', 'latitude': 28.6562, 'longitude': 77.2410, 'image': 'https://images.unsplash.com/photo-1585135497273-1a86d9d9b7f0?w=600&auto=format'},
                    {'name': 'India Gate', 'description': 'A 42-meter tall war memorial arch built in 1931, dedicated to 70,000 soldiers who died in World War I. The eternal flame Amar Jawan Jyoti burns beneath the arch.', 'category': 'historical', 'timing': 'Open 24 hours', 'entry_fee': 'Free', 'latitude': 28.6129, 'longitude': 77.2295, 'image': 'https://images.unsplash.com/photo-1597040663342-45b6af3d7489?w=600&auto=format'},
                    {'name': 'Qutub Minar', 'description': 'A 73-meter tall UNESCO World Heritage Site, the tallest brick minaret in the world. Built in 1193 by Qutb-ud-din Aibak, it features intricate carvings and inscriptions.', 'category': 'historical', 'timing': '7:00 AM - 5:00 PM', 'entry_fee': '₹35 (Indians), ₹550 (Foreigners)', 'latitude': 28.5245, 'longitude': 77.1855, 'image': 'https://images.unsplash.com/photo-1548013146-72479768bada?w=600&auto=format'},
                    {'name': 'Lotus Temple', 'description': 'A stunning Bahai House of Worship shaped like a lotus flower with 27 marble petals. Winner of numerous architectural awards, it welcomes people of all faiths.', 'category': 'religious', 'timing': '9:00 AM - 5:30 PM (Closed Monday)', 'entry_fee': 'Free', 'latitude': 28.5535, 'longitude': 77.2588, 'image': 'https://images.unsplash.com/photo-1621427640389-b3f26d4f7108?w=600&auto=format'},
                    {'name': 'Humayun\'s Tomb', 'description': 'The first garden-tomb on the Indian subcontinent, built in 1570. This UNESCO World Heritage Site inspired the design of the Taj Mahal.', 'category': 'historical', 'timing': '6:00 AM - 6:00 PM', 'entry_fee': '₹35 (Indians), ₹550 (Foreigners)', 'latitude': 28.5933, 'longitude': 77.2507, 'image': 'https://images.unsplash.com/photo-1623689048105-a17b1e1936b8?w=600&auto=format'},
                    {'name': 'Chandni Chowk', 'description': 'One of the oldest and busiest markets in Old Delhi, established by Emperor Shah Jahan in the 17th century. A paradise for street food lovers and shoppers.', 'category': 'cultural', 'timing': 'Open all day (shops: 9:30 AM - 8:00 PM)', 'entry_fee': 'Free', 'latitude': 28.6506, 'longitude': 77.2334, 'image': 'https://images.unsplash.com/photo-1567157577867-05ccb1388e13?w=600&auto=format'},
                    {'name': 'Akshardham Temple', 'description': 'A magnificent Hindu temple complex showcasing 10,000 years of Indian culture through exhibitions, musical fountain shows, and stunning architecture carved from pink sandstone and marble.', 'category': 'religious', 'timing': '9:30 AM - 6:30 PM (Closed Monday)', 'entry_fee': 'Free (Shows: ₹170)', 'latitude': 28.6127, 'longitude': 77.2773, 'image': 'https://images.unsplash.com/photo-1597735881932-d9664c9bbcea?w=600&auto=format'},
                ],
                'foods': [
                    {'name': 'Chole Bhature', 'description': 'Spicy chickpea curry served with deep-fried puffed bread — Delhi\'s most iconic breakfast dish. Best enjoyed at Sita Ram Diwan Chand in Paharganj.'},
                    {'name': 'Butter Chicken', 'description': 'Creamy tomato-based chicken curry invented in Delhi in the 1950s. The original is at Moti Mahal in Daryaganj.'},
                    {'name': 'Paranthe Wali Gali', 'description': 'A famous lane in Chandni Chowk serving stuffed paranthas (flatbreads) with various fillings like potato, paneer, and even rabri, since the 1870s.'},
                    {'name': 'Daulat Ki Chaat', 'description': 'A seasonal winter delicacy made from milk froth, saffron, and pistachios. This ethereal sweet is available only from November to February.'},
                    {'name': 'Kebabs at Jama Masjid', 'description': 'Succulent seekh kebabs and tikkas from the legendary eateries near Jama Masjid. Karim\'s has been serving since 1913.'},
                ],
            },
            {
                'name': 'Jaipur',
                'state': 'Rajasthan',
                'description': 'Known as the "Pink City" due to its characteristic terracotta-pink buildings, Jaipur is the capital of Rajasthan and a UNESCO World Heritage City. Founded in 1727 by Maharaja Sawai Jai Singh II, it was India\'s first planned city. Jaipur forms part of the famous Golden Triangle tourist circuit along with Delhi and Agra.',
                'best_time_to_visit': 'October to March — Pleasant winter weather ideal for exploring forts and palaces. January hosts the famous Jaipur Literature Festival.',
                'image': 'https://images.unsplash.com/photo-1477587458883-47145ed94245?w=800&auto=format',
                'latitude': 26.9124,
                'longitude': 75.7873,
                'travel_tips': 'Hire a local guide at Amber Fort for the fascinating history and secret passages.\nWear comfortable walking shoes — the forts involve a lot of climbing.\nVisit Hawa Mahal early morning for the best photographs.\nThe famous Lassiwala on MI Road closes by afternoon — go early!\nShop for block-printed textiles at Johari Bazaar.\nTry to time your visit with the Elephant Festival or Kite Festival for a magical experience.',
                'places': [
                    {'name': 'Amber Fort', 'description': 'A majestic hilltop fort built from red sandstone and marble, known for its artistic Hindu-style elements. The Sheesh Mahal (Mirror Palace) inside is breathtaking with thousands of tiny mirrors.', 'category': 'historical', 'timing': '8:00 AM - 5:30 PM', 'entry_fee': '₹100 (Indians), ₹500 (Foreigners)', 'latitude': 26.9855, 'longitude': 75.8513, 'image': 'https://images.unsplash.com/photo-1599661046289-e31897846e41?w=600&auto=format'},
                    {'name': 'Hawa Mahal', 'description': 'The iconic "Palace of Winds" with 953 small windows (jharokhas) designed so royal women could observe street life without being seen. Built in 1799, its pink sandstone facade resembles a honeycomb.', 'category': 'historical', 'timing': '9:00 AM - 5:00 PM', 'entry_fee': '₹50 (Indians), ₹200 (Foreigners)', 'latitude': 26.9239, 'longitude': 75.8267, 'image': 'https://images.unsplash.com/photo-1574313653331-65370e384207?w=600&auto=format'},
                    {'name': 'City Palace', 'description': 'A stunning blend of Rajasthani and Mughal architecture, the palace complex includes courtyards, gardens, and museums. Part of it is still a royal residence.', 'category': 'historical', 'timing': '9:30 AM - 5:00 PM', 'entry_fee': '₹200 (Indians), ₹700 (Foreigners)', 'latitude': 26.9258, 'longitude': 75.8237, 'image': 'https://images.unsplash.com/photo-1603262110263-fb0112e7cc33?w=600&auto=format'},
                    {'name': 'Jantar Mantar', 'description': 'UNESCO World Heritage astronomical observation site built by Maharaja Jai Singh II in 1734. Houses the world\'s largest stone sundial (27m tall) that tells time accurate to 2 seconds.', 'category': 'historical', 'timing': '9:00 AM - 4:30 PM', 'entry_fee': '₹50 (Indians), ₹200 (Foreigners)', 'latitude': 26.9247, 'longitude': 75.8245, 'image': 'https://images.unsplash.com/photo-1602508453274-d193b6637c5c?w=600&auto=format'},
                    {'name': 'Nahargarh Fort', 'description': 'Perched on the Aravalli Hills, this fort offers panoramic views of Jaipur city, especially stunning at sunset. The Madhavendra Bhawan inside has interconnected suites for the king\'s queens.', 'category': 'historical', 'timing': '10:00 AM - 5:30 PM', 'entry_fee': '₹50 (Indians), ₹200 (Foreigners)', 'latitude': 26.9371, 'longitude': 75.8153, 'image': 'https://images.unsplash.com/photo-1590689081018-80297e0e0222?w=600&auto=format'},
                    {'name': 'Jal Mahal', 'description': 'The beautiful "Water Palace" situated in the middle of Man Sagar Lake. While visitors can\'t enter the palace, the view from the lakeside is spectacular, especially at dusk.', 'category': 'historical', 'timing': 'Viewing: 6:00 AM - 6:00 PM', 'entry_fee': 'Free (viewing from shore)', 'latitude': 26.9530, 'longitude': 75.8460, 'image': 'https://images.unsplash.com/photo-1603204077167-2fa0397f27c2?w=600&auto=format'},
                    {'name': 'Albert Hall Museum', 'description': 'The oldest museum of Rajasthan, built in 1876 in Indo-Saracenic architecture. Houses an Egyptian mummy, an extensive collection of paintings, carpets, ivory, and metal sculptures.', 'category': 'cultural', 'timing': '9:00 AM - 5:00 PM', 'entry_fee': '₹40 (Indians), ₹300 (Foreigners)', 'latitude': 26.9117, 'longitude': 75.8196, 'image': 'https://images.unsplash.com/photo-1610715946174-13deafb0ec6e?w=600&auto=format'},
                ],
                'foods': [
                    {'name': 'Dal Baati Churma', 'description': 'The quintessential Rajasthani dish — hard wheat rolls (baati) served with spiced lentils (dal) and a sweet crumbled wheat mixture (churma). A royal feast in every bite.'},
                    {'name': 'Laal Maas', 'description': 'A fiery Rajasthani mutton curry cooked with mathania red chilies, giving it an intense red color and deep flavor. A warrior\'s dish from the royal kitchens.'},
                    {'name': 'Pyaaz Kachori', 'description': 'Large, crispy deep-fried pastries stuffed with spiced onion filling, served with tangy tamarind chutney. Best at Rawat Mishtan Bhandar.'},
                    {'name': 'Ghewar', 'description': 'A traditional Rajasthani disc-shaped sweet made from flour and soaked in sugar syrup, often topped with rabri and nuts. Especially popular during the Teej festival.'},
                    {'name': 'Lassi at Lassiwala', 'description': 'The legendary thick, creamy lassi served in clay cups at the original Lassiwala shop on MI Road since 1944. A must-visit Jaipur institution.'},
                ],
            },
            {
                'name': 'Goa',
                'state': 'Goa',
                'description': 'India\'s smallest state by area, Goa is a paradise of sun-kissed beaches, Portuguese colonial architecture, vibrant nightlife, and lush spice plantations. Known as the "Pearl of the Orient," Goa\'s unique culture is a beautiful blend of Indian and Portuguese influences, visible in its cuisine, churches, and colorful houses.',
                'best_time_to_visit': 'November to February — Perfect beach weather, festive season with Christmas and New Year celebrations, and pleasant temperatures around 25-32°C.',
                'image': 'https://images.unsplash.com/photo-1512343879784-a960bf40e7f2?w=800&auto=format',
                'latitude': 15.2993,
                'longitude': 74.1240,
                'travel_tips': 'Rent a scooter or bike to explore — it\'s the easiest way to get around Goa.\nNorth Goa is more lively and touristy; South Goa is quieter and more scenic.\nVisit the Saturday Night Market at Arpora for a unique shopping experience.\nCarry cash for beach shacks — many don\'t accept cards.\nAlways apply sunscreen — the tropical sun is strong even on cloudy days.\nTry water sports at Calangute or Baga Beach.',
                'places': [
                    {'name': 'Baga Beach', 'description': 'One of Goa\'s most popular beaches known for its lively atmosphere, water sports, beach shacks, and vibrant nightlife. The Saturday Night Market nearby is a must-visit.', 'category': 'beach', 'timing': 'Open 24 hours', 'entry_fee': 'Free', 'latitude': 15.5553, 'longitude': 73.7516, 'image': 'https://images.unsplash.com/photo-1539635278303-d4002c07eae3?w=600&auto=format'},
                    {'name': 'Basilica of Bom Jesus', 'description': 'A UNESCO World Heritage Site built in 1605, it holds the mortal remains of St. Francis Xavier. One of the finest examples of baroque architecture in India.', 'category': 'historical', 'timing': '9:00 AM - 6:30 PM', 'entry_fee': 'Free', 'latitude': 15.5009, 'longitude': 73.9116, 'image': 'https://images.unsplash.com/photo-1581791538302-03537b9c97bf?w=600&auto=format'},
                    {'name': 'Fort Aguada', 'description': 'A well-preserved 17th-century Portuguese fort overlooking the Arabian Sea. The fort includes a lighthouse (the oldest in Asia) and offers stunning panoramic views.', 'category': 'historical', 'timing': '9:30 AM - 6:00 PM', 'entry_fee': 'Free', 'latitude': 15.4919, 'longitude': 73.7737, 'image': 'https://images.unsplash.com/photo-1587922546307-776227941871?w=600&auto=format'},
                    {'name': 'Dudhsagar Falls', 'description': 'One of India\'s tallest waterfalls (310m), located on the Mandovi River. The name means "Sea of Milk" due to the white frothy appearance of the cascading water through lush green forest.', 'category': 'nature', 'timing': '6:00 AM - 5:00 PM (Best: Monsoon season)', 'entry_fee': '₹400 (jeep ride)', 'latitude': 15.3144, 'longitude': 74.3143, 'image': 'https://images.unsplash.com/photo-1606298246186-08599e5de544?w=600&auto=format'},
                    {'name': 'Anjuna Flea Market', 'description': 'A vibrant Wednesday market where everything from handicrafts, clothing, and jewelry to souvenirs and spices is sold. A relic of Goa\'s hippie era with live music and performances.', 'category': 'cultural', 'timing': 'Every Wednesday: 8:00 AM - 6:00 PM', 'entry_fee': 'Free', 'latitude': 15.5735, 'longitude': 73.7414, 'image': 'https://images.unsplash.com/photo-1580060839134-75a5edca2e99?w=600&auto=format'},
                    {'name': 'Palolem Beach', 'description': 'A crescent-shaped beach in South Goa known for its natural beauty, calm waters, and colorful beach huts. Perfect for swimming, kayaking, and watching dolphins at sunset.', 'category': 'beach', 'timing': 'Open 24 hours', 'entry_fee': 'Free', 'latitude': 15.0100, 'longitude': 74.0230, 'image': 'https://images.unsplash.com/photo-1507525428034-b723cf961d3e?w=600&auto=format'},
                ],
                'foods': [
                    {'name': 'Fish Curry Rice', 'description': 'Goa\'s staple dish — fresh fish (usually kingfish or pomfret) cooked in a tangy coconut-based curry with kokum, served with steamed rice. Every Goan household has its own recipe.'},
                    {'name': 'Pork Vindaloo', 'description': 'A fiery Indo-Portuguese dish of pork marinated in vinegar, garlic, and red chilies. The name comes from "vinha d\'alhos" (wine and garlic). A Goan Christmas staple.'},
                    {'name': 'Bebinca', 'description': 'A traditional Goan layered pudding made with coconut milk, eggs, sugar, and ghee. Each of its 7-16 layers is baked individually, making it a labor of love.'},
                    {'name': 'Prawn Balchão', 'description': 'Spicy pickled prawns in a tangy red paste of dried chilies, vinegar, tomatoes, and spices. It can be stored for weeks and gets better with time.'},
                    {'name': 'Feni', 'description': 'Goa\'s signature spirit distilled from cashew apples or coconut palm sap. Usually enjoyed neat, with lime and soda, or in cocktails. It has a GI tag unique to Goa.'},
                ],
            },
            {
                'name': 'Varanasi',
                'state': 'Uttar Pradesh',
                'description': 'Varanasi (also known as Banaras or Kashi) is one of the oldest continuously inhabited cities in the world, dating back over 5,000 years. Situated on the banks of the sacred River Ganges, it is the spiritual capital of India and a major pilgrimage destination for Hindus. The city is famous for its ghats, temples, silk weaving, and rich musical tradition.',
                'best_time_to_visit': 'October to March — Pleasant weather with temperatures between 5-20°C. Dev Deepawali (usually November) is a spectacular festival when the ghats are lit with a million earthen lamps.',
                'image': 'https://images.unsplash.com/photo-1561361513-2d000a50f0dc?w=800&auto=format',
                'latitude': 25.3176,
                'longitude': 83.0068,
                'travel_tips': 'Wake up early for the sunrise boat ride on the Ganges — it is a life-changing experience.\nAttend the Ganga Aarti at Dashashwamedh Ghat every evening at 7 PM.\nNavigate the old city lanes on foot or by cycle rickshaw — autos can\'t enter the narrow lanes.\nBuy authentic Banarasi silk sarees directly from weavers in the Muslim quarter.\nRespect the local customs — Varanasi is deeply sacred to many faiths.\nDon\'t miss the ancient Sarnath, just 10 km from Varanasi.',
                'places': [
                    {'name': 'Dashashwamedh Ghat', 'description': 'The main ghat in Varanasi, famous for its spectacular Ganga Aarti ceremony held every evening. The name means "ghat of ten sacrificed horses" from a legend about Lord Brahma.', 'category': 'religious', 'timing': 'Open 24 hours (Aarti: 7:00 PM daily)', 'entry_fee': 'Free', 'latitude': 25.3046, 'longitude': 83.0107, 'image': 'https://images.unsplash.com/photo-1567157577867-05ccb1388e13?w=600&auto=format'},
                    {'name': 'Kashi Vishwanath Temple', 'description': 'One of the most famous Hindu temples, dedicated to Lord Shiva. The current structure was built in 1780 by Maharani Ahilyabai Holkar and has 800 kg of gold plating on its tower.', 'category': 'religious', 'timing': '3:00 AM - 11:00 PM', 'entry_fee': 'Free', 'latitude': 25.3109, 'longitude': 83.0107, 'image': 'https://images.unsplash.com/photo-1627894006066-b45e3a637834?w=600&auto=format'},
                    {'name': 'Sarnath', 'description': 'The sacred Buddhist site where Lord Buddha gave his first sermon after enlightenment. Features the famous Dhamek Stupa (128 feet tall), Ashoka Pillar, and an excellent archaeological museum.', 'category': 'religious', 'timing': '6:00 AM - 6:00 PM', 'entry_fee': '₹25 (Indians), ₹300 (Foreigners)', 'latitude': 25.3814, 'longitude': 83.0223, 'image': 'https://images.unsplash.com/photo-1591017403321-cf0e4cdd9644?w=600&auto=format'},
                    {'name': 'Manikarnika Ghat', 'description': 'One of the oldest and most sacred cremation ghats in the city. Hindus believe that being cremated here provides moksha (liberation from the cycle of rebirth). Fires here are said to have been burning for over 5,000 years.', 'category': 'religious', 'timing': 'Open 24 hours', 'entry_fee': 'Free (Photography not allowed)', 'latitude': 25.3118, 'longitude': 83.0143, 'image': 'https://images.unsplash.com/photo-1571536802807-30451e3955d8?w=600&auto=format'},
                    {'name': 'Ramnagar Fort', 'description': 'An 18th-century fort built with cream-colored sandstone, situated on the eastern bank of the Ganges. It houses a museum with vintage cars, royal costumes, ivory chess sets, and antique weaponry.', 'category': 'historical', 'timing': '10:00 AM - 5:00 PM', 'entry_fee': '₹25 (Indians), ₹75 (Foreigners)', 'latitude': 25.2856, 'longitude': 83.0300, 'image': 'https://images.unsplash.com/photo-1625472610751-c4a01cd42c2f?w=600&auto=format'},
                    {'name': 'Assi Ghat', 'description': 'The southernmost ghat of Varanasi, believed to be the spot where saint Tulsidas wrote the epic Ramcharitmanas. Popular with both pilgrims and travelers for morning yoga and meditation.', 'category': 'religious', 'timing': 'Open 24 hours', 'entry_fee': 'Free', 'latitude': 25.2877, 'longitude': 83.0043, 'image': 'https://images.unsplash.com/photo-1609948543911-7aee47c8a155?w=600&auto=format'},
                ],
                'foods': [
                    {'name': 'Kachori Sabzi', 'description': 'Varanasi\'s beloved breakfast — crispy fried kachori (pastry) filled with lentils, served with spicy potato curry and tangy chutney. Head to Kachori Gali for the best experience.'},
                    {'name': 'Banarasi Paan', 'description': 'The legendary betel leaf preparation from Varanasi, filled with gulkand (rose petal jam), coconut, and aromatic spices. A digestive and a cultural experience in one.'},
                    {'name': 'Thandai', 'description': 'A refreshing cold drink made from milk blended with a paste of almonds, fennel seeds, rose petals, pepper, cardamom, and saffron. Especially popular during Holi.'},
                    {'name': 'Malaiyo', 'description': 'A magical winter-only delicacy — light, frothy milk foam collected overnight in clay pots, flavored with saffron, cardamom, and pistachios. Available only from November to February.'},
                    {'name': 'Tamatar Chaat', 'description': 'Varanasi-style chaat made with tangy tomato sauce, crispy puris, potatoes, onions, and a blend of spices. A flavor explosion unique to Banaras.'},
                ],
            },
            {
                'name': 'Udaipur',
                'state': 'Rajasthan',
                'description': 'Known as the "City of Lakes" and the "Venice of the East," Udaipur is one of India\'s most romantic and picturesque cities. Nestled between the Aravalli Hills and sparkling lakes, Udaipur was founded in 1559 by Maharana Udai Singh II as the new capital of the Mewar Kingdom. Its stunning palaces, temples, and havelis reflect centuries of architectural grandeur.',
                'best_time_to_visit': 'September to March — The monsoon season (July-September) fills the lakes and makes the surroundings lush green. Winters are cool and perfect for sightseeing and boat rides.',
                'image': 'https://images.unsplash.com/photo-1602508453274-d193b6637c5c?w=800&auto=format',
                'latitude': 24.5854,
                'longitude': 73.7125,
                'travel_tips': 'Take a sunset boat ride on Lake Pichola — it\'s the most romantic experience in Udaipur.\nThe City Palace is massive — plan at least 2-3 hours for a thorough visit.\nWatch a cultural show at Bagore Ki Haveli every evening.\nVisit Sajjangarh (Monsoon Palace) for spectacular sunset city views.\nExplore the local art scene at Shilpgram Crafts Village.\nStay at a heritage hotel or haveli for the authentic Udaipur experience.',
                'places': [
                    {'name': 'City Palace', 'description': 'The largest palace complex in Rajasthan, built over 400 years by successive Mewar rulers. Perched on the banks of Lake Pichola, it blends Rajasthani, Mughal, Medieval, European, and Chinese architecture.', 'category': 'historical', 'timing': '9:30 AM - 5:30 PM', 'entry_fee': '₹300 (Indians), ₹700 (Foreigners)', 'latitude': 24.5764, 'longitude': 73.6826, 'image': 'https://images.unsplash.com/photo-1603204077167-2fa0397f27c2?w=600&auto=format'},
                    {'name': 'Lake Pichola', 'description': 'An artificial freshwater lake created in 1362, surrounded by palaces, temples, and hills. The famous Lake Palace (now a luxury hotel) and Jag Mandir sit on islands in the lake.', 'category': 'nature', 'timing': '9:00 AM - 6:00 PM (boat rides)', 'entry_fee': '₹400 (boat ride)', 'latitude': 24.5725, 'longitude': 73.6796, 'image': 'https://images.unsplash.com/photo-1586183189334-3be18791fb88?w=600&auto=format'},
                    {'name': 'Jag Mandir', 'description': 'A palace built on an island in Lake Pichola, featuring elegant gardens, marble elephants, and stunning Aravalli Hill views. It sheltered Mughal Prince Khurram (later Shah Jahan) during a rebellion.', 'category': 'historical', 'timing': '10:00 AM - 6:00 PM', 'entry_fee': '₹400 (including boat)', 'latitude': 24.5697, 'longitude': 73.6788, 'image': 'https://images.unsplash.com/photo-1623689048105-a17b1e1936b8?w=600&auto=format'},
                    {'name': 'Saheliyon Ki Bari', 'description': 'The "Garden of Maidens" — a beautiful ornamental garden designed for the queen and her 48 maidens. Features lotus pools, marble elephants, delicate fountains, and lush landscaping.', 'category': 'nature', 'timing': '9:00 AM - 6:00 PM', 'entry_fee': '₹20 (Indians), ₹100 (Foreigners)', 'latitude': 24.5939, 'longitude': 73.6887, 'image': 'https://images.unsplash.com/photo-1595431715579-46e6b4e04059?w=600&auto=format'},
                    {'name': 'Sajjangarh (Monsoon Palace)', 'description': 'A hilltop palace built in 1884 to watch monsoon clouds. Located 944m above sea level, it offers breathtaking panoramic views of the city, lakes, and surrounding Aravalli Hills, especially at sunset.', 'category': 'historical', 'timing': '9:00 AM - 6:00 PM', 'entry_fee': '₹80 (Indians), ₹300 (Foreigners)', 'latitude': 24.5479, 'longitude': 73.6505, 'image': 'https://images.unsplash.com/photo-1578662996442-48f60103fc96?w=600&auto=format'},
                    {'name': 'Jagdish Temple', 'description': 'A large Hindu temple built in 1651 in the Indo-Aryan style, dedicated to Lord Vishnu. Features intricate carvings, sculpted pillars, and a 79-foot high tower visible from all parts of the old city.', 'category': 'religious', 'timing': '4:15 AM - 1:00 PM, 5:15 PM - 8:00 PM', 'entry_fee': 'Free', 'latitude': 24.5770, 'longitude': 73.6836, 'image': 'https://images.unsplash.com/photo-1602508453274-d193b6637c5c?w=600&auto=format'},
                    {'name': 'Fateh Sagar Lake', 'description': 'A picturesque lake connected to Lake Pichola by a canal, surrounded by hills and Nehru Garden on an island. Popular for boating, lakeside walks, and the beautiful sunset views.', 'category': 'nature', 'timing': '8:00 AM - 6:00 PM', 'entry_fee': '₹30 (boat ride)', 'latitude': 24.5930, 'longitude': 73.6800, 'image': 'https://images.unsplash.com/photo-1586183189334-3be18791fb88?w=600&auto=format'},
                    {'name': 'Bagore Ki Haveli', 'description': 'An 18th-century haveli on the waterfront of Gangaur Ghat with over 100 rooms. Hosts daily Rajasthani cultural shows with folk dances (Ghoomar), puppet shows, and live music.', 'category': 'cultural', 'timing': '10:00 AM - 5:30 PM (Show: 7:00 PM)', 'entry_fee': '₹100 (Museum), ₹150 (Cultural Show)', 'latitude': 24.5777, 'longitude': 73.6815, 'image': 'https://images.unsplash.com/photo-1590689081018-80297e0e0222?w=600&auto=format'},
                ],
                'foods': [
                    {'name': 'Dal Baati Churma', 'description': 'Rajasthan\'s signature dish — baked wheat balls (baati) served with five-lentil dal and sweet churma. In Udaipur, try it at Ambrai Restaurant with a lake view.'},
                    {'name': 'Gatte Ki Sabzi', 'description': 'Gram flour dumplings cooked in a spicy yogurt-based gravy. A unique Rajasthani dish that showcases the creativity of desert cuisine where fresh vegetables were scarce.'},
                    {'name': 'Kachhi Dabeli', 'description': 'A sweet-spicy snack from the Gujarat-Rajasthan border — a bread bun stuffed with spiced potato filling, pomegranate seeds, peanuts, and chutneys. A beloved street food in Udaipur.'},
                    {'name': 'Mawa Kachori', 'description': 'A sweet deep-fried pastry stuffed with mawa (reduced milk), dry fruits, and flavored with cardamom. The Udaipur version is extra rich and served warm drizzled with sugar syrup.'},
                ],
            },
        ]

        for city_info in cities_data:
            places_data = city_info.pop('places')
            foods_data = city_info.pop('foods')

            city = City.objects.create(**city_info)
            self.stdout.write(f'  Created city: {city.name}')

            for place_info in places_data:
                Place.objects.create(city=city, **place_info)

            for food_info in foods_data:
                Food.objects.create(city=city, **food_info)

            self.stdout.write(f'    → {len(places_data)} places, {len(foods_data)} foods')

        self.stdout.write(self.style.SUCCESS(f'Successfully seeded {City.objects.count()} cities!'))
