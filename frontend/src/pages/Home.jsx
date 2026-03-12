import { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import SearchBar from '../components/SearchBar';
import CityCard from '../components/CityCard';
import { getCities } from '../services/api';

export default function Home() {
  const [cities, setCities] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    getCities()
      .then(setCities)
      .catch(() => {})
      .finally(() => setLoading(false));
  }, []);

  return (
    <main>
      {/* ── Hero Section ── */}
      <section className="hero" id="hero">
        <div className="hero-content">
          <div className="hero-badge">
            ✨ AI-Powered Travel Planning
          </div>
          <h1>
            Discover & Plan Your<br />
            Journey Across <span className="highlight">India</span>
          </h1>
          <p>
            From ancient temples to sun-kissed beaches, royal palaces to snow-capped peaks.
            Let our AI create your personalized itinerary for the adventure of a lifetime.
          </p>

          <SearchBar variant="hero" />

          <div className="hero-buttons" style={{ marginTop: '1.5rem' }}>
            <Link to="/planner" className="btn btn-primary">
              ✨ Plan My Trip
            </Link>
            <Link to="/explore" className="btn btn-secondary">
              🧭 Explore Cities
            </Link>
          </div>

          <div className="hero-stats">
            <div className="hero-stat">
              <div className="hero-stat-number">100+</div>
              <div className="hero-stat-label">Cities</div>
            </div>
            <div className="hero-stat">
              <div className="hero-stat-number">200+</div>
              <div className="hero-stat-label">Tourist Places</div>
            </div>
            <div className="hero-stat">
              <div className="hero-stat-number">150+</div>
              <div className="hero-stat-label">Famous Foods</div>
            </div>
            <div className="hero-stat">
              <div className="hero-stat-number">AI</div>
              <div className="hero-stat-label">Smart Planner</div>
            </div>
          </div>
        </div>
      </section>

      {/* ── Featured Cities ── */}
      <section className="section" id="destinations">
        <div className="section-header">
          <div className="section-label">Discover India</div>
          <h2 className="section-title">Featured Destinations</h2>
          <p className="section-subtitle">
            Explore India's most enchanting cities, each with its own unique charm and character
          </p>
        </div>

        {loading ? (
          <div className="loading">
            <div className="spinner"></div>
            <span className="loading-text">Loading destinations...</span>
          </div>
        ) : (
          <div className="cities-grid">
            {cities.map((city) => (
              <CityCard key={city.id} city={city} />
            ))}
          </div>
        )}
      </section>

      {/* ── Features Section ── */}
      <section className="section" style={{ background: 'var(--white)' }}>
        <div className="section-header">
          <div className="section-label">Why Choose Us</div>
          <h2 className="section-title">Your Smart Travel Companion</h2>
          <p className="section-subtitle">
            We combine local knowledge with AI to craft the perfect Indian travel experience
          </p>
        </div>

        <div className="cities-grid" style={{ maxWidth: '900px' }}>
          {[
            { icon: '🤖', title: 'AI-Powered Itineraries', desc: 'Get personalized day-by-day plans based on your interests, budget, and duration for 100+ Indian cities.' },
            { icon: '📥', title: 'PDF Travel Guides', desc: 'Download professional India-themed PDF itineraries with all details you need.' },
            { icon: '💬', title: 'Smart Travel Chatbot', desc: 'Ask any travel question and get instant, context-aware answers about India.' },
            { icon: '🗺️', title: 'Universal City Search', desc: 'Search any city in India — AI generates travel data even for cities not in our database.' },
          ].map((f, i) => (
            <div key={i} style={{
              background: 'var(--cream)',
              borderRadius: 'var(--radius-lg)',
              padding: '1.8rem',
              textAlign: 'center',
              transition: 'all 0.3s ease',
              border: '1px solid rgba(212, 168, 67, 0.12)',
            }}>
              <div style={{ fontSize: '2.5rem', marginBottom: '0.6rem' }}>{f.icon}</div>
              <h3 style={{
                fontFamily: 'var(--font-heading)',
                fontSize: '1.1rem',
                fontWeight: 700,
                color: 'var(--deep-blue)',
                marginBottom: '0.4rem',
              }}>{f.title}</h3>
              <p style={{ fontSize: '0.85rem', color: 'var(--gray-600)', lineHeight: '1.55' }}>{f.desc}</p>
            </div>
          ))}
        </div>
      </section>

      {/* ── CTA ── */}
      <section style={{
        background: 'linear-gradient(135deg, var(--deep-blue) 0%, var(--deep-blue-light) 100%)',
        padding: '4rem 2rem',
        textAlign: 'center',
        color: 'var(--white)',
      }}>
        <h2 style={{
          fontFamily: 'var(--font-heading)',
          fontSize: '2rem',
          fontWeight: 800,
          marginBottom: '0.5rem',
        }}>Ready to Explore India?</h2>
        <p style={{ fontSize: '1rem', opacity: 0.85, marginBottom: '1.5rem', fontWeight: 300 }}>
          Search any city, discover hidden gems, and plan your perfect trip
        </p>
        <div className="hero-buttons" style={{ justifyContent: 'center' }}>
          <Link to="/explore" className="btn btn-primary">🧭 Explore Destinations</Link>
          <Link to="/about" className="btn btn-outline" style={{ color: 'white', borderColor: 'rgba(255,255,255,0.4)' }}>Learn More</Link>
        </div>
      </section>

      {/* ── Footer ── */}
      <footer className="footer">
        <p>© 2024 India Travel Planner — Plan Your Perfect Trip Across India 🇮🇳</p>
      </footer>
    </main>
  );
}
