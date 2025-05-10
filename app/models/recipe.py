from datetime import datetime
from sqlalchemy import Column, Integer, String, Float, DateTime, Table, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

# Association tables for many-to-many relationships
recipe_ingredients = Table('recipe_ingredients', Base.metadata,
    Column('recipe_id', Integer, ForeignKey('recipes.id')),
    Column('ingredient_id', Integer, ForeignKey('ingredients.id'))
)

recipe_tags = Table('recipe_tags', Base.metadata,
    Column('recipe_id', Integer, ForeignKey('recipes.id')),
    Column('tag_id', Integer, ForeignKey('tags.id'))
)

class Recipe(Base):
    __tablename__ = 'recipes'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    description = Column(String(500))
    instructions = Column(String(2000))
    prep_time = Column(Integer)  # in minutes
    cook_time = Column(Integer)  # in minutes
    servings = Column(Integer)
    difficulty = Column(String(20))
    video_url = Column(String(200))
    image_url = Column(String(200))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    ingredients = relationship("Ingredient", secondary=recipe_ingredients, back_populates="recipes")
    tags = relationship("Tag", secondary=recipe_tags, back_populates="recipes")
    ratings = relationship("Rating", back_populates="recipe")

    def __repr__(self):
        return f"<Recipe {self.name}>"

class Ingredient(Base):
    __tablename__ = 'ingredients'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False, unique=True)
    category = Column(String(50))
    recipes = relationship("Recipe", secondary=recipe_ingredients, back_populates="ingredients")

    def __repr__(self):
        return f"<Ingredient {self.name}>"

class Tag(Base):
    __tablename__ = 'tags'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False, unique=True)
    recipes = relationship("Recipe", secondary=recipe_tags, back_populates="tags")

    def __repr__(self):
        return f"<Tag {self.name}>"

class Rating(Base):
    __tablename__ = 'ratings'

    id = Column(Integer, primary_key=True)
    recipe_id = Column(Integer, ForeignKey('recipes.id'))
    user_id = Column(Integer, ForeignKey('users.id'))
    rating = Column(Float)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    recipe = relationship("Recipe", back_populates="ratings")
    user = relationship("User", back_populates="ratings")

    def __repr__(self):
        return f"<Rating {self.rating} for Recipe {self.recipe_id}>" 