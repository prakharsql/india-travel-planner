import BudgetSelector from './BudgetSelector';

const INTERESTS = ['Historical', 'Food', 'Nature', 'Adventure', 'Cultural', 'Religious'];

export default function ItineraryForm({
  cities,
  selectedCityId,
  onCityChange,
  numDays,
  onDaysChange,
  budget,
  onBudgetChange,
  interests,
  onInterestsChange,
  onSubmit,
  loading,
}) {

  const toggleInterest = (interest) => {
    if (interests.includes(interest)) {
      onInterestsChange(interests.filter(i => i !== interest));
    } else {
      onInterestsChange([...interests, interest]);
    }
  };

  return (
    <div className="planner-form-card">
      <div className="form-group">
        <label className="form-label">Select City</label>
        <select
          className="form-select"
          value={selectedCityId}
          onChange={(e) => onCityChange(e.target.value)}
          id="city-select"
        >
          <option value="">Choose a destination...</option>
          {cities.map((c) => (
            <option key={c.id} value={c.id}>{c.name}, {c.state}</option>
          ))}
        </select>
      </div>

      <div className="form-row">
        <div className="form-group">
          <label className="form-label">Number of Days</label>
          <select
            className="form-select"
            value={numDays}
            onChange={(e) => onDaysChange(Number(e.target.value))}
            id="days-select"
          >
            {[1, 2, 3, 4, 5, 6, 7].map(d => (
              <option key={d} value={d}>{d} {d === 1 ? 'Day' : 'Days'}</option>
            ))}
          </select>
        </div>
      </div>

      <div className="form-group">
        <label className="form-label">Budget Level</label>
        <BudgetSelector value={budget} onChange={onBudgetChange} />
      </div>

      <div className="form-group">
        <label className="form-label">Travel Interests</label>
        <div className="interest-tags">
          {INTERESTS.map((interest) => (
            <button
              key={interest}
              className={`interest-tag ${interests.includes(interest.toLowerCase()) ? 'active' : ''}`}
              onClick={() => toggleInterest(interest.toLowerCase())}
              type="button"
              id={`interest-${interest.toLowerCase()}`}
            >
              {interest}
            </button>
          ))}
        </div>
      </div>

      <button
        className="btn btn-primary"
        onClick={onSubmit}
        disabled={!selectedCityId || loading}
        style={{ width: '100%', justifyContent: 'center', marginTop: '0.5rem' }}
        id="generate-btn"
      >
        {loading ? (
          <>
            <span className="spinner" style={{ width: 20, height: 20, borderWidth: 2 }}></span>
            Generating Itinerary...
          </>
        ) : (
          <>✨ Generate AI Itinerary</>
        )}
      </button>
    </div>
  );
}
