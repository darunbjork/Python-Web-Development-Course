import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Practice-Task-1')))

from setup_database import Recipe, engine
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()

recipes = session.query(Recipe).all()
print("Available recipes:")
for recipe in recipes:
    print(f"ID: {recipe.id}, Name: {recipe.name}")

session.close()
