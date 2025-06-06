import React, { useState } from 'react';

function SearchForm({ onSearch }) {
  const [dietaryRestrictions, setDietaryRestrictions] = useState([]);
  const [cuisine, setCuisine] = useState('');
  const [ingredients, setIngredients] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    
    // Format the search parameters
    const searchParams = {
      preferences: {
        dietary_restrictions: dietaryRestrictions,
        cuisine: cuisine,
        available_ingredients: ingredients.split(',').map(i => i.trim()).filter(i => i)
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

  return (
    <div className="card">
      <div className="card-body">
        <h5 className="card-title">Find Recipes</h5>
        <form onSubmit={handleSubmit}>
          <div className="mb-3">
            <label className="form-label">Dietary Restrictions</label>
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
          </div>

          <div className="mb-3">
            <label htmlFor="cuisine" className="form-label">Cuisine</label>
            <select
              className="form-select"
              id="cuisine"
              value={cuisine}
              onChange={(e) => setCuisine(e.target.value)}
            >
              <option value="">Any</option>
              <option value="italian">Italian</option>
              <option value="mexican">Mexican</option>
              <option value="asian">Asian</option>
              <option value="indian">Indian</option>
              <option value="american">American</option>
            </select>
          </div>

          <div className="mb-3">
            <label htmlFor="ingredients" className="form-label">Available Ingredients</label>
            <input
              type="text"
              className="form-control"
              id="ingredients"
              value={ingredients}
              onChange={(e) => setIngredients(e.target.value)}
              placeholder="Enter ingredients separated by commas"
            />
          </div>

          <button type="submit" className="btn btn-primary">Get Recommendations</button>
        </form>
      </div>
    </div>
  );
}

export default SearchForm; 