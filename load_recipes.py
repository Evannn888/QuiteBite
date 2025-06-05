import json
from app.database import SessionLocal, engine
from app.models.recipe import Base, Recipe, Ingredient, Tag
from sqlalchemy.orm import Session

def load_recipes_from_json():
    # Create database tables
    Base.metadata.create_all(bind=engine)
    
    # Read JSON file
    with open('database_init.json', 'r') as f:
        data = json.load(f)
    
    # Initialize database session
    db = SessionLocal()
    
    try:
        # Process each recipe
        for recipe_data in data['recipes']:
            # Create recipe
            recipe = Recipe(
                name=recipe_data['name'],
                description=recipe_data['description'],
                instructions=recipe_data['instructions'],
                prep_time=recipe_data['prep_time'],
                cook_time=recipe_data['cook_time'],
                servings=recipe_data['servings'],
                difficulty=recipe_data['difficulty']
            )
            
            # Add ingredients
            for ingredient_name in recipe_data['ingredients']:
                # Check if ingredient exists
                ingredient = db.query(Ingredient).filter_by(name=ingredient_name).first()
                if not ingredient:
                    ingredient = Ingredient(name=ingredient_name)
                    db.add(ingredient)
                    db.flush()
                recipe.ingredients.append(ingredient)
            
            # Add tags
            for tag_name in recipe_data['tags']:
                # Check if tag exists
                tag = db.query(Tag).filter_by(name=tag_name).first()
                if not tag:
                    tag = Tag(name=tag_name)
                    db.add(tag)
                    db.flush()
                recipe.tags.append(tag)
            
            # Add recipe to session
            db.add(recipe)
        
        # Commit all changes
        db.commit()
        print("Successfully loaded recipes into database!")
        
    except Exception as e:
        print(f"Error loading recipes: {str(e)}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    load_recipes_from_json() 