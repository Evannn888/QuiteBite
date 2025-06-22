import React, { useState, useEffect } from 'react';
import RecipeCard from './components/RecipeCard';
import SearchForm from './components/SearchForm';
import './App.css';

function App() {
  const [recipes, setRecipes] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [searchParams, setSearchParams] = useState(null);
  const [totalRecipes, setTotalRecipes] = useState(0);
  const [darkMode, setDarkMode] = useState(false);
  const [favorites, setFavorites] = useState([]);
  const [showFavorites, setShowFavorites] = useState(false);

  useEffect(() => {
    loadAllRecipes();
    // Check for saved theme preference
    const savedTheme = localStorage.getItem('darkMode');
    if (savedTheme) {
      setDarkMode(JSON.parse(savedTheme));
    }
    
    // Load favorites from localStorage
    const savedFavorites = localStorage.getItem('favorites');
    if (savedFavorites) {
      setFavorites(JSON.parse(savedFavorites));
    }
  }, []);

  useEffect(() => {
    // Update body class when dark mode changes
    document.body.classList.toggle('dark-mode', darkMode);
    localStorage.setItem('darkMode', JSON.stringify(darkMode));
  }, [darkMode]);

  useEffect(() => {
    // Save favorites to localStorage
    localStorage.setItem('favorites', JSON.stringify(favorites));
  }, [favorites]);

  const toggleDarkMode = () => {
    setDarkMode(!darkMode);
  };

  const toggleFavorite = (recipeId) => {
    setFavorites(prev => {
      if (prev.includes(recipeId)) {
        return prev.filter(id => id !== recipeId);
      } else {
        return [...prev, recipeId];
      }
    });
  };

  const loadAllRecipes = async () => {
    try {
      setLoading(true);
      setError(null);
      const response = await fetch('http://localhost:5002/api/recipes');
      if (!response.ok) {
        throw new Error(`Failed to fetch recipes: ${response.statusText}`);
      }
      const data = await response.json();
      setRecipes(data);
      setTotalRecipes(data.length);
    } catch (err) {
      setError(err.message);
      console.error('Error loading recipes:', err);
    } finally {
      setLoading(false);
    }
  };

  const handleSearch = async (params) => {
    try {
      setLoading(true);
      setError(null);
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
        throw new Error(`Search failed: ${response.statusText}`);
      }
      
      const data = await response.json();
      console.log('Received recipes:', data);
      setRecipes(data);
      setTotalRecipes(data.length);
    } catch (err) {
      console.error('Search error:', err);
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  const getDisplayRecipes = () => {
    if (showFavorites) {
      return recipes.filter(recipe => favorites.includes(recipe.id));
    }
    return recipes;
  };

  return (
    <div className={`container mt-4 ${darkMode ? 'dark-mode' : ''}`}>
      <nav className="navbar navbar-expand-lg navbar-light bg-light mb-4 shadow-sm">
        <div className="container-fluid">
          <a className="navbar-brand fw-bold animate-brand" href="/">QuickBites</a>
          <div className="d-flex align-items-center">
            <span className="navbar-text text-muted me-3">
              {showFavorites ? `${favorites.length} favorites` : `${totalRecipes} recipes available`}
            </span>
            <button 
              className="btn btn-outline-primary btn-sm me-2"
              onClick={() => setShowFavorites(!showFavorites)}
              title={showFavorites ? "Show All Recipes" : "Show Favorites"}
            >
              <i className={`bi bi-${showFavorites ? 'house' : 'heart-fill'} fs-5`}></i>
            </button>
            <button 
              className="btn btn-outline-primary btn-sm ms-3"
              onClick={toggleDarkMode}
              title={darkMode ? "Switch to Light Mode" : "Switch to Dark Mode"}
            >
              <i className={`bi bi-${darkMode ? 'sun-fill' : 'moon-fill'} fs-5`}></i>
            </button>
          </div>
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
              <p className="mt-2 text-muted">Loading recipes...</p>
            </div>
          )}
          
          {error && (
            <div className="alert alert-danger shadow-sm" role="alert">
              <h4 className="alert-heading">Oops! Something went wrong</h4>
              <p>{error}</p>
              <hr />
              <p className="mb-0">Please try again or contact support if the problem persists.</p>
            </div>
          )}

          {!loading && !error && getDisplayRecipes().length === 0 && (
            <div className="alert alert-info shadow-sm" role="alert">
              <h4 className="alert-heading">
                {showFavorites ? "No favorites yet" : "No recipes found"}
              </h4>
              <p>
                {showFavorites 
                  ? "Start adding recipes to your favorites to see them here." 
                  : "Try adjusting your search criteria or browse all recipes."
                }
              </p>
              <hr />
              <button 
                className="btn btn-outline-primary"
                onClick={loadAllRecipes}
              >
                {showFavorites ? "Browse All Recipes" : "Show All Recipes"}
              </button>
            </div>
          )}

          <div className="row row-cols-1 row-cols-md-2 g-4">
            {getDisplayRecipes().map((recipe) => (
              <div key={recipe.id} className="col-md-6 col-lg-4 mb-4">
                <RecipeCard 
                  recipe={recipe} 
                  darkMode={darkMode}
                  isFavorite={favorites.includes(recipe.id)}
                  onToggleFavorite={() => toggleFavorite(recipe.id)}
                />
              </div>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;
