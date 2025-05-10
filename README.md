# QuickBites Recommendation System

A personalized meal recommendation platform that helps users discover recipes based on their preferences, dietary restrictions, and available ingredients.

## Features

- Personalized recipe recommendations using TensorFlow
- Database of 500+ recipes with video links
- Dietary restriction and allergy filtering
- Ingredient and cookware-based suggestions
- User preference learning

## Project Structure

```
quickbites/
├── app/
│   ├── models/         # Database models
│   ├── recommender/    # Recommendation system
│   ├── api/           # REST API endpoints
│   └── utils/         # Utility functions
├── data/              # Recipe data and models
├── tests/             # Test files
└── config/            # Configuration files
```

## Setup

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up the database:
```bash
python scripts/init_db.py
```

4. Run the application:
```bash
python run.py
```

## API Documentation

The API provides endpoints for:
- Recipe recommendations
- User preference management
- Recipe search and filtering
- Dietary restriction management

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request 