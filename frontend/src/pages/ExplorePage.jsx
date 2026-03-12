import { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import SearchBar from '../components/SearchBar';
import CityCard from '../components/CityCard';
import { getCities } from '../services/api';

const CATEGORIES = [
  {
    icon: '🏔️',
    title: 'Mountains & Hills',
    desc: 'Escape to serene hill stations and mighty peaks',
    color: '#2D7D46',
    cities: ['Shimla', 'Manali', 'Darjeeling', 'Mussoorie', 'Ooty', 'Munnar'],
    image: '/generated_images/category_mountains.png',
  },
  {
    icon: '🏖️',
    title: 'Beaches & Islands',
    desc: 'Sun-kissed shores and crystal waters await',
    color: '#0891B2',
    cities: ['Goa', 'Pondicherry', 'Port Blair', 'Lakshadweep', 'Kovalam'],
    image: '/generated_images/category_beaches.png',
  },
  {
    icon: '🕌',
    title: 'Spiritual & Sacred',
    desc: 'Find peace at ancient temples and holy cities',
    color: '#DC2626',
    cities: ['Varanasi', 'Rishikesh', 'Amritsar', 'Bodh Gaya', 'Tirupati', 'Haridwar'],
    image: '/generated_images/category_spiritual.png',
  },
  {
    icon: '🏰',
    title: 'Heritage & Forts',
    desc: 'Walk through India\'s glorious royal history',
    color: '#B45309',
    cities: ['Jaipur', 'Jodhpur', 'Jaisalmer', 'Udaipur', 'Agra', 'Hampi'],
    image: '/generated_images/category_heritage.png',
  },
  {
    icon: '🍛',
    title: 'Food Destinations',
    desc: 'Taste the incredible flavors of India',
    color: '#E85D04',
    cities: ['Delhi', 'Lucknow', 'Hyderabad', 'Mumbai', 'Kolkata', 'Indore'],
    image: '/generated_images/category_food.png',
  },
  {
    icon: '🌿',
    title: 'Nature & Wildlife',
    desc: 'Explore lush forests and rare wildlife',
    color: '#15803D',
    cities: ['Kaziranga', 'Jim Corbett', 'Coorg', 'Wayanad', 'Sundarbans', 'Ranthambore'],
    image: '/generated_images/category_nature.png',
  },
];

export default function ExplorePage() {
  const navigate = useNavigate();
  const [cities, setCities] = useState([]);
  const [activeCategory, setActiveCategory] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    getCities().then(setCities).catch(() => {}).finally(() => setLoading(false));
  }, []);

  const handleCityClick = (cityName) => {
    // Search for the city in DB results
    const dbCity = cities.find(c => c.name.toLowerCase() === cityName.toLowerCase());
    if (dbCity) {
      navigate(`/city/${dbCity.id}`);
    } else {
      navigate(`/city/dynamic_${cityName.toLowerCase().replace(/\s+/g, '_')}`);
    }
  };

  return (
    <div className="explore-page">
      {/* Hero Banner */}
      <section className="explore-hero">
        <div className="explore-hero-overlay">
          <div className="explore-hero-content">
            <div className="hero-badge">🧭 Discover Destinations</div>
            <h1>Explore <span className="highlight">Incredible India</span></h1>
            <p>From snow-capped Himalayas to tropical beaches, ancient temples to modern cities — find your perfect destination</p>
            <div style={{ maxWidth: '500px', margin: '1.5rem auto 0' }}>
              <SearchBar variant="hero" />
            </div>
          </div>
        </div>
      </section>

      {/* Categories */}
      <section className="section" id="categories">
        <div className="section-header">
          <div className="section-label">Travel Categories</div>
          <h2 className="section-title">How Do You Want to Travel?</h2>
          <p className="section-subtitle">Choose your travel style and discover the perfect Indian destinations</p>
        </div>

        <div className="explore-categories">
          {CATEGORIES.map((cat, i) => (
            <div
              key={i}
              className={`explore-category-card ${activeCategory === i ? 'active' : ''}`}
              onClick={() => setActiveCategory(activeCategory === i ? null : i)}
              style={{ '--cat-color': cat.color }}
            >
              <div className="explore-cat-image">
                <img src={cat.image} alt={cat.title} loading="lazy" />
                <div className="explore-cat-image-overlay">
                  <span className="explore-cat-icon">{cat.icon}</span>
                </div>
              </div>
              <div className="explore-cat-body">
                <h3 className="explore-cat-title">{cat.title}</h3>
                <p className="explore-cat-desc">{cat.desc}</p>

                {activeCategory === i && (
                  <div className="explore-cat-cities">
                    {cat.cities.map((city, j) => (
                      <button
                        key={j}
                        className="explore-city-chip"
                        onClick={(e) => {
                          e.stopPropagation();
                          handleCityClick(city);
                        }}
                      >
                        {city} →
                      </button>
                    ))}
                  </div>
                )}
              </div>
            </div>
          ))}
        </div>
      </section>

      {/* All Cities */}
      <section className="section" style={{ background: 'var(--white)' }}>
        <div className="section-header">
          <div className="section-label">Popular Destinations</div>
          <h2 className="section-title">Featured Cities</h2>
          <p className="section-subtitle">Cities with detailed data, curated places, and food recommendations</p>
        </div>

        {loading ? (
          <div className="loading">
            <div className="spinner"></div>
            <span className="loading-text">Loading destinations...</span>
          </div>
        ) : (
          <div className="cities-grid">
            {cities.map(city => (
              <CityCard key={city.id} city={city} />
            ))}
          </div>
        )}
      </section>

      <footer className="footer">
        <p>© 2024 India Travel Planner — Explore the beauty of India 🇮🇳</p>
      </footer>
    </div>
  );
}
