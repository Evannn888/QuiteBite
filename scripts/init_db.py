from app.database import SessionLocal, engine, Base
from app.models.recipe import Recipe, Ingredient, Tag
from app.models.user import User, Allergy, Preference
import json
import os

def init_db():
    # Create tables
    Base.metadata.create_all(bind=engine)
    
    # Create a new session
    db = SessionLocal()
    
    try:
        # Create sample ingredients
        ingredients = [
            Ingredient(name="chicken breast", category="meat"),
            Ingredient(name="rice", category="grain"),
            Ingredient(name="olive oil", category="oil"),
            Ingredient(name="salt", category="spice"),
            Ingredient(name="pepper", category="spice"),
            Ingredient(name="garlic", category="vegetable"),
            Ingredient(name="onion", category="vegetable"),
            Ingredient(name="tomato", category="vegetable"),
            Ingredient(name="pasta", category="grain"),
            Ingredient(name="cheese", category="dairy")
        ]
        
        for ingredient in ingredients:
            db.add(ingredient)
        
        # Create sample tags
        tags = [
            Tag(name="vegetarian"),
            Tag(name="vegan"),
            Tag(name="gluten-free"),
            Tag(name="dairy-free"),
            Tag(name="quick"),
            Tag(name="healthy"),
            Tag(name="low-carb"),
            Tag(name="high-protein")
        ]
        
        for tag in tags:
            db.add(tag)
        
        # Create sample recipes
        recipes = [
            Recipe(
                name="Simple Chicken and Rice",
                description="A quick and easy chicken and rice dish",
                instructions="1. Cook rice\n2. Season chicken\n3. Cook chicken\n4. Combine and serve",
                prep_time=10,
                cook_time=30,
                servings=4,
                difficulty="easy",
                video_url="https://example.com/chicken-rice",
                image_url="https://example.com/chicken-rice.jpg"
            ),
            Recipe(
                name="Pasta Primavera",
                description="Fresh vegetable pasta dish",
                instructions="1. Cook pasta\n2. Sauté vegetables\n3. Combine and serve",
                prep_time=15,
                cook_time=20,
                servings=4,
                difficulty="medium",
                video_url="https://example.com/pasta-primavera",
                image_url="https://example.com/pasta-primavera.jpg"
            )
        ]
        
        # Add ingredients and tags to recipes
        recipes[0].ingredients = [ingredients[0], ingredients[1], ingredients[2], ingredients[3], ingredients[4]]
        recipes[0].tags = [tags[4], tags[5], tags[7]]
        
        recipes[1].ingredients = [ingredients[8], ingredients[2], ingredients[3], ingredients[4], ingredients[5], ingredients[6], ingredients[7]]
        recipes[1].tags = [tags[0], tags[5]]
        
        for recipe in recipes:
            db.add(recipe)
        
        # Create sample user
        user = User(
            username="test_user",
            email="test@example.com",
            password_hash="hashed_password_here"
        )
        db.add(user)
        
        # Create sample allergies
        allergies = [
            Allergy(name="peanuts"),
            Allergy(name="shellfish")
        ]
        
        for allergy in allergies:
            db.add(allergy)
        
        # Create sample preferences
        preferences = [
            Preference(name="spicy"),
            Preference(name="low-sodium")
        ]
        
        for preference in preferences:
            db.add(preference)
        
        # Commit all changes
        db.commit()
        
        print("Database initialized successfully!")
        
    except Exception as e:
        print(f"An error occurred: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    init_db() 