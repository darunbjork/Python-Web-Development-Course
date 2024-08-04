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

def create_recipe(conn, cursor):
    name = input("Enter the recipe name: ")
    cooking_time = int(input("Enter the cooking time (in minutes): "))
    ingredients = input("Enter the ingredients (comma-separated): ").split(", ")

    difficulty = calculate_difficulty(cooking_time, ingredients)

    cursor.execute('''INSERT INTO Recipes (name, ingredients, cooking_time, difficulty)
                      VALUES (%s, %s, %s, %s)''',
                   (name, ", ".join(ingredients), cooking_time, difficulty))

    conn.commit()
    print("Recipe added successfully!")

def search_recipe(conn, cursor):
    cursor.execute("SELECT ingredients FROM Recipes")
    results = cursor.fetchall()

    all_ingredients = set()
    for row in results:
        for ingredient in row[0].split(", "):
            all_ingredients.add(ingredient)

    print("Available ingredients: ")
    for i, ingredient in enumerate(all_ingredients):
        print(f"{i+1}. {ingredient}")

    choice = int(input("Choose an ingredient by number: ")) - 1
    search_ingredient = list(all_ingredients)[choice]

    cursor.execute('''SELECT id, name, ingredients, cooking_time, difficulty
                      FROM Recipes WHERE ingredients LIKE %s''',
                   (f"%{search_ingredient}%",))
    results = cursor.fetchall()

    for row in results:
        print(f"ID: {row[0]}")
        print(f"Name: {row[1]}")
        print(f"Ingredients: {row[2]}")
        print(f"Cooking Time: {row[3]}")
        print(f"Difficulty: {row[4]}")
        print()

def update_recipe(conn, cursor):
    cursor.execute("SELECT id, name FROM Recipes")
    results = cursor.fetchall()

    print("Available recipes: ")
    for row in results:
        print(f"ID: {row[0]}, Name: {row[1]}")

    recipe_id = int(input("Enter the ID of the recipe to update: "))
    column_to_update = input("Enter the column to update (name, cooking_time, ingredients): ")
    new_value = input(f"Enter the new value for {column_to_update}: ")

    if column_to_update == "cooking_time":
        new_value = int(new_value)
        cursor.execute("UPDATE Recipes SET cooking_time = %s WHERE id = %s", (new_value, recipe_id))
    elif column_to_update == "ingredients":
        ingredients = new_value.split(", ")
        cursor.execute("SELECT cooking_time FROM Recipes WHERE id = %s", (recipe_id,))
        cooking_time = cursor.fetchone()[0]
        difficulty = calculate_difficulty(cooking_time, ingredients)
        cursor.execute("UPDATE Recipes SET ingredients = %s, difficulty = %s WHERE id = %s", (", ".join(ingredients), difficulty, recipe_id))
    else:
        cursor.execute(f"UPDATE Recipes SET {column_to_update} = %s WHERE id = %s", (new_value, recipe_id))

    conn.commit()
    print("Recipe updated successfully!")

def delete_recipe(conn, cursor):
    cursor.execute("SELECT id, name FROM Recipes")
    results = cursor.fetchall()

    print("Available recipes: ")
    for row in results:
        print(f"ID: {row[0]}, Name: {row[1]}")

    recipe_id = int(input("Enter the ID of the recipe to delete: "))

    cursor.execute("DELETE FROM Recipes WHERE id = %s", (recipe_id,))
    conn.commit()
    print("Recipe deleted successfully!")

def main_menu(conn, cursor):
    while True:
        print("Main Menu")
        print("1. Create a new recipe")
        print("2. Search for a recipe by ingredient")
        print("3. Update an existing recipe")
        print("4. Delete a recipe")
        print("Type 'quit' to exit the program.")
        choice = input("Your choice: ")

        if choice == '1':
            create_recipe(conn, cursor)
        elif choice == '2':
            search_recipe(conn, cursor)
        elif choice == '3':
            update_recipe(conn, cursor)
        elif choice == '4':
            delete_recipe(conn, cursor)
        elif choice == 'quit':
            break
        else:
            print("Invalid choice. Please try again.")

    conn.commit()
    conn.close()

# Call the main menu
conn = mysql.connector.connect(
    host='localhost',
    user='cf-python',
    passwd='password',
    database='task_database'
)
cursor = conn.cursor()
main_menu(conn, cursor)

