from sqlalchemy.orm import Session
from app.database import SessionLocal, engine, Base
from app.models.recipe import Recipe, Ingredient, Tag, Rating
from app.models.user import User
from datetime import datetime
import random

def clear_existing_data():
    db = SessionLocal()
    try:
        # Delete all data in reverse order of dependencies
        db.query(Rating).delete()
        db.query(Recipe).delete()
        db.query(Ingredient).delete()
        db.query(Tag).delete()
        db.query(User).delete()
        db.commit()
    except Exception as e:
        print(f"Error clearing data: {e}")
        db.rollback()
    finally:
        db.close()

def generate_sample_data():
    # Clear existing data first
    clear_existing_data()
    
    db = SessionLocal()
    
    # Create sample ingredients
    ingredients = [
        # Meats
        Ingredient(name="Chicken Breast", category="Meat"),
        Ingredient(name="Ground Beef", category="Meat"),
        Ingredient(name="Pork Belly", category="Meat"),
        Ingredient(name="Turkey Breast", category="Meat"),
        Ingredient(name="Lamb", category="Meat"),
        Ingredient(name="Duck Breast", category="Meat"),
        Ingredient(name="Bacon", category="Meat"),
        
        # Seafood
        Ingredient(name="Salmon", category="Seafood"),
        Ingredient(name="Shrimp", category="Seafood"),
        Ingredient(name="Tuna", category="Seafood"),
        Ingredient(name="Cod", category="Seafood"),
        Ingredient(name="Mussels", category="Seafood"),
        Ingredient(name="Crab", category="Seafood"),
        Ingredient(name="Scallops", category="Seafood"),
        
        # Grains & Pasta
        Ingredient(name="Jasmine Rice", category="Grain"),
        Ingredient(name="Sushi Rice", category="Grain"),
        Ingredient(name="Brown Rice", category="Grain"),
        Ingredient(name="Spaghetti", category="Pasta"),
        Ingredient(name="Penne", category="Pasta"),
        Ingredient(name="Udon Noodles", category="Pasta"),
        Ingredient(name="Rice Noodles", category="Pasta"),
        Ingredient(name="Quinoa", category="Grain"),
        Ingredient(name="Couscous", category="Grain"),
        Ingredient(name="Bulgur", category="Grain"),
        
        # Vegetables
        Ingredient(name="Garlic", category="Vegetable"),
        Ingredient(name="Ginger", category="Vegetable"),
        Ingredient(name="Green Onion", category="Vegetable"),
        Ingredient(name="Red Onion", category="Vegetable"),
        Ingredient(name="Tomato", category="Vegetable"),
        Ingredient(name="Cherry Tomatoes", category="Vegetable"),
        Ingredient(name="Sweet Potato", category="Vegetable"),
        Ingredient(name="Carrot", category="Vegetable"),
        Ingredient(name="Broccoli", category="Vegetable"),
        Ingredient(name="Cauliflower", category="Vegetable"),
        Ingredient(name="Spinach", category="Vegetable"),
        Ingredient(name="Kale", category="Vegetable"),
        Ingredient(name="Bell Pepper", category="Vegetable"),
        Ingredient(name="Mushroom", category="Vegetable"),
        Ingredient(name="Shiitake Mushroom", category="Vegetable"),
        Ingredient(name="Zucchini", category="Vegetable"),
        Ingredient(name="Eggplant", category="Vegetable"),
        Ingredient(name="Bok Choy", category="Vegetable"),
        
        # Proteins
        Ingredient(name="Firm Tofu", category="Protein"),
        Ingredient(name="Silken Tofu", category="Protein"),
        Ingredient(name="Tempeh", category="Protein"),
        Ingredient(name="Chickpeas", category="Protein"),
        Ingredient(name="Black Beans", category="Protein"),
        Ingredient(name="Lentils", category="Protein"),
        Ingredient(name="Edamame", category="Protein"),
        
        # Dairy & Alternatives
        Ingredient(name="Parmesan Cheese", category="Dairy"),
        Ingredient(name="Mozzarella", category="Dairy"),
        Ingredient(name="Feta Cheese", category="Dairy"),
        Ingredient(name="Greek Yogurt", category="Dairy"),
        Ingredient(name="Coconut Milk", category="Dairy"),
        Ingredient(name="Almond Milk", category="Dairy"),
        
        # Herbs & Spices
        Ingredient(name="Basil", category="Herb"),
        Ingredient(name="Cilantro", category="Herb"),
        Ingredient(name="Mint", category="Herb"),
        Ingredient(name="Thai Basil", category="Herb"),
        Ingredient(name="Cumin", category="Spice"),
        Ingredient(name="Turmeric", category="Spice"),
        Ingredient(name="Paprika", category="Spice"),
        Ingredient(name="Cayenne", category="Spice"),
        
        # Sauces & Condiments
        Ingredient(name="Soy Sauce", category="Sauce"),
        Ingredient(name="Sesame Oil", category="Oil"),
        Ingredient(name="Olive Oil", category="Oil"),
        Ingredient(name="Rice Vinegar", category="Sauce"),
        Ingredient(name="Miso Paste", category="Sauce"),
        Ingredient(name="Thai Curry Paste", category="Sauce"),
        Ingredient(name="Tahini", category="Sauce"),
        Ingredient(name="Pesto", category="Sauce")
    ]
    
    # Create sample tags
    tags = [
        # Dietary
        Tag(name="Vegetarian"),
        Tag(name="Vegan"),
        Tag(name="Gluten-Free"),
        Tag(name="Dairy-Free"),
        Tag(name="Keto"),
        Tag(name="Paleo"),
        Tag(name="Low-Carb"),
        Tag(name="High-Protein"),
        
        # Meal Type
        Tag(name="Breakfast"),
        Tag(name="Lunch"),
        Tag(name="Dinner"),
        Tag(name="Snack"),
        Tag(name="Appetizer"),
        Tag(name="Main Course"),
        Tag(name="Side Dish"),
        Tag(name="Dessert"),
        
        # Cuisine
        Tag(name="Italian"),
        Tag(name="Japanese"),
        Tag(name="Chinese"),
        Tag(name="Thai"),
        Tag(name="Indian"),
        Tag(name="Mediterranean"),
        Tag(name="Mexican"),
        Tag(name="Korean"),
        Tag(name="Vietnamese"),
        Tag(name="Middle Eastern"),
        
        # Characteristics
        Tag(name="Quick"),
        Tag(name="Easy"),
        Tag(name="Budget-Friendly"),
        Tag(name="Meal Prep"),
        Tag(name="One Pot"),
        Tag(name="Spicy"),
        Tag(name="Comfort Food"),
        Tag(name="Healthy"),
        Tag(name="Light"),
        Tag(name="Hearty")
    ]
    
    # Create sample recipes
    recipes = [
        # Asian Cuisine
        Recipe(
            name="Miso Ramen",
            description="Comforting Japanese ramen with miso broth",
            instructions="1. Prepare miso broth\n2. Cook noodles\n3. Prepare toppings\n4. Assemble bowl",
            prep_time=20,
            cook_time=30,
            servings=2,
            difficulty="Medium",
            video_url="https://example.com/videos/miso-ramen",
            image_url="https://example.com/images/miso-ramen.jpg"
        ),
        Recipe(
            name="Pad Thai",
            description="Classic Thai stir-fried rice noodles",
            instructions="1. Soak noodles\n2. Prepare sauce\n3. Stir-fry ingredients\n4. Combine and garnish",
            prep_time=25,
            cook_time=15,
            servings=4,
            difficulty="Medium",
            video_url="https://example.com/videos/pad-thai",
            image_url="https://example.com/images/pad-thai.jpg"
        ),
        Recipe(
            name="Korean Bibimbap",
            description="Colorful rice bowl with vegetables and gochujang",
            instructions="1. Cook rice\n2. Prepare vegetables\n3. Cook protein\n4. Assemble bowl",
            prep_time=30,
            cook_time=20,
            servings=2,
            difficulty="Medium",
            video_url="https://example.com/videos/bibimbap",
            image_url="https://example.com/images/bibimbap.jpg"
        ),
        
        # Mediterranean/Middle Eastern
        Recipe(
            name="Falafel Bowl",
            description="Crispy chickpea falafel with tahini sauce",
            instructions="1. Prepare falafel mix\n2. Form and fry\n3. Make tahini sauce\n4. Assemble bowl",
            prep_time=20,
            cook_time=20,
            servings=4,
            difficulty="Medium",
            video_url="https://example.com/videos/falafel",
            image_url="https://example.com/images/falafel.jpg"
        ),
        Recipe(
            name="Greek Moussaka",
            description="Layered eggplant and meat casserole",
            instructions="1. Prepare eggplant\n2. Make meat sauce\n3. Make bechamel\n4. Layer and bake",
            prep_time=45,
            cook_time=60,
            servings=6,
            difficulty="Hard",
            video_url="https://example.com/videos/moussaka",
            image_url="https://example.com/images/moussaka.jpg"
        ),
        
        # Italian
        Recipe(
            name="Pesto Pasta Primavera",
            description="Fresh pasta with seasonal vegetables and pesto",
            instructions="1. Cook pasta\n2. Prepare vegetables\n3. Make pesto\n4. Combine",
            prep_time=20,
            cook_time=15,
            servings=4,
            difficulty="Easy",
            video_url="https://example.com/videos/pesto-pasta",
            image_url="https://example.com/images/pesto-pasta.jpg"
        ),
        
        # Healthy/Modern
        Recipe(
            name="Buddha Bowl",
            description="Nourishing bowl with grains, vegetables, and tahini",
            instructions="1. Cook grains\n2. Roast vegetables\n3. Prepare sauce\n4. Assemble",
            prep_time=20,
            cook_time=30,
            servings=2,
            difficulty="Easy",
            video_url="https://example.com/videos/buddha-bowl",
            image_url="https://example.com/images/buddha-bowl.jpg"
        ),
        Recipe(
            name="Cauliflower Rice Stir-Fry",
            description="Low-carb stir-fry with cauliflower rice",
            instructions="1. Rice cauliflower\n2. Prepare vegetables\n3. Stir-fry\n4. Season",
            prep_time=15,
            cook_time=15,
            servings=4,
            difficulty="Easy",
            video_url="https://example.com/videos/cauli-rice",
            image_url="https://example.com/images/cauli-rice.jpg"
        ),
        
        # Breakfast
        Recipe(
            name="Acai Bowl",
            description="Refreshing breakfast bowl with superfoods",
            instructions="1. Blend acai\n2. Prepare toppings\n3. Assemble bowl\n4. Garnish",
            prep_time=10,
            cook_time=5,
            servings=1,
            difficulty="Easy",
            video_url="https://example.com/videos/acai-bowl",
            image_url="https://example.com/images/acai-bowl.jpg"
        ),
        Recipe(
            name="Shakshuka",
            description="Middle Eastern eggs in spiced tomato sauce",
            instructions="1. Make sauce\n2. Add eggs\n3. Simmer\n4. Garnish",
            prep_time=10,
            cook_time=20,
            servings=2,
            difficulty="Medium",
            video_url="https://example.com/videos/shakshuka",
            image_url="https://example.com/images/shakshuka.jpg"
        )
    ]
    
    # Add ingredients and tags to recipes with more specific combinations
    recipe_data = {
        "Miso Ramen": {
            "ingredients": ["Udon Noodles", "Miso Paste", "Firm Tofu", "Shiitake Mushroom", "Bok Choy", "Green Onion", "Ginger"],
            "tags": ["Japanese", "Main Course", "Comfort Food", "Vegetarian"]
        },
        "Pad Thai": {
            "ingredients": ["Rice Noodles", "Shrimp", "Firm Tofu", "Bean Sprouts", "Green Onion", "Peanuts"],
            "tags": ["Thai", "Main Course", "Spicy", "Quick"]
        },
        "Korean Bibimbap": {
            "ingredients": ["Brown Rice", "Spinach", "Carrot", "Mushroom", "Firm Tofu", "Gochujang"],
            "tags": ["Korean", "Healthy", "Main Course", "Vegetarian"]
        },
        "Falafel Bowl": {
            "ingredients": ["Chickpeas", "Tahini", "Cumin", "Parsley", "Garlic", "Olive Oil"],
            "tags": ["Middle Eastern", "Vegan", "Healthy", "High-Protein"]
        },
        "Greek Moussaka": {
            "ingredients": ["Eggplant", "Ground Beef", "Tomato", "Parmesan Cheese", "Olive Oil"],
            "tags": ["Mediterranean", "Main Course", "Comfort Food", "Hearty"]
        },
        "Pesto Pasta Primavera": {
            "ingredients": ["Penne", "Pesto", "Cherry Tomatoes", "Zucchini", "Parmesan Cheese"],
            "tags": ["Italian", "Vegetarian", "Quick", "Easy"]
        },
        "Buddha Bowl": {
            "ingredients": ["Quinoa", "Sweet Potato", "Kale", "Chickpeas", "Tahini"],
            "tags": ["Vegan", "Healthy", "Meal Prep", "Gluten-Free"]
        },
        "Cauliflower Rice Stir-Fry": {
            "ingredients": ["Cauliflower", "Bell Pepper", "Ginger", "Soy Sauce", "Sesame Oil"],
            "tags": ["Low-Carb", "Keto", "Quick", "Healthy"]
        },
        "Acai Bowl": {
            "ingredients": ["Acai", "Almond Milk", "Banana", "Berries", "Honey"],
            "tags": ["Breakfast", "Vegetarian", "Healthy", "Quick"]
        },
        "Shakshuka": {
            "ingredients": ["Eggs", "Tomato", "Bell Pepper", "Cumin", "Paprika"],
            "tags": ["Middle Eastern", "Breakfast", "Vegetarian", "One Pot"]
        }
    }

    # Create sample users with different preferences
    users = [
        User(username="health_nut", email="health@example.com"),
        User(username="veggie_lover", email="veggie@example.com"),
        User(username="spice_enthusiast", email="spicy@example.com"),
        User(username="quick_cook", email="quick@example.com"),
        User(username="gourmet_chef", email="chef@example.com"),
        User(username="budget_foodie", email="budget@example.com"),
        User(username="asian_cuisine_fan", email="asian@example.com"),
        User(username="keto_dieter", email="keto@example.com")
    ]
    
    # Add everything to the database
    db.add_all(ingredients)
    db.add_all(tags)
    
    # Add recipes with their specific ingredients and tags
    for recipe in recipes:
        recipe_info = recipe_data.get(recipe.name, {})
        if recipe_info:
            recipe_ingredients = [ing for ing in ingredients if ing.name in recipe_info.get("ingredients", [])]
            recipe_tags = [tag for tag in tags if tag.name in recipe_info.get("tags", [])]
            recipe.ingredients = recipe_ingredients
            recipe.tags = recipe_tags
        db.add(recipe)
    
    db.add_all(users)
    db.commit()
    
    # Generate random ratings with user preferences in mind
    for user in users:
        for recipe in recipes:
            if random.random() < 0.8:  # 80% chance of rating
                # Adjust rating based on user preferences
                base_rating = random.uniform(3.0, 5.0)
                
                # Modify rating based on user preferences
                if user.username == "health_nut" and "Healthy" in [t.name for t in recipe.tags]:
                    base_rating += 0.5
                elif user.username == "veggie_lover" and "Vegetarian" in [t.name for t in recipe.tags]:
                    base_rating += 0.5
                elif user.username == "spice_enthusiast" and "Spicy" in [t.name for t in recipe.tags]:
                    base_rating += 0.5
                elif user.username == "quick_cook" and "Quick" in [t.name for t in recipe.tags]:
                    base_rating += 0.5
                
                # Ensure rating stays within bounds
                final_rating = min(5.0, max(1.0, base_rating))
                
                rating = Rating(
                    recipe_id=recipe.id,
                    user_id=user.id,
                    rating=final_rating,
                    created_at=datetime.utcnow()
                )
                db.add(rating)
    
    db.commit()
    db.close()

if __name__ == "__main__":
    generate_sample_data()
    print("Sample data generated successfully!") 