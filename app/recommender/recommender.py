import tensorflow as tf
import numpy as np
from sklearn.preprocessing import StandardScaler
from typing import List, Dict, Any
import pandas as pd

class RecipeRecommender:
    def __init__(self):
        self.model = None
        self.scaler = StandardScaler()
        self.feature_columns = [
            'prep_time', 'cook_time', 'difficulty_level',
            'ingredient_count', 'tag_count'
        ]

    def build_model(self, input_dim: int):
        """Build the recommendation model architecture."""
        model = tf.keras.Sequential([
            tf.keras.layers.Dense(64, activation='relu', input_shape=(input_dim,)),
            tf.keras.layers.Dropout(0.2),
            tf.keras.layers.Dense(32, activation='relu'),
            tf.keras.layers.Dense(1, activation='sigmoid')
        ])
        
        model.compile(
            optimizer='adam',
            loss='binary_crossentropy',
            metrics=['accuracy']
        )
        
        self.model = model
        return model

    def prepare_features(self, recipes: List[Dict[str, Any]]) -> np.ndarray:
        """Prepare recipe features for the model."""
        if not recipes:
            return np.array([])
            
        features = []
        for recipe in recipes:
            feature_vector = [
                recipe.get('prep_time', 0),
                recipe.get('cook_time', 0),
                self._encode_difficulty(recipe.get('difficulty', 'medium')),
                len(recipe.get('ingredients', [])),
                len(recipe.get('tags', []))
            ]
            features.append(feature_vector)
        
        return self.scaler.fit_transform(np.array(features))

    def _encode_difficulty(self, difficulty: str) -> int:
        """Encode difficulty level to numerical value."""
        difficulty_map = {
            'easy': 1,
            'medium': 2,
            'hard': 3
        }
        return difficulty_map.get(difficulty.lower(), 2)

    def train(self, recipes: List[Dict[str, Any]], user_ratings: List[float]):
        """Train the recommendation model."""
        X = self.prepare_features(recipes)
        y = np.array(user_ratings)
        
        if self.model is None:
            self.build_model(X.shape[1])
        
        self.model.fit(
            X, y,
            epochs=10,
            batch_size=32,
            validation_split=0.2,
            verbose=1
        )

    def predict(self, recipes: List[Dict[str, Any]]) -> List[float]:
        """Predict user preferences for recipes."""
        if not recipes:
            return []
            
        if self.model is None:
            # If model is not trained, return scores based on a combination of factors
            scores = []
            for recipe in recipes:
                # Score based on preparation complexity (lower is better)
                time_score = 1.0 / (recipe.get('prep_time', 30) + recipe.get('cook_time', 30))
                # Score based on ingredient variety
                ingredient_score = len(recipe.get('ingredients', [])) / 10  # Normalize by assuming max 10 ingredients
                # Score based on tags (more tags = more versatile)
                tag_score = len(recipe.get('tags', [])) / 5  # Normalize by assuming max 5 tags
                
                # Combine scores with weights
                final_score = (0.4 * time_score + 0.3 * ingredient_score + 0.3 * tag_score)
                scores.append(final_score)
            
            # Normalize scores to 0-1 range
            if scores:
                min_score = min(scores)
                max_score = max(scores)
                if max_score > min_score:
                    scores = [(s - min_score) / (max_score - min_score) for s in scores]
            return scores
            
        X = self.prepare_features(recipes)
        predictions = self.model.predict(X)
        return predictions.flatten().tolist()

    def filter_by_dietary_restrictions(
        self,
        recipes: List[Dict[str, Any]],
        restrictions: List[str]
    ) -> List[Dict[str, Any]]:
        """Filter recipes based on dietary restrictions."""
        if not restrictions:
            return recipes
            
        filtered_recipes = []
        restrictions = [r.lower() for r in restrictions]
        for recipe in recipes:
            recipe_tags = [tag.lower() for tag in recipe.get('tags', [])]
            # Include recipes that match any of the dietary restrictions
            if any(tag in restrictions for tag in recipe_tags):
                filtered_recipes.append(recipe)
        return filtered_recipes

    def filter_by_cuisine(
        self,
        recipes: List[Dict[str, Any]],
        cuisine: str
    ) -> List[Dict[str, Any]]:
        """Filter recipes based on cuisine preference."""
        if not cuisine:
            return recipes
            
        filtered_recipes = []
        cuisine = cuisine.lower()
        for recipe in recipes:
            recipe_tags = [tag.lower() for tag in recipe.get('tags', [])]
            if cuisine in recipe_tags:
                filtered_recipes.append(recipe)
        return filtered_recipes

    def filter_by_ingredients(
        self,
        recipes: List[Dict[str, Any]],
        available_ingredients: List[str]
    ) -> List[Dict[str, Any]]:
        """Filter recipes based on available ingredients."""
        if not available_ingredients:
            return recipes
            
        filtered_recipes = []
        available_ingredients_lower = [ing.lower() for ing in available_ingredients]
        
        for recipe in recipes:
            recipe_ingredients = [ing.lower() for ing in recipe.get('ingredients', [])]
            
            # Calculate ingredient match score
            matching_ingredients = sum(1 for avail in available_ingredients_lower 
                                    if any(avail in ing for ing in recipe_ingredients))
            
            # If at least one ingredient matches, include the recipe
            if matching_ingredients > 0:
                # Add match score to recipe for better ranking
                recipe['ingredient_match_score'] = matching_ingredients / len(recipe_ingredients)
                filtered_recipes.append(recipe)
        
        return filtered_recipes

    def get_recommendations(
        self,
        recipes: List[Dict[str, Any]],
        user_preferences: Dict[str, Any],
        n_recommendations: int = 5
    ) -> List[Dict[str, Any]]:
        """Get personalized recipe recommendations."""
        # Apply filters
        filtered_recipes = self.filter_by_dietary_restrictions(
            recipes,
            user_preferences.get('dietary_restrictions', [])
        )
        
        # Filter by cuisine if specified
        if user_preferences.get('cuisine'):
            filtered_recipes = self.filter_by_cuisine(
                filtered_recipes,
                user_preferences['cuisine']
            )
        
        # Filter by available ingredients
        if user_preferences.get('available_ingredients'):
            filtered_recipes = self.filter_by_ingredients(
                filtered_recipes,
                user_preferences['available_ingredients']
            )
        
        # Get predictions
        predictions = self.predict(filtered_recipes)
        
        # Combine recipes with predictions and adjust scores based on ingredient matches
        recipe_scores = []
        for recipe, pred_score in zip(filtered_recipes, predictions):
            # Adjust score based on ingredient match if available
            if 'ingredient_match_score' in recipe:
                final_score = 0.7 * pred_score + 0.3 * recipe['ingredient_match_score']
                # Remove the temporary score
                del recipe['ingredient_match_score']
            else:
                final_score = pred_score
            recipe_scores.append((recipe, final_score))
        
        # Sort by final score
        recipe_scores.sort(key=lambda x: x[1], reverse=True)
        
        # Return top N recommendations
        return [recipe for recipe, _ in recipe_scores[:n_recommendations]] 