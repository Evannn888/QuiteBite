import React, { useState } from 'react';

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

const RecipeCard = ({ recipe, darkMode }) => {
  const [isExpanded, setIsExpanded] = useState(false);
  const totalTime = recipe.prep_time + recipe.cook_time;

  const toggleExpand = () => {
    setIsExpanded(!isExpanded);
  };

  return (
    <div className={`card h-100 shadow-sm hover-card ${darkMode ? 'dark-mode' : ''}`}>
      <div className="card-body">
        <h5 className="card-title fw-bold text-truncate" title={recipe.name}>
          {recipe.name}
        </h5>
        <p className="card-text text-muted small">
          {isExpanded ? recipe.description : `${recipe.description.substring(0, 100)}...`}
        </p>
        
        <div className="d-flex justify-content-between align-items-center mb-3">
          <div className="d-flex gap-2">
            <span className="badge bg-primary" title="Preparation Time">
              <i className="bi bi-clock me-1"></i>
              {formatTime(recipe.prep_time)}
            </span>
            <span className="badge bg-info" title="Cooking Time">
              <i className="bi bi-fire me-1"></i>
              {formatTime(recipe.cook_time)}
            </span>
          </div>
          <span className={`badge ${getDifficultyClass(recipe.difficulty)}`} title="Difficulty Level">
            {recipe.difficulty}
          </span>
        </div>

        {recipe.ingredients && recipe.ingredients.length > 0 && (
          <div className="mb-3">
            <h6 className="fw-bold mb-2">
              <i className="bi bi-list-check me-1"></i>
              Ingredients:
            </h6>
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
            <h6 className="fw-bold mb-2">
              <i className="bi bi-tags me-1"></i>
              Tags:
            </h6>
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
          <button 
            className="btn btn-outline-primary btn-sm me-2"
            onClick={toggleExpand}
          >
            <i className={`bi bi-${isExpanded ? 'chevron-up' : 'chevron-down'} me-1`}></i>
            {isExpanded ? 'Show Less' : 'Show More'}
          </button>
          <button className="btn btn-outline-primary btn-sm">
            <i className="bi bi-bookmark me-1"></i>
            Save Recipe
          </button>
        </div>
      </div>
    </div>
  );
};

export default RecipeCard; 