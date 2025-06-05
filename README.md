# QuiteBite - Recipe Recommendation System

QuiteBite is a modern web application that helps users discover and explore recipes based on their preferences, dietary restrictions, and available ingredients. The system provides personalized recipe recommendations and allows users to save their favorite recipes.

## Features

- **Recipe Discovery**: Browse through a diverse collection of recipes from various cuisines
- **Smart Recommendations**: Get personalized recipe suggestions based on:
  - Dietary restrictions (vegetarian, vegan, gluten-free)
  - Available ingredients
  - Cuisine preferences
- **Recipe Details**: View comprehensive recipe information including:
  - Preparation and cooking times
  - Difficulty level
  - Ingredients list
  - Step-by-step instructions
  - Tags and categories
- **User Preferences**: Save and manage:
  - Dietary restrictions
  - Allergies
  - Cuisine preferences
  - Favorite recipes

## Tech Stack

### Backend
- Python 3.9+
- Flask (Web Framework)
- SQLAlchemy (ORM)
- SQLite (Database)

### Frontend
- React.js
- Bootstrap 5
- CSS3

## Prerequisites

- Python 3.9 or higher
- Node.js 14 or higher
- Yarn package manager
- Git

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/QuiteBite.git
cd QuiteBite
```

2. Set up the Python virtual environment:
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

3. Set up the frontend:
```bash
cd frontend
yarn install
```

4. Initialize the database:
```bash
# Make sure you're in the project root directory
python add_recipes.py
```

## Running the Application

1. Start the backend server:
```bash
# Make sure you're in the project root directory and virtual environment is activated
python run.py
```
The backend server will run on http://localhost:5002

2. Start the frontend development server:
```bash
cd frontend
yarn start
```
The frontend application will run on http://localhost:3000

## Troubleshooting

### Backend Issues

1. **ImportError: cannot import name 'Rating'**
   - Make sure the Rating model is properly defined in `app/models/recipe.py`
   - Check that all model relationships are correctly set up

2. **Database Connection Issues**
   - Verify that SQLite database file exists
   - Check database permissions
   - Ensure all required tables are created

3. **Port Already in Use**
   - If port 5002 is already in use:
   ```bash
   # Find the process using port 5002
   lsof -i :5002
   # Kill the process
   kill <PID>
   ```

### Frontend Issues

1. **Port 3000 Already in Use**
   - If you see "Something is already running on port 3000":
   - Press 'Y' to use a different port
   - Or kill the existing process:
   ```bash
   lsof -i :3000
   kill <PID>
   ```

2. **Failed to Fetch**
   - Ensure backend server is running
   - Check CORS configuration in `run.py`
   - Verify API endpoint URLs in frontend code

3. **Module Not Found**
   - Make sure all dependencies are installed:
   ```bash
   cd frontend
   yarn install
   ```

## API Endpoints

### Recipes
- `GET /api/recipes` - Get all recipes
- `POST /api/recipes/recommend` - Get recipe recommendations
  ```json
  {
    "preferences": {
      "dietary_restrictions": ["vegetarian"],
      "available_ingredients": ["pasta", "tomato", "garlic"]
    }
  }
  ```

### User Preferences
- `POST /api/users/{user_id}/preferences` - Update user preferences
  ```json
  {
    "allergies": ["peanuts"],
    "preferences": ["spicy", "low-sodium"]
  }
  ```

### Recipe Ratings
- `POST /api/recipes/{recipe_id}/rate` - Rate a recipe
  ```json
  {
    "user_id": 1,
    "rating": 4.5
  }
  ```

## Project Structure

```
QuiteBite/
├── app/
│   ├── models/
│   │   ├── recipe.py      # Recipe, Ingredient, Tag, and Rating models
│   │   └── user.py        # User, Allergy, Preference models
│   ├── recommender/
│   │   └── recommender.py # Recipe recommendation logic
│   └── database.py        # Database configuration
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── RecipeCard.js  # Recipe display component
│   │   │   └── SearchForm.js  # Search and filter component
│   │   └── App.js            # Main application component
│   └── package.json
├── static/                 # Static files
├── templates/             # HTML templates
├── run.py                # Flask application entry point
├── add_recipes.py        # Database initialization script
└── requirements.txt      # Python dependencies
```

## Development

### Adding New Recipes
1. Edit `add_recipes.py` to add new recipe data
2. Run the script to update the database:
```bash
python add_recipes.py
```

### Modifying the Frontend
1. Make changes to React components in `frontend/src/components/`
2. The development server will automatically reload

### Database Changes
1. Modify models in `app/models/`
2. Update database schema:
```bash
# Drop existing tables (if needed)
rm quickbites.db
# Recreate database
python add_recipes.py
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Recipe data sourced from various culinary resources
- Icons and UI components from Bootstrap
- Development tools and libraries from the open-source community 