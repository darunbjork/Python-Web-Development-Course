import mysql.connector

def search_recipe():
    conn = mysql.connector.connect(
        host='localhost',
        user='cf-python',
        passwd='password',
        database='task_database'
    )
    cursor = conn.cursor()

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

    conn.close()

search_recipe()

