from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, Table, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

# Association tables for many-to-many relationships
user_allergies = Table('user_allergies', Base.metadata,
    Column('user_id', Integer, ForeignKey('users.id')),
    Column('allergy_id', Integer, ForeignKey('allergies.id'))
)

user_preferences = Table('user_preferences', Base.metadata,
    Column('user_id', Integer, ForeignKey('users.id')),
    Column('preference_id', Integer, ForeignKey('preferences.id'))
)

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    password_hash = Column(String(128))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    allergies = relationship("Allergy", secondary=user_allergies, back_populates="users")
    preferences = relationship("Preference", secondary=user_preferences, back_populates="users")
    ratings = relationship("Rating", back_populates="user")
    saved_recipes = relationship("SavedRecipe", back_populates="user")

    def __repr__(self):
        return f"<User {self.username}>"

class Allergy(Base):
    __tablename__ = 'allergies'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False, unique=True)
    users = relationship("User", secondary=user_allergies, back_populates="allergies")

    def __repr__(self):
        return f"<Allergy {self.name}>"

class Preference(Base):
    __tablename__ = 'preferences'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False, unique=True)
    users = relationship("User", secondary=user_preferences, back_populates="preferences")

    def __repr__(self):
        return f"<Preference {self.name}>"

class SavedRecipe(Base):
    __tablename__ = 'saved_recipes'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    recipe_id = Column(Integer, ForeignKey('recipes.id'))
    saved_at = Column(DateTime, default=datetime.utcnow)
    
    user = relationship("User", back_populates="saved_recipes")
    recipe = relationship("Recipe")

    def __repr__(self):
        return f"<SavedRecipe {self.recipe_id} for User {self.user_id}>" 