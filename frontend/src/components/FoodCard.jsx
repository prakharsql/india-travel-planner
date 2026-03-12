export default function FoodCard({ food }) {
  return (
    <div className="food-card" id={`food-${food.id}`}>
      <h4 className="food-card-name">🍽️ {food.name}</h4>
      <p className="food-card-desc">{food.description}</p>
    </div>
  );
}
