import { useNavigate } from 'react-router-dom';

export default function ItineraryPage() {
  const navigate = useNavigate();

  return (
    <div className="planner-page">
      <div className="planner-container" style={{ textAlign: 'center', paddingTop: '4rem' }}>
        <div style={{ fontSize: '4rem', marginBottom: '1rem' }}>🗺️</div>
        <h1 className="section-title">Your Travel Itineraries</h1>
        <p className="section-subtitle" style={{ marginBottom: '2rem' }}>
          Generate personalized AI itineraries for any Indian city
        </p>
        <button
          className="btn btn-primary"
          onClick={() => navigate('/planner')}
          style={{ fontSize: '1.05rem' }}
        >
          ✨ Create New Itinerary
        </button>

        <div style={{
          marginTop: '3rem',
          padding: '2rem',
          background: 'var(--white)',
          borderRadius: 'var(--radius-lg)',
          boxShadow: 'var(--shadow)',
        }}>
          <h3 style={{
            fontFamily: 'var(--font-heading)',
            color: 'var(--deep-blue)',
            marginBottom: '1rem',
          }}>How It Works</h3>
          <div style={{
            display: 'grid',
            gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))',
            gap: '1.5rem',
            textAlign: 'center',
          }}>
            {[
              { step: '1', icon: '🏙️', title: 'Choose a City', desc: 'Select from India\'s most amazing destinations' },
              { step: '2', icon: '⚙️', title: 'Set Preferences', desc: 'Pick your days, budget, and interests' },
              { step: '3', icon: '🤖', title: 'AI Generates', desc: 'Get a smart, personalized itinerary' },
              { step: '4', icon: '📥', title: 'Download PDF', desc: 'Save your professional travel guide' },
            ].map((s, i) => (
              <div key={i}>
                <div style={{
                  width: '50px',
                  height: '50px',
                  borderRadius: '50%',
                  background: 'var(--cream)',
                  display: 'flex',
                  alignItems: 'center',
                  justifyContent: 'center',
                  fontSize: '1.5rem',
                  margin: '0 auto 0.5rem',
                }}>{s.icon}</div>
                <h4 style={{
                  fontFamily: 'var(--font-heading)',
                  color: 'var(--deep-blue)',
                  fontSize: '0.95rem',
                  marginBottom: '0.3rem',
                }}>{s.title}</h4>
                <p style={{ fontSize: '0.8rem', color: 'var(--gray-500)' }}>{s.desc}</p>
              </div>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
}
