import { Link } from 'react-router-dom';

const FEATURES = [
  { icon: '🤖', title: 'AI-Powered Itineraries', desc: 'Generate personalized day-by-day travel plans with our advanced AI. Choose your budget, interests, and duration — get a complete itinerary in seconds.' },
  { icon: '🏙️', title: 'Universal City Search', desc: 'Search any city in India — not just our curated picks. Our AI dynamically generates travel data for 100+ cities across the country.' },
  { icon: '📥', title: 'PDF Travel Guides', desc: 'Download beautifully formatted PDF itineraries with India-themed design. Share with travel companions or print for offline use.' },
  { icon: '💬', title: 'Smart Travel Chatbot', desc: 'Ask any travel question — best foods, safety tips, budget planning, or hidden gems. Our AI assistant knows India inside out.' },
  { icon: '🗺️', title: 'Rich Destination Data', desc: 'Detailed information on tourist places, famous foods, entry fees, timings, and local travel tips for every destination.' },
  { icon: '🌤️', title: 'Weather Intelligence', desc: 'Check current weather conditions and best times to visit any Indian city. Plan your trip around perfect weather windows.' },
];

const STATS = [
  { number: '100+', label: 'Indian Cities' },
  { number: '200+', label: 'Tourist Places' },
  { number: '150+', label: 'Famous Foods' },
  { number: 'AI', label: 'Smart Planner' },
];

const TEAM_VALUES = [
  { icon: '🎯', title: 'Mission', desc: 'To make travel planning for India effortless, enjoyable, and accessible to everyone — from first-time visitors to seasoned explorers.' },
  { icon: '🧠', title: 'AI-First Approach', desc: 'We leverage cutting-edge AI (Google Gemini) to generate personalized, context-aware travel recommendations that feel handcrafted.' },
  { icon: '🇮🇳', title: 'Celebrating India', desc: 'We showcase the incredible diversity of India — from 29 states and 7 union territories, each with unique culture, food, and landscapes.' },
];

export default function AboutPage() {
  return (
    <div className="about-page">
      {/* Hero */}
      <section className="about-hero">
        <div className="about-hero-overlay">
          <div className="about-hero-content">
            <div className="hero-badge">🇮🇳 About Us</div>
            <h1>Your AI-Powered<br /><span className="highlight">India Travel Companion</span></h1>
            <p>We combine local knowledge, rich data, and artificial intelligence to help you plan the perfect journey across incredible India.</p>
          </div>
        </div>
      </section>

      {/* Stats */}
      <section className="about-stats-section">
        <div className="about-stats">
          {STATS.map((s, i) => (
            <div key={i} className="about-stat">
              <div className="about-stat-number">{s.number}</div>
              <div className="about-stat-label">{s.label}</div>
            </div>
          ))}
        </div>
      </section>

      {/* Mission */}
      <section className="section">
        <div className="section-header">
          <div className="section-label">Who We Are</div>
          <h2 className="section-title">What Drives Us</h2>
        </div>

        <div className="about-values-grid">
          {TEAM_VALUES.map((v, i) => (
            <div key={i} className="about-value-card">
              <div className="about-value-icon">{v.icon}</div>
              <h3>{v.title}</h3>
              <p>{v.desc}</p>
            </div>
          ))}
        </div>
      </section>

      {/* Features */}
      <section className="section" style={{ background: 'var(--white)' }}>
        <div className="section-header">
          <div className="section-label">Platform Features</div>
          <h2 className="section-title">What We Offer</h2>
          <p className="section-subtitle">Powerful features designed to make your India trip unforgettable</p>
        </div>

        <div className="about-features-grid">
          {FEATURES.map((f, i) => (
            <div key={i} className="about-feature-card">
              <div className="about-feature-icon">{f.icon}</div>
              <h3>{f.title}</h3>
              <p>{f.desc}</p>
            </div>
          ))}
        </div>
      </section>

      {/* Tech Stack */}
      <section className="section">
        <div className="section-header">
          <div className="section-label">Built With</div>
          <h2 className="section-title">Technology Stack</h2>
        </div>

        <div className="about-tech-grid">
          {[
            { name: 'React', icon: '⚛️', desc: 'Modern UI framework' },
            { name: 'Django', icon: '🐍', desc: 'Robust REST backend' },
            { name: 'Google Gemini', icon: '✨', desc: 'AI-powered features' },
            { name: 'ReportLab', icon: '📄', desc: 'Professional PDFs' },
            { name: 'SQLite', icon: '🗄️', desc: 'Reliable data store' },
            { name: 'Vite', icon: '⚡', desc: 'Lightning-fast builds' },
          ].map((t, i) => (
            <div key={i} className="about-tech-card">
              <span className="about-tech-icon">{t.icon}</span>
              <strong>{t.name}</strong>
              <span className="about-tech-desc">{t.desc}</span>
            </div>
          ))}
        </div>
      </section>

      {/* CTA */}
      <section className="about-cta">
        <h2>Ready to Plan Your Indian Adventure?</h2>
        <p>Start exploring destinations or let our AI create your perfect itinerary</p>
        <div className="hero-buttons" style={{ justifyContent: 'center' }}>
          <Link to="/planner" className="btn btn-primary">✨ AI Trip Planner</Link>
          <Link to="/explore" className="btn btn-outline" style={{ color: 'white', borderColor: 'rgba(255,255,255,0.5)' }}>🧭 Explore Cities</Link>
        </div>
      </section>

      <footer className="footer">
        <p>© 2024 India Travel Planner — Built with ❤️ for India 🇮🇳</p>
      </footer>
    </div>
  );
}
