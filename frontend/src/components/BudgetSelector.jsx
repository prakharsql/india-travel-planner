export default function BudgetSelector({ value, onChange }) {
  const options = [
    { key: 'low', icon: '🎒', name: 'Budget', range: '₹1,000 – ₹2,500/day' },
    { key: 'medium', icon: '🏨', name: 'Comfort', range: '₹2,500 – ₹6,000/day' },
    { key: 'luxury', icon: '👑', name: 'Luxury', range: '₹8,000+/day' },
  ];

  return (
    <div className="budget-options">
      {options.map((opt) => (
        <div
          key={opt.key}
          className={`budget-option ${value === opt.key ? 'active' : ''}`}
          onClick={() => onChange(opt.key)}
          id={`budget-${opt.key}`}
        >
          <div className="budget-option-icon">{opt.icon}</div>
          <div className="budget-option-name">{opt.name}</div>
          <div className="budget-option-range">{opt.range}</div>
        </div>
      ))}
    </div>
  );
}
