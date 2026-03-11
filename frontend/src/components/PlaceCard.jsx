import { useState } from 'react';

export default function PlaceCard({ place }) {
  const [imgLoaded, setImgLoaded] = useState(false);

  return (
    <div className="place-card" id={`place-${place.id}`}>
      <div className="place-card-image">
        {!imgLoaded && (
          <div className="image-skeleton">
            <div className="skeleton-shimmer"></div>
          </div>
        )}
        {place.image && (
          <img
            src={place.image}
            alt={`AI generated view of ${place.name}`}
            loading="lazy"
            onLoad={() => setImgLoaded(true)}
            style={{ opacity: imgLoaded ? 1 : 0, transition: 'opacity 0.6s ease' }}
          />
        )}
      </div>
      <div className="place-card-body">
        <span className="place-card-category">{place.category}</span>
        <h3 className="place-card-name">{place.name}</h3>
        <p className="place-card-desc">{place.description}</p>
        <div className="place-card-meta">
          {place.timing && <span>🕐 {place.timing}</span>}
          {place.entry_fee && <span>🎫 {place.entry_fee}</span>}
        </div>
      </div>
    </div>
  );
}
