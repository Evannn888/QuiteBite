from flask import Flask, request, jsonify, render_template_string, render_template
from flask_cors import CORS
from app.database import engine, Base, get_db, SessionLocal
from app.models.recipe import Recipe, Ingredient, Tag, Rating
from app.models.user import User, Allergy, Preference, SavedRecipe
from app.recommender.recommender import RecipeRecommender
from sqlalchemy.orm import Session
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Create database tables
Base.metadata.create_all(bind=engine)

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes
recommender = RecipeRecommender()

# HTML template for the home page
HOME_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>QuickBites API</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            line-height: 1.6;
        }
        .endpoint {
            background-color: #f5f5f5;
            padding: 15px;
            margin: 10px 0;
            border-radius: 5px;
        }
        code {
            background-color: #e0e0e0;
            padding: 2px 5px;
            border-radius: 3px;
        }
        h1, h2 {
            color: #333;
        }
    </style>
</head>
<body>
    <h1>Welcome to QuickBites API</h1>
    <p>This is a RESTful API for the QuickBites recipe recommendation system.</p>
    
    <h2>Available Endpoints:</h2>
    
    <div class="endpoint">
        <h3>Get All Recipes</h3>
        <p><code>GET /api/recipes</code></p>
        <p>Returns a list of all available recipes.</p>
    </div>

    <div class="endpoint">
        <h3>Get Recipe Recommendations</h3>
        <p><code>POST /api/recipes/recommend</code></p>
        <p>Get personalized recipe recommendations based on user preferences.</p>
        <p>Example request body:</p>
        <pre>
{
    "preferences": {
        "dietary_restrictions": ["vegetarian"],
        "available_ingredients": ["pasta", "tomato", "garlic"]
    }
}
        </pre>
    </div>

    <div class="endpoint">
        <h3>Update User Preferences</h3>
        <p><code>POST /api/users/{user_id}/preferences</code></p>
        <p>Update user preferences and dietary restrictions.</p>
        <p>Example request body:</p>
        <pre>
{
    "allergies": ["peanuts"],
    "preferences": ["spicy", "low-sodium"]
}
        </pre>
    </div>

    <div class="endpoint">
        <h3>Rate a Recipe</h3>
        <p><code>POST /api/recipes/{recipe_id}/rate</code></p>
        <p>Rate a recipe (1-5 stars).</p>
        <p>Example request body:</p>
        <pre>
{
    "user_id": 1,
    "rating": 4.5
}
        </pre>
    </div>
</body>
</html>
"""

@app.route('/')
def index():
    """Render the main page."""
    return render_template('index.html')

@app.route('/api/recipes')
def get_recipes():
    """Get all recipes."""
    db = SessionLocal()
    try:
        recipes = db.query(Recipe).all()
        return jsonify([{
            'id': recipe.id,
            'name': recipe.name,
            'description': recipe.description,
            'prep_time': recipe.prep_time,
            'cook_time': recipe.cook_time,
            'difficulty': recipe.difficulty,
            'ingredients': [ing.name for ing in recipe.ingredients],
            'tags': [tag.name for tag in recipe.tags]
        } for recipe in recipes])
    finally:
        db.close()

@app.route('/api/recipes/recommend', methods=['POST'])
def recommend_recipes():
    """Get recipe recommendations based on user preferences."""
    data = request.json
    preferences = data.get('preferences', {})
    db = SessionLocal()
    try:
        recipes = db.query(Recipe).all()
        # Convert recipes to dictionary format
        recipe_dicts = [{
            'id': recipe.id,
            'name': recipe.name,
            'description': recipe.description,
            'prep_time': recipe.prep_time,
            'cook_time': recipe.cook_time,
            'difficulty': recipe.difficulty,
            'ingredients': [ing.name for ing in recipe.ingredients],
            'tags': [tag.name for tag in recipe.tags]
        } for recipe in recipes]
        
        # Get recommendations
        recommendations = recommender.get_recommendations(
            recipe_dicts,
            preferences,
            n_recommendations=5
        )
        
        return jsonify(recommendations)
    finally:
        db.close()

@app.route('/api/users/<int:user_id>/preferences', methods=['POST'])
def update_user_preferences(user_id):
    data = request.get_json()
    db = next(get_db())
    
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        return jsonify({'error': 'User not found'}), 404
    
    # Update allergies
    if 'allergies' in data:
        allergies = []
        for allergy_name in data['allergies']:
            allergy = db.query(Allergy).filter(Allergy.name == allergy_name).first()
            if not allergy:
                allergy = Allergy(name=allergy_name)
                db.add(allergy)
            allergies.append(allergy)
        user.allergies = allergies
    
    # Update preferences
    if 'preferences' in data:
        preferences = []
        for pref_name in data['preferences']:
            preference = db.query(Preference).filter(Preference.name == pref_name).first()
            if not preference:
                preference = Preference(name=pref_name)
                db.add(preference)
            preferences.append(preference)
        user.preferences = preferences
    
    db.commit()
    return jsonify({'message': 'Preferences updated successfully'})

@app.route('/api/recipes/<int:recipe_id>/rate', methods=['POST'])
def rate_recipe(recipe_id):
    data = request.get_json()
    user_id = data.get('user_id')
    rating_value = data.get('rating')
    
    if not user_id or not rating_value:
        return jsonify({'error': 'Missing user_id or rating'}), 400
    
    db = next(get_db())
    
    # Check if recipe exists
    recipe = db.query(Recipe).filter(Recipe.id == recipe_id).first()
    if not recipe:
        return jsonify({'error': 'Recipe not found'}), 404
    
    # Create or update rating
    rating = db.query(Rating).filter(
        Rating.recipe_id == recipe_id,
        Rating.user_id == user_id
    ).first()
    
    if rating:
        rating.rating = rating_value
    else:
        rating = Rating(
            recipe_id=recipe_id,
            user_id=user_id,
            rating=rating_value
        )
        db.add(rating)
    
    db.commit()
    return jsonify({'message': 'Rating saved successfully'})

@app.route('/api/recipes/<int:recipe_id>/analyze', methods=['GET'])
def analyze_recipe(recipe_id):
    """Get detailed analysis of a recipe using DeepSeek API."""
    db = SessionLocal()
    try:
        recipe = db.query(Recipe).filter(Recipe.id == recipe_id).first()
        if not recipe:
            return jsonify({'error': 'Recipe not found'}), 404

        recipe_dict = {
            'id': recipe.id,
            'name': recipe.name,
            'description': recipe.description,
            'prep_time': recipe.prep_time,
            'cook_time': recipe.cook_time,
            'difficulty': recipe.difficulty,
            'ingredients': [ing.name for ing in recipe.ingredients],
            'tags': [tag.name for tag in recipe.tags]
        }

        analysis = deepseek_service.analyze_recipe(recipe_dict)
        return jsonify(analysis)
    finally:
        db.close()

@app.route('/api/recipes/suggest', methods=['POST'])
def suggest_recipes():
    """Get AI-generated recipe suggestions based on ingredients and preferences."""
    data = request.json
    preferences = data.get('preferences', {})
    ingredients = data.get('ingredients', [])

    suggestions = deepseek_service.get_recipe_suggestions(ingredients, preferences)
    return jsonify(suggestions)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=True) 