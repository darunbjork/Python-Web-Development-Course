import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    user='cf-python',
    passwd='password'
)

cursor = conn.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS task_database")
cursor.execute("USE task_database")

cursor.execute('''CREATE TABLE IF NOT EXISTS Recipes (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    name VARCHAR(50),
                    ingredients VARCHAR(255),
                    cooking_time INT,
                    difficulty VARCHAR(20)
                 )''')

conn.commit()
conn.close()

