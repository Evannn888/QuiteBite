import React, { useState } from 'react';

function SearchForm({ onSearch }) {
  const [dietaryRestrictions, setDietaryRestrictions] = useState([]);
  const [cuisine, setCuisine] = useState('');
  const [ingredients, setIngredients] = useState('');
  const [maxTime, setMaxTime] = useState('');
  const [difficulty, setDifficulty] = useState('');
  const [tags, setTags] = useState('');
  const [sortBy, setSortBy] = useState('name');

  const handleSubmit = (e) => {
    e.preventDefault();
    
    // Format the search parameters
    const searchParams = {
      preferences: {
        dietary_restrictions: dietaryRestrictions,
        cuisine: cuisine,
        available_ingredients: ingredients.split(',').map(i => i.trim()).filter(i => i),
        max_time: maxTime ? parseInt(maxTime) : null,
        difficulty: difficulty,
        tags: tags.split(',').map(t => t.trim()).filter(t => t),
        sort_by: sortBy
      }
    };
    
    onSearch(searchParams);
  };

  const handleDietaryChange = (e) => {
    const value = e.target.value;
    if (e.target.checked) {
      setDietaryRestrictions([...dietaryRestrictions, value]);
    } else {
      setDietaryRestrictions(dietaryRestrictions.filter(dr => dr !== value));
    }
  };

  const clearFilters = () => {
    setDietaryRestrictions([]);
    setCuisine('');
    setIngredients('');
    setMaxTime('');
    setDifficulty('');
    setTags('');
    setSortBy('name');
  };

  return (
    <div className="card shadow-sm">
      <div className="card-body">
        <div className="d-flex justify-content-between align-items-center mb-3">
          <h5 className="card-title fw-bold mb-0">
            <i className="bi bi-search me-2"></i>
            Find Recipes
          </h5>
          <button 
            type="button" 
            className="btn btn-outline-secondary btn-sm"
            onClick={clearFilters}
          >
            <i className="bi bi-arrow-clockwise me-1"></i>
            Clear
          </button>
        </div>
        
        <form onSubmit={handleSubmit}>
          <div className="mb-3">
            <label className="form-label fw-bold">
              <i className="bi bi-heart me-1"></i>
              Dietary Restrictions
            </label>
            <div className="row">
              <div className="col-6">
                <div className="form-check">
                  <input
                    className="form-check-input"
                    type="checkbox"
                    value="vegetarian"
                    id="vegetarian"
                    onChange={handleDietaryChange}
                  />
                  <label className="form-check-label" htmlFor="vegetarian">
                    Vegetarian
                  </label>
                </div>
                <div className="form-check">
                  <input
                    className="form-check-input"
                    type="checkbox"
                    value="vegan"
                    id="vegan"
                    onChange={handleDietaryChange}
                  />
                  <label className="form-check-label" htmlFor="vegan">
                    Vegan
                  </label>
                </div>
              </div>
              <div className="col-6">
                <div className="form-check">
                  <input
                    className="form-check-input"
                    type="checkbox"
                    value="gluten-free"
                    id="gluten-free"
                    onChange={handleDietaryChange}
                  />
                  <label className="form-check-label" htmlFor="gluten-free">
                    Gluten-Free
                  </label>
                </div>
                <div className="form-check">
                  <input
                    className="form-check-input"
                    type="checkbox"
                    value="dairy-free"
                    id="dairy-free"
                    onChange={handleDietaryChange}
                  />
                  <label className="form-check-label" htmlFor="dairy-free">
                    Dairy-Free
                  </label>
                </div>
              </div>
            </div>
          </div>

          <div className="mb-3">
            <label htmlFor="cuisine" className="form-label fw-bold">
              <i className="bi bi-globe me-1"></i>
              Cuisine
            </label>
            <select
              className="form-select"
              id="cuisine"
              value={cuisine}
              onChange={(e) => setCuisine(e.target.value)}
            >
              <option value="">Any Cuisine</option>
              <option value="italian">Italian</option>
              <option value="mexican">Mexican</option>
              <option value="asian">Asian</option>
              <option value="indian">Indian</option>
              <option value="american">American</option>
              <option value="mediterranean">Mediterranean</option>
              <option value="french">French</option>
              <option value="thai">Thai</option>
              <option value="japanese">Japanese</option>
            </select>
          </div>

          <div className="mb-3">
            <label htmlFor="ingredients" className="form-label fw-bold">
              <i className="bi bi-basket me-1"></i>
              Available Ingredients
            </label>
            <input
              type="text"
              className="form-control"
              id="ingredients"
              value={ingredients}
              onChange={(e) => setIngredients(e.target.value)}
              placeholder="e.g., chicken, rice, tomatoes"
            />
            <div className="form-text">Separate ingredients with commas</div>
          </div>

          <div className="row mb-3">
            <div className="col-6">
              <label htmlFor="maxTime" className="form-label fw-bold">
                <i className="bi bi-clock me-1"></i>
                Max Time (mins)
              </label>
              <input
                type="number"
                className="form-control"
                id="maxTime"
                value={maxTime}
                onChange={(e) => setMaxTime(e.target.value)}
                placeholder="60"
                min="0"
              />
            </div>
            <div className="col-6">
              <label htmlFor="difficulty" className="form-label fw-bold">
                <i className="bi bi-speedometer2 me-1"></i>
                Difficulty
              </label>
              <select
                className="form-select"
                id="difficulty"
                value={difficulty}
                onChange={(e) => setDifficulty(e.target.value)}
              >
                <option value="">Any Level</option>
                <option value="easy">Easy</option>
                <option value="medium">Medium</option>
                <option value="hard">Hard</option>
              </select>
            </div>
          </div>

          <div className="mb-3">
            <label htmlFor="tags" className="form-label fw-bold">
              <i className="bi bi-tags me-1"></i>
              Tags
            </label>
            <input
              type="text"
              className="form-control"
              id="tags"
              value={tags}
              onChange={(e) => setTags(e.target.value)}
              placeholder="e.g., quick, healthy, spicy"
            />
            <div className="form-text">Separate tags with commas</div>
          </div>

          <div className="mb-3">
            <label htmlFor="sortBy" className="form-label fw-bold">
              <i className="bi bi-sort-down me-1"></i>
              Sort By
            </label>
            <select
              className="form-select"
              id="sortBy"
              value={sortBy}
              onChange={(e) => setSortBy(e.target.value)}
            >
              <option value="name">Name (A-Z)</option>
              <option value="prep_time">Preparation Time</option>
              <option value="cook_time">Cooking Time</option>
              <option value="difficulty">Difficulty</option>
              <option value="rating">Rating</option>
            </select>
          </div>

          <button type="submit" className="btn btn-primary w-100">
            <i className="bi bi-search me-2"></i>
            Get Recommendations
          </button>
        </form>
      </div>
    </div>
  );
}

export default SearchForm; 