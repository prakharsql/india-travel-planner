import { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import ItineraryForm from '../components/ItineraryForm';
import { getCities, generateItinerary, downloadPDF } from '../services/api';

export default function AIPlanner() {
  const { cityId: paramCityId } = useParams();
  const [cities, setCities] = useState([]);
  const [selectedCityId, setSelectedCityId] = useState(paramCityId || '');
  const [numDays, setNumDays] = useState(3);
  const [budget, setBudget] = useState('medium');
  const [interests, setInterests] = useState([]);
  const [itinerary, setItinerary] = useState(null);
  const [loading, setLoading] = useState(false);
  const [downloading, setDownloading] = useState(false);
  const [error, setError] = useState('');

  useEffect(() => {
    getCities().then(setCities).catch(() => {});
  }, []);

  useEffect(() => {
    if (paramCityId) setSelectedCityId(paramCityId);
  }, [paramCityId]);

  const handleGenerate = async () => {
    if (!selectedCityId) return;
    setLoading(true);
    setItinerary(null);
    setError('');

    try {
      const data = await generateItinerary(selectedCityId, numDays, budget, interests);
      setItinerary(data);
    } catch (err) {
      setError('Failed to generate itinerary. Please try again.');
    } finally {
      setLoading(false);
    }
  };

  const handleDownloadPDF = async () => {
    if (!itinerary || !selectedCityId) return;
    setDownloading(true);
    try {
      await downloadPDF(selectedCityId, itinerary);
    } catch {
      alert('Failed to download PDF. Please try again.');
    } finally {
      setDownloading(false);
    }
  };

  const selectedCity = cities.find(c => String(c.id) === String(selectedCityId));

  return (
    <div className="planner-page">
      <div className="planner-container">
        {/* Header */}
        <div className="planner-header">
          <div className="section-label">AI-Powered</div>
          <h1 className="section-title">Trip Planner</h1>
          <p className="section-subtitle">
            Select your destination, set your preferences, and let AI craft the perfect itinerary
          </p>
        </div>

        {/* Form */}
        <ItineraryForm
          cities={cities}
          selectedCityId={selectedCityId}
          onCityChange={setSelectedCityId}
          numDays={numDays}
          onDaysChange={setNumDays}
          budget={budget}
          onBudgetChange={setBudget}
          interests={interests}
          onInterestsChange={setInterests}
          onSubmit={handleGenerate}
          loading={loading}
        />

        {/* Error */}
        {error && (
          <div style={{
            background: 'rgba(239, 68, 68, 0.08)',
            border: '1px solid rgba(239, 68, 68, 0.2)',
            borderRadius: 'var(--radius)',
            padding: '1rem 1.5rem',
            color: 'var(--red)',
            marginBottom: '1.5rem',
            textAlign: 'center',
            fontWeight: 500,
          }}>
            ⚠️ {error}
          </div>
        )}

        {/* Results */}
        {itinerary && (
          <div className="itinerary-result" id="itinerary-result">
            {/* Header */}
            <div className="itinerary-header">
              <div>
                <h2 className="itinerary-title">
                  🗺️ {itinerary.city || selectedCity?.name} — {itinerary.num_days} Day Itinerary
                </h2>
              </div>
              <div style={{ display: 'flex', gap: '0.8rem', flexWrap: 'wrap' }}>
                <button
                  className="btn btn-gold"
                  onClick={handleDownloadPDF}
                  disabled={downloading}
                  id="download-pdf-btn"
                >
                  {downloading ? '⏳ Downloading...' : '📥 Download PDF'}
                </button>
              </div>
            </div>

            {/* Budget */}
            <div className="itinerary-budget" style={{ marginBottom: '1.5rem' }}>
              <div className="itinerary-budget-item">
                <div className="itinerary-budget-label">Budget Type</div>
                <div className="itinerary-budget-value">{(itinerary.budget_type || budget).toUpperCase()}</div>
              </div>
              <div className="itinerary-budget-item">
                <div className="itinerary-budget-label">Daily Estimate</div>
                <div className="itinerary-budget-value">
                  {itinerary.currency || '₹'} {(itinerary.estimated_daily_budget || 0).toLocaleString()}
                </div>
              </div>
              <div className="itinerary-budget-item">
                <div className="itinerary-budget-label">Total Estimate</div>
                <div className="itinerary-budget-value">
                  {itinerary.currency || '₹'} {(itinerary.estimated_total_budget || 0).toLocaleString()}
                </div>
              </div>
            </div>

            {/* Days */}
            {itinerary.days?.map((day) => (
              <div key={day.day} className="day-card">
                <div className="day-card-header">
                  📅 Day {day.day}
                </div>
                <div className="day-card-body">
                  {day.activities?.length > 0 ? (
                    day.activities.map((act, i) => (
                      <div key={i} className="activity-item">
                        <div className="activity-time">{act.time}</div>
                        <div className="activity-content">
                          <div className="activity-name">{act.activity}</div>
                          {act.description && (
                            <div className="activity-desc">{act.description}</div>
                          )}
                          {act.type && (
                            <span className="activity-type">{act.type}</span>
                          )}
                        </div>
                      </div>
                    ))
                  ) : (
                    <p style={{ color: 'var(--gray-500)', fontSize: '0.9rem', padding: '0.5rem 0' }}>
                      Free day — explore at your own pace!
                    </p>
                  )}
                </div>
              </div>
            ))}
          </div>
        )}
      </div>
    </div>
  );
}
