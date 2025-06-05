document.addEventListener('DOMContentLoaded', function() {
    const recipeForm = document.getElementById('recipeForm');
    const recipeResults = document.getElementById('recipeResults');

    // Load all recipes on page load
    loadAllRecipes();

    // Handle form submission
    recipeForm.addEventListener('submit', function(e) {
        e.preventDefault();
        getRecipes();
    });

    // Function to load all recipes
    async function loadAllRecipes() {
        try {
            const response = await fetch('/api/recipes');
            const recipes = await response.json();
            displayRecipes(recipes);
        } catch (error) {
            console.error('Error loading recipes:', error);
            showError('Failed to load recipes. Please try again later.');
        }
    }

    // Function to get recipes based on filters
    async function getRecipes() {
        const formData = new FormData(recipeForm);
        const dietaryRestrictions = Array.from(formData.getAll('dietary'));
        const cuisine = formData.get('cuisine');
        const ingredients = formData.get('ingredients')
            .split(',')
            .map(ing => ing.trim())
            .filter(ing => ing);

        const preferences = {
            dietary_restrictions: dietaryRestrictions,
            available_ingredients: ingredients
        };

        if (cuisine) {
            preferences.dietary_restrictions.push(cuisine);
        }

        try {
            recipeResults.classList.add('loading');
            const response = await fetch('/api/recipes/recommend', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ preferences }),
            });

            const recipes = await response.json();
            displayRecipes(recipes);
        } catch (error) {
            console.error('Error getting recipes:', error);
            showError('Failed to get recipes. Please try again later.');
        } finally {
            recipeResults.classList.remove('loading');
        }
    }

    // Function to display recipes
    function displayRecipes(recipes) {
        recipeResults.innerHTML = '';

        if (recipes.length === 0) {
            recipeResults.innerHTML = `
                <div class="col-12">
                    <div class="alert alert-info">
                        No recipes found matching your criteria. Try adjusting your filters.
                    </div>
                </div>
            `;
            return;
        }

        // Display recipes
        recipes.forEach(recipe => {
            const card = document.createElement('div');
            card.className = 'col-md-6 mb-4';
            card.innerHTML = `
                <div class="card h-100">
                    <div class="card-body">
                        <h5 class="card-title">${recipe.name}</h5>
                        <p class="card-text">${recipe.description}</p>
                        <div class="recipe-details">
                            <p><strong>Preparation Time:</strong> ${recipe.prep_time} minutes</p>
                            <p><strong>Cooking Time:</strong> ${recipe.cook_time} minutes</p>
                            <p><strong>Difficulty:</strong> ${recipe.difficulty}</p>
                            <p><strong>Ingredients:</strong> ${recipe.ingredients.join(', ')}</p>
                            <p><strong>Tags:</strong> ${recipe.tags.join(', ')}</p>
                        </div>
                    </div>
                </div>
            `;
            recipeResults.appendChild(card);
        });
    }

    // Function to show error message
    function showError(message) {
        recipeResults.innerHTML = `
            <div class="col-12">
                <div class="alert alert-danger">
                    ${message}
                </div>
            </div>
        `;
    }
}); 