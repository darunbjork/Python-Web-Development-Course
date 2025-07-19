import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Practice-Task-1')))

from setup_database import Recipe, Base, engine
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()

name = input("Enter the recipe name: ")
cooking_time = int(input("Enter the cooking time (in minutes): "))
ingredients = input("Enter the ingredients (comma-separated): ")

recipe = Recipe(name=name, cooking_time=cooking_time, ingredients=ingredients)
recipe.calculate_difficulty()

session.add(recipe)
session.commit()

print("Recipe added successfully!")
session.close()
