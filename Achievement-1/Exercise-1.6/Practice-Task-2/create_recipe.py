import mysql.connector

def calculate_difficulty(cooking_time, ingredients):
    if cooking_time < 10 and len(ingredients) < 4:
        return "Easy"
    elif cooking_time < 10 and len(ingredients) >= 4:
        return "Medium"
    elif cooking_time >= 10 and len(ingredients) < 4:
        return "Intermediate"
    else:
        return "Hard"

def create_recipe():
    conn = mysql.connector.connect(
        host='localhost',
        user='cf-python',
        passwd='password',
        database='task_database'
    )
    cursor = conn.cursor()

    name = input("Enter the recipe name: ")
    cooking_time = int(input("Enter the cooking time (in minutes): "))
    ingredients = input("Enter the ingredients (comma-separated): ").split(", ")

    difficulty = calculate_difficulty(cooking_time, ingredients)

    cursor.execute('''INSERT INTO Recipes (name, ingredients, cooking_time, difficulty)
                      VALUES (%s, %s, %s, %s)''',
                   (name, ", ".join(ingredients), cooking_time, difficulty))

    conn.commit()
    conn.close()
    print("Recipe added successfully!")

create_recipe()

