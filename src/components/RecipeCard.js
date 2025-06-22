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

const StarRating = ({ rating, onRate, readonly = false }) => {
  const stars = [1, 2, 3, 4, 5];
  
  return (
    <div className="d-flex align-items-center">
      {stars.map((star) => (
        <i
          key={star}
          className={`bi bi-star${star <= rating ? '-fill' : ''} text-warning me-1`}
          style={{ cursor: readonly ? 'default' : 'pointer' }}
          onClick={() => !readonly && onRate(star)}
          title={readonly ? `${rating}/5 stars` : `Rate ${star} stars`}
        />
      ))}
      {!readonly && (
        <small className="text-muted ms-2">Click to rate</small>
      )}
    </div>
  );
};

const RecipeCard = ({ recipe, darkMode, isFavorite, onToggleFavorite }) => {
  const [isExpanded, setIsExpanded] = useState(false);
  const [userRating, setUserRating] = useState(0);
  const [isRated, setIsRated] = useState(false);
  const totalTime = recipe.prep_time + recipe.cook_time;

  const toggleExpand = () => {
    setIsExpanded(!isExpanded);
  };

  const handleRate = async (rating) => {
    setUserRating(rating);
    setIsRated(true);
    
    // Here you would typically send the rating to your backend
    try {
      await fetch(`http://localhost:5002/api/recipes/${recipe.id}/rate`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          user_id: 1, // This would come from user authentication
          rating: rating
        }),
      });
    } catch (error) {
      console.error('Failed to save rating:', error);
    }
  };

  return (
    <div className={`card h-100 shadow-sm hover-card ${darkMode ? 'dark-mode' : ''}`}>
      <div className="card-body">
        <div className="d-flex justify-content-between align-items-start mb-2">
          <h5 className="card-title fw-bold text-truncate" title={recipe.name}>
            {recipe.name}
          </h5>
          <div className="d-flex align-items-center">
            <button
              className="btn btn-link btn-sm p-0 me-2"
              onClick={onToggleFavorite}
              title={isFavorite ? "Remove from favorites" : "Add to favorites"}
            >
              <i className={`bi bi-heart${isFavorite ? '-fill' : ''} text-danger fs-5`}></i>
            </button>
            <StarRating 
              rating={recipe.average_rating || 0} 
              readonly={true}
            />
          </div>
        </div>
        
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
          <div className="mb-3">
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

        <div className="mb-3">
          <h6 className="fw-bold mb-2">
            <i className="bi bi-star me-1"></i>
            Rate this recipe:
          </h6>
          <StarRating 
            rating={userRating} 
            onRate={handleRate}
            readonly={isRated}
          />
          {isRated && (
            <div className="alert alert-success alert-sm mt-2">
              <i className="bi bi-check-circle me-1"></i>
              Thank you for rating!
            </div>
          )}
        </div>

        <div className="mt-3 text-center">
          <button 
            className="btn btn-outline-primary btn-sm me-2"
            onClick={toggleExpand}
          >
            <i className={`bi bi-${isExpanded ? 'chevron-up' : 'chevron-down'} me-1`}></i>
            {isExpanded ? 'Show Less' : 'Show More'}
          </button>
          <button className="btn btn-outline-primary btn-sm">
            <i className="bi bi-share me-1"></i>
            Share Recipe
          </button>
        </div>
      </div>
    </div>
  );
};

export default RecipeCard; 