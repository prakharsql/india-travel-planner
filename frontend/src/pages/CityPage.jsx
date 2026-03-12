import { useState, useEffect } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import PlaceCard from '../components/PlaceCard';
import FoodCard from '../components/FoodCard';
import { getCityDetail, getWeather } from '../services/api';

export default function CityPage() {
  const { id } = useParams();
  const navigate = useNavigate();
  const [city, setCity] = useState(null);
  const [weather, setWeather] = useState(null);
  const [loading, setLoading] = useState(true);
  const [bannerLoaded, setBannerLoaded] = useState(false);

  useEffect(() => {
    setLoading(true);
    setBannerLoaded(false);
    getCityDetail(id)
      .then((data) => {
        setCity(data);
        return getWeather(data.name);
      })
      .then(setWeather)
      .catch(() => {})
      .finally(() => setLoading(false));
  }, [id]);

  if (loading) {
    return (
      <div className="loading" style={{ minHeight: '100vh', paddingTop: '100px' }}>
        <div className="spinner"></div>
        <span className="loading-text">Loading city details...</span>
      </div>
    );
  }

  if (!city) {
    return (
      <div className="empty-state" style={{ minHeight: '100vh', paddingTop: '100px' }}>
        <div className="empty-state-icon">😕</div>
        <p>City not found</p>
      </div>
    );
  }

  const tips = city.travel_tips ? city.travel_tips.split('\n').filter(t => t.trim()) : [];
  const hasImage = city.image && city.image !== 'null' && city.image !== '';

  return (
    <main>
      {/* ── Banner ── */}
      <div className="city-banner">
        {/* Skeleton while loading */}
        {!bannerLoaded && (
          <div className="image-skeleton">
            <div className="skeleton-shimmer"></div>
          </div>
        )}
        {hasImage && (
          <img
            src={city.image}
            alt={`AI generated travel photograph of ${city.name}, India`}
            onLoad={() => setBannerLoaded(true)}
            onError={() => setBannerLoaded(true)}
            style={{
              opacity: bannerLoaded ? 1 : 0,
              transition: 'opacity 0.6s ease',
            }}
          />
        )}
        <div className="city-banner-overlay">
          <div className="city-banner-state">{city.state}, India</div>
          <h1 className="city-banner-name">{city.name}</h1>
        </div>
      </div>

      {/* ── Content ── */}
      <div className="city-content">
        {/* Overview */}
        <div className="city-overview">
          <div>
            <p className="city-description">{city.description}</p>
          </div>
          <div>
            <div className="city-info-box">
              <div className="city-info-title">Quick Info</div>
              <div className="city-info-item">
                <span className="city-info-icon">📅</span>
                <div><strong>Best Time:</strong> {city.best_time_to_visit}</div>
              </div>
              {weather && (
                <>
                  <div className="city-info-item">
                    <span className="city-info-icon">🌡️</span>
                    <div><strong>Temperature:</strong> {weather.temperature}°C (Feels like {weather.feels_like}°C)</div>
                  </div>
                  <div className="city-info-item">
                    <span className="city-info-icon">💧</span>
                    <div><strong>Humidity:</strong> {weather.humidity}%</div>
                  </div>
                  <div className="city-info-item">
                    <span className="city-info-icon">☁️</span>
                    <div><strong>Weather:</strong> {weather.description}</div>
                  </div>
                  {weather.best_months && (
                    <div className="city-info-item">
                      <span className="city-info-icon">🗓️</span>
                      <div><strong>Best Months:</strong> {weather.best_months}</div>
                    </div>
                  )}
                </>
              )}
              <div className="city-info-item">
                <span className="city-info-icon">📍</span>
                <div><strong>Places:</strong> {city.places?.length || 0} attractions</div>
              </div>
            </div>
          </div>
        </div>

        {/* AI Planner Button */}
        <div style={{ textAlign: 'center', margin: '2rem 0' }}>
          <button
            className="btn btn-primary"
            onClick={() => navigate(`/planner/${city.id}`)}
            id="generate-ai-itinerary"
            style={{ fontSize: '1.05rem', padding: '14px 32px' }}
          >
            ✨ Generate AI Itinerary for {city.name}
          </button>
        </div>

        {/* Places */}
        {city.places && city.places.length > 0 && (
          <section style={{ marginBottom: '3rem' }}>
            <div className="section-header" style={{ textAlign: 'left' }}>
              <div className="section-label">Must Visit</div>
              <h2 className="section-title" style={{ fontSize: '1.8rem' }}>Famous Tourist Places</h2>
            </div>
            <div className="places-grid">
              {city.places.map((place) => (
                <PlaceCard key={place.id} place={place} />
              ))}
            </div>
          </section>
        )}

        {/* Foods */}
        {city.foods && city.foods.length > 0 && (
          <section style={{ marginBottom: '3rem' }}>
            <div className="section-header" style={{ textAlign: 'left' }}>
              <div className="section-label">Must Try</div>
              <h2 className="section-title" style={{ fontSize: '1.8rem' }}>Famous Foods</h2>
            </div>
            <div className="foods-grid">
              {city.foods.map((food) => (
                <FoodCard key={food.id} food={food} />
              ))}
            </div>
          </section>
        )}

        {/* Map */}
        <section style={{ marginBottom: '3rem' }}>
          <div className="section-header" style={{ textAlign: 'left' }}>
            <div className="section-label">Location</div>
            <h2 className="section-title" style={{ fontSize: '1.8rem' }}>Explore on Map</h2>
          </div>
          <div className="map-container">
            {city.latitude && city.longitude ? (
              <iframe
                title={`${city.name} Map`}
                width="100%"
                height="100%"
                style={{ border: 0 }}
                loading="lazy"
                referrerPolicy="no-referrer-when-downgrade"
                src={`https://www.google.com/maps/embed/v1/place?key=${import.meta.env.VITE_GOOGLE_MAPS_KEY || ''}&q=${encodeURIComponent(city.name + ', India')}&center=${city.latitude},${city.longitude}&zoom=12`}
                allowFullScreen
              />
            ) : (
              <div className="map-placeholder">
                <div className="map-placeholder-icon">🗺️</div>
                <p>Map requires Google Maps API key</p>
                <p style={{ fontSize: '0.8rem', marginTop: '4px' }}>
                  Set <code>VITE_GOOGLE_MAPS_KEY</code> in <code>frontend/.env</code>
                </p>
              </div>
            )}
          </div>
        </section>

        {/* Travel Tips */}
        {tips.length > 0 && (
          <div className="travel-tips">
            <h3 className="travel-tips-title">💡 Travel Tips</h3>
            {tips.map((tip, i) => (
              <div key={i} className="travel-tip">
                <span className="travel-tip-icon">✓</span>
                <span>{tip}</span>
              </div>
            ))}
          </div>
        )}
      </div>

      <footer className="footer">
        <p>© 2024 India Travel Planner 🇮🇳</p>
      </footer>
    </main>
  );
}
