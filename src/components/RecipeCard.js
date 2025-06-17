import React from 'react';

const formatTime = (minutes) => {
  if (minutes < 60) return `${minutes} mins`;
  const hours = Math.floor(minutes / 60);
  const remainingMinutes = minutes % 60;
  return remainingMinutes > 0 
    ? `${hours} hr ${remainingMinutes} mins`
    : `${hours} hr`;
};

const getDifficultyClass = (difficulty) => {
  const classes = {
    easy: 'bg-success',
    medium: 'bg-warning',
    hard: 'bg-danger'
  };
  return classes[difficulty.toLowerCase()] || 'bg-secondary';
};

const RecipeCard = ({ recipe }) => {
  const totalTime = recipe.prep_time + recipe.cook_time;

  return (
    <div className="card h-100 shadow-sm hover-card">
      <div className="card-body">
        <h5 className="card-title fw-bold text-truncate">{recipe.name}</h5>
        <p className="card-text text-muted small">{recipe.description}</p>
        
        <div className="d-flex justify-content-between align-items-center mb-3">
          <div className="d-flex gap-2">
            <span className="badge bg-primary">
              <i className="bi bi-clock me-1"></i>
              {formatTime(recipe.prep_time)}
            </span>
            <span className="badge bg-info">
              <i className="bi bi-fire me-1"></i>
              {formatTime(recipe.cook_time)}
            </span>
          </div>
          <span className={`badge ${getDifficultyClass(recipe.difficulty)}`}>
            {recipe.difficulty}
          </span>
        </div>

        {recipe.ingredients && recipe.ingredients.length > 0 && (
          <div className="mb-3">
            <h6 className="fw-bold mb-2">Ingredients:</h6>
            <div className="d-flex flex-wrap gap-1">
              {recipe.ingredients.map((ingredient, index) => (
                <span key={index} className="badge bg-light text-dark">
                  {ingredient}
                </span>
              ))}
            </div>
          </div>
        )}

        {recipe.tags && recipe.tags.length > 0 && (
          <div>
            <h6 className="fw-bold mb-2">Tags:</h6>
            <div className="d-flex flex-wrap gap-1">
              {recipe.tags.map((tag, index) => (
                <span key={index} className="badge bg-secondary">
                  {tag}
                </span>
              ))}
            </div>
          </div>
        )}

        <div className="mt-3 text-center">
          <button className="btn btn-outline-primary btn-sm">
            View Recipe
          </button>
        </div>
      </div>
    </div>
  );
};

export default RecipeCard; 