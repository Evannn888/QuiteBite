import React from 'react';

function RecipeCard({ recipe }) {
  return (
    <div className="card mb-4">
      <div className="card-header">
        <h5 className="card-title mb-0">{recipe.name}</h5>
      </div>
      <div className="card-body">
        <p className="card-text">{recipe.description}</p>
        <div className="recipe-details mb-3">
          <div className="row">
            <div className="col-6">
              <small className="text-muted">Prep Time: {recipe.prep_time} mins</small>
            </div>
            <div className="col-6">
              <small className="text-muted">Cook Time: {recipe.cook_time} mins</small>
            </div>
          </div>
          <div className="row mt-2">
            <div className="col-6">
              <small className="text-muted">Difficulty: {recipe.difficulty}</small>
            </div>
            <div className="col-6">
              <small className="text-muted">Servings: {recipe.servings}</small>
            </div>
          </div>
        </div>
        <div className="ingredients mb-3">
          <h6>Ingredients:</h6>
          <ul className="list-unstyled">
            {recipe.ingredients.map((ingredient, index) => (
              <li key={index} className="ingredient-item">
                <small>{ingredient}</small>
              </li>
            ))}
          </ul>
        </div>
        <div className="tags">
          {recipe.tags.map((tag, index) => (
            <span key={index} className="badge bg-primary me-1">
              {tag}
            </span>
          ))}
        </div>
      </div>
    </div>
  );
}

export default RecipeCard; 