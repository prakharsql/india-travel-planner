import { useState, useEffect, useRef } from 'react';
import { useNavigate } from 'react-router-dom';
import { getCities } from '../services/api';

export default function SearchBar({ variant = 'hero' }) {
  const [query, setQuery] = useState('');
  const [results, setResults] = useState([]);
  const [showResults, setShowResults] = useState(false);
  const navigate = useNavigate();
  const ref = useRef(null);

  useEffect(() => {
    if (query.trim().length < 1) {
      setResults([]);
      setShowResults(false);
      return;
    }

    const timer = setTimeout(async () => {
      try {
        const data = await getCities(query);
        setResults(data);
        setShowResults(true);
      } catch {
        setResults([]);
      }
    }, 200);

    return () => clearTimeout(timer);
  }, [query]);

  useEffect(() => {
    const onClick = (e) => {
      if (ref.current && !ref.current.contains(e.target)) {
        setShowResults(false);
      }
    };
    document.addEventListener('mousedown', onClick);
    return () => document.removeEventListener('mousedown', onClick);
  }, []);

  const handleSelect = (city) => {
    setQuery('');
    setShowResults(false);
    navigate(`/city/${city.id}`);
  };

  const isPage = variant === 'page';

  return (
    <div className="search-container" ref={ref}>
      <span className="search-icon">🔍</span>
      <input
        type="text"
        className={`search-bar ${isPage ? 'search-bar-page' : ''}`}
        placeholder="Search any Indian city... (Delhi, Indore, Shimla...)"
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        onFocus={() => results.length > 0 && setShowResults(true)}
        id="city-search"
      />
      {showResults && results.length > 0 && (
        <div className="search-results">
          {results.map((city, i) => (
            <div
              key={city.id || i}
              className="search-result-item"
              onClick={() => handleSelect(city)}
            >
              {city.image && (
                <img src={city.image} alt={city.name} />
              )}
              <div>
                <div className="search-result-name">
                  {city.name}
                  {city.is_dynamic && <span style={{ fontSize: '0.7rem', color: 'var(--saffron)', marginLeft: '6px' }}>✨ AI</span>}
                </div>
                <div className="search-result-state">{city.state}</div>
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}
