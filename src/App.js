import React, { useState, useEffect } from 'react';
import RecipeCard from './components/RecipeCard';
import SearchForm from './components/SearchForm';
import './App.css';

function App() {
  const [recipes, setRecipes] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [searchParams, setSearchParams] = useState(null);

  useEffect(() => {
    loadAllRecipes();
  }, []);

  const loadAllRecipes = async () => {
    try {
      setLoading(true);
      const response = await fetch('http://localhost:5002/api/recipes');
      if (!response.ok) {
        throw new Error('Failed to fetch recipes');
      }
      const data = await response.json();
      setRecipes(data);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  const handleSearch = async (params) => {
    try {
      setLoading(true);
      console.log('Sending search params:', params);
      setSearchParams(params.preferences);
      
      const response = await fetch('http://localhost:5002/api/recipes/recommend', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(params),
      });
      
      if (!response.ok) {
        throw new Error('Failed to get recipes');
      }
      
      const data = await response.json();
      console.log('Received recipes:', data);
      setRecipes(data);
    } catch (err) {
      console.error('Search error:', err);
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="container mt-4">
      <nav className="navbar navbar-expand-lg navbar-light bg-light mb-4 shadow-sm">
        <div className="container-fluid">
          <a className="navbar-brand fw-bold animate-brand" href="/">QuickBites</a>
        </div>
      </nav>

      <div className="row">
        <div className="col-md-4">
          <div className="card shadow-sm mb-4">
            <div className="card-body">
              <h5 className="card-title fw-bold">Find Recipes</h5>
              <SearchForm onSearch={handleSearch} />
            </div>
          </div>
        </div>
        <div className="col-md-8">
          {loading && (
            <div className="text-center my-5">
              <div className="spinner-border text-primary" role="status">
                <span className="visually-hidden">Loading...</span>
              </div>
            </div>
          )}
          
          {error && (
            <div className="alert alert-danger shadow-sm" role="alert">
              {error}
            </div>
          )}

          {!loading && !error && recipes.length === 0 && (
            <div className="alert alert-info shadow-sm" role="alert">
              No recipes found. Try adjusting your search criteria.
            </div>
          )}

          <div className="row row-cols-1 row-cols-md-2 g-4">
            {recipes.map((recipe) => (
              <div className="col" key={recipe.id}>
                <RecipeCard recipe={recipe} />
              </div>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;
