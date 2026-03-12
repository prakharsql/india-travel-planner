import { useState } from 'react';
import { Link } from 'react-router-dom';

export default function CityCard({ city }) {
  const [imgLoaded, setImgLoaded] = useState(false);
  const [imgError, setImgError] = useState(false);

  const hasImage = city.image && city.image !== 'null' && city.image !== '';

  return (
    <Link to={`/city/${city.id}`} className="city-card" id={`city-card-${city.id}`}>
      <div className="city-card-image">
        {/* Skeleton loader while image loads */}
        {!imgLoaded && (
          <div className="image-skeleton">
            <div className="skeleton-shimmer"></div>
          </div>
        )}

        {hasImage ? (
          <img
            src={city.image}
            alt={`AI generated travel photograph of ${city.name}, India`}
            loading="lazy"
            onLoad={() => setImgLoaded(true)}
            onError={() => {
              setImgError(true);
              setImgLoaded(true);
            }}
            style={{
              opacity: imgLoaded ? 1 : 0,
              transition: 'opacity 0.6s ease',
            }}
          />
        ) : (
          <div className="city-card-fallback" style={{ opacity: 1 }}>
            <span className="city-card-fallback-emoji">🏛️</span>
          </div>
        )}

        <div className="city-card-overlay">
          <h3 className="city-card-name">{city.name}</h3>
          <span className="city-card-state">{city.state}</span>
        </div>
      </div>

      <div className="city-card-body">
        <p className="city-card-desc">{city.description}</p>
        <div className="city-card-footer">
          <span className="city-card-time">🕐 {city.best_time_to_visit || 'Oct–Mar'}</span>
          <span className="city-card-explore">Explore →</span>
        </div>
      </div>
    </Link>
  );
}
