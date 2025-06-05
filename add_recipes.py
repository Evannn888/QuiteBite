from app.database import SessionLocal, engine, Base
from app.models.recipe import Recipe, Ingredient, Tag
from sqlalchemy.orm import Session

# Create database tables
Base.metadata.create_all(bind=engine)

# Sample recipes data
recipes_data = [
    # Italian Cuisine
    {
        "name": "Classic Margherita Pizza",
        "description": "Traditional Italian pizza with fresh mozzarella, tomatoes, and basil",
        "prep_time": 30,
        "cook_time": 15,
        "servings": 4,
        "difficulty": "Medium",
        "ingredients": ["pizza dough", "fresh mozzarella", "tomatoes", "basil", "olive oil", "salt"],
        "tags": ["italian", "vegetarian", "pizza"]
    },
    {
        "name": "Spaghetti Carbonara",
        "description": "Creamy pasta dish with eggs, cheese, pancetta, and black pepper",
        "prep_time": 15,
        "cook_time": 20,
        "servings": 4,
        "difficulty": "Medium",
        "ingredients": ["spaghetti", "eggs", "pecorino cheese", "pancetta", "black pepper", "salt"],
        "tags": ["italian", "pasta"]
    },
    {
        "name": "Risotto ai Funghi",
        "description": "Creamy mushroom risotto with parmesan cheese",
        "prep_time": 20,
        "cook_time": 30,
        "servings": 4,
        "difficulty": "Medium",
        "ingredients": ["arborio rice", "mushrooms", "onion", "white wine", "parmesan", "butter", "vegetable stock"],
        "tags": ["italian", "vegetarian", "risotto"]
    },

    # Japanese Cuisine
    {
        "name": "Miso Ramen",
        "description": "Traditional Japanese noodle soup with miso broth",
        "prep_time": 30,
        "cook_time": 45,
        "servings": 4,
        "difficulty": "Medium",
        "ingredients": ["ramen noodles", "miso paste", "pork belly", "green onions", "corn", "seaweed", "egg"],
        "tags": ["japanese", "soup", "noodles"]
    },
    {
        "name": "Sushi Roll",
        "description": "Fresh salmon and avocado roll with sushi rice",
        "prep_time": 45,
        "cook_time": 15,
        "servings": 4,
        "difficulty": "Hard",
        "ingredients": ["sushi rice", "salmon", "avocado", "nori", "rice vinegar", "wasabi", "soy sauce"],
        "tags": ["japanese", "seafood", "sushi"]
    },
    {
        "name": "Chicken Teriyaki",
        "description": "Grilled chicken glazed with sweet teriyaki sauce",
        "prep_time": 20,
        "cook_time": 25,
        "servings": 4,
        "difficulty": "Easy",
        "ingredients": ["chicken breast", "teriyaki sauce", "ginger", "garlic", "sesame seeds", "green onions"],
        "tags": ["japanese", "chicken"]
    },

    # Mexican Cuisine
    {
        "name": "Chicken Enchiladas",
        "description": "Tortillas filled with chicken and cheese, covered in enchilada sauce",
        "prep_time": 30,
        "cook_time": 25,
        "servings": 6,
        "difficulty": "Medium",
        "ingredients": ["chicken", "tortillas", "enchilada sauce", "cheese", "onion", "sour cream"],
        "tags": ["mexican", "chicken"]
    },
    {
        "name": "Vegetarian Tacos",
        "description": "Crispy tacos filled with seasoned black beans and vegetables",
        "prep_time": 20,
        "cook_time": 15,
        "servings": 4,
        "difficulty": "Easy",
        "ingredients": ["taco shells", "black beans", "bell peppers", "onion", "lettuce", "tomato", "avocado"],
        "tags": ["mexican", "vegetarian", "tacos"]
    },
    {
        "name": "Chiles Rellenos",
        "description": "Stuffed poblano peppers with cheese and tomato sauce",
        "prep_time": 40,
        "cook_time": 30,
        "servings": 4,
        "difficulty": "Hard",
        "ingredients": ["poblano peppers", "cheese", "eggs", "flour", "tomato sauce", "onion", "garlic"],
        "tags": ["mexican", "vegetarian"]
    },

    # Indian Cuisine
    {
        "name": "Butter Chicken",
        "description": "Creamy tomato-based curry with tender chicken",
        "prep_time": 30,
        "cook_time": 40,
        "servings": 4,
        "difficulty": "Medium",
        "ingredients": ["chicken", "tomato sauce", "butter", "cream", "garam masala", "ginger", "garlic"],
        "tags": ["indian", "chicken", "curry"]
    },
    {
        "name": "Vegetable Biryani",
        "description": "Fragrant rice dish with mixed vegetables and spices",
        "prep_time": 30,
        "cook_time": 45,
        "servings": 6,
        "difficulty": "Medium",
        "ingredients": ["basmati rice", "mixed vegetables", "biryani spices", "yogurt", "onion", "mint"],
        "tags": ["indian", "vegetarian", "rice"]
    },
    {
        "name": "Palak Paneer",
        "description": "Cottage cheese cubes in spiced spinach gravy",
        "prep_time": 25,
        "cook_time": 20,
        "servings": 4,
        "difficulty": "Medium",
        "ingredients": ["paneer", "spinach", "onion", "tomato", "garlic", "ginger", "spices"],
        "tags": ["indian", "vegetarian"]
    },

    # Thai Cuisine
    {
        "name": "Pad Thai",
        "description": "Stir-fried rice noodles with tofu, peanuts, and tamarind sauce",
        "prep_time": 25,
        "cook_time": 15,
        "servings": 4,
        "difficulty": "Medium",
        "ingredients": ["rice noodles", "tofu", "peanuts", "tamarind sauce", "bean sprouts", "egg", "lime"],
        "tags": ["thai", "vegetarian", "noodles"]
    },
    {
        "name": "Green Curry",
        "description": "Coconut milk curry with green curry paste and vegetables",
        "prep_time": 20,
        "cook_time": 25,
        "servings": 4,
        "difficulty": "Medium",
        "ingredients": ["coconut milk", "green curry paste", "vegetables", "basil", "fish sauce", "palm sugar"],
        "tags": ["thai", "curry"]
    },
    {
        "name": "Tom Yum Soup",
        "description": "Hot and sour soup with mushrooms and lemongrass",
        "prep_time": 20,
        "cook_time": 15,
        "servings": 4,
        "difficulty": "Easy",
        "ingredients": ["mushrooms", "lemongrass", "lime", "chili", "fish sauce", "tomatoes", "cilantro"],
        "tags": ["thai", "soup"]
    },

    # Mediterranean Cuisine
    {
        "name": "Greek Moussaka",
        "description": "Layered eggplant casserole with spiced meat sauce",
        "prep_time": 45,
        "cook_time": 60,
        "servings": 6,
        "difficulty": "Hard",
        "ingredients": ["eggplant", "ground beef", "béchamel sauce", "tomato sauce", "onion", "garlic", "spices"],
        "tags": ["mediterranean", "greek"]
    },
    {
        "name": "Falafel Plate",
        "description": "Crispy chickpea patties with hummus and salad",
        "prep_time": 30,
        "cook_time": 20,
        "servings": 4,
        "difficulty": "Medium",
        "ingredients": ["chickpeas", "parsley", "onion", "garlic", "spices", "pita bread", "hummus"],
        "tags": ["mediterranean", "vegetarian"]
    },
    {
        "name": "Shakshuka",
        "description": "Eggs poached in spiced tomato sauce",
        "prep_time": 15,
        "cook_time": 25,
        "servings": 4,
        "difficulty": "Easy",
        "ingredients": ["eggs", "tomatoes", "bell peppers", "onion", "garlic", "spices", "feta cheese"],
        "tags": ["mediterranean", "vegetarian"]
    },

    # Korean Cuisine
    {
        "name": "Bibimbap",
        "description": "Rice bowl with vegetables, meat, and gochujang sauce",
        "prep_time": 40,
        "cook_time": 20,
        "servings": 4,
        "difficulty": "Medium",
        "ingredients": ["rice", "beef", "vegetables", "gochujang", "sesame oil", "egg", "kimchi"],
        "tags": ["korean", "rice bowl"]
    },
    {
        "name": "Kimchi Stew",
        "description": "Spicy fermented cabbage soup with pork",
        "prep_time": 20,
        "cook_time": 30,
        "servings": 4,
        "difficulty": "Easy",
        "ingredients": ["kimchi", "pork", "tofu", "onion", "garlic", "gochugaru", "green onions"],
        "tags": ["korean", "soup"]
    },
    {
        "name": "Korean Fried Chicken",
        "description": "Crispy fried chicken glazed with sweet and spicy sauce",
        "prep_time": 30,
        "cook_time": 20,
        "servings": 4,
        "difficulty": "Medium",
        "ingredients": ["chicken", "gochujang", "honey", "garlic", "ginger", "sesame seeds"],
        "tags": ["korean", "chicken"]
    },

    # Middle Eastern Cuisine
    {
        "name": "Lamb Shawarma",
        "description": "Spiced lamb wrapped in pita with tahini sauce",
        "prep_time": 30,
        "cook_time": 40,
        "servings": 4,
        "difficulty": "Medium",
        "ingredients": ["lamb", "pita bread", "tahini", "garlic", "spices", "lettuce", "tomato"],
        "tags": ["middle-eastern", "lamb"]
    },
    {
        "name": "Tabbouleh",
        "description": "Fresh parsley and bulgur wheat salad",
        "prep_time": 20,
        "cook_time": 0,
        "servings": 4,
        "difficulty": "Easy",
        "ingredients": ["bulgur wheat", "parsley", "mint", "tomato", "cucumber", "lemon", "olive oil"],
        "tags": ["middle-eastern", "vegetarian", "salad"]
    },
    {
        "name": "Baklava",
        "description": "Sweet pastry with layers of phyllo and nuts",
        "prep_time": 45,
        "cook_time": 35,
        "servings": 12,
        "difficulty": "Hard",
        "ingredients": ["phyllo dough", "pistachios", "honey", "butter", "sugar", "cinnamon"],
        "tags": ["middle-eastern", "dessert"]
    }
]

def add_recipes():
    db = SessionLocal()
    try:
        # Add ingredients
        ingredients = {}
        for recipe_data in recipes_data:
            for ingredient_name in recipe_data["ingredients"]:
                if ingredient_name not in ingredients:
                    ingredient = Ingredient(name=ingredient_name)
                    db.add(ingredient)
                    ingredients[ingredient_name] = ingredient
        db.commit()

        # Add tags
        tags = {}
        for recipe_data in recipes_data:
            for tag_name in recipe_data["tags"]:
                if tag_name not in tags:
                    tag = Tag(name=tag_name)
                    db.add(tag)
                    tags[tag_name] = tag
        db.commit()

        # Add recipes
        for recipe_data in recipes_data:
            recipe = Recipe(
                name=recipe_data["name"],
                description=recipe_data["description"],
                prep_time=recipe_data["prep_time"],
                cook_time=recipe_data["cook_time"],
                servings=recipe_data["servings"],
                difficulty=recipe_data["difficulty"],
                instructions="Detailed instructions will be added later."  # Adding placeholder instructions
            )
            
            # Add ingredients
            for ingredient_name in recipe_data["ingredients"]:
                recipe.ingredients.append(ingredients[ingredient_name])
            
            # Add tags
            for tag_name in recipe_data["tags"]:
                recipe.tags.append(tags[tag_name])
            
            db.add(recipe)
        
        db.commit()
        print("Successfully added recipes!")
    except Exception as e:
        print(f"Error adding recipes: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    add_recipes() 