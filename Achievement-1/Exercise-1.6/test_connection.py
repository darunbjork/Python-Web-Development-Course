import mysql.connector

try:
    conn = mysql.connector.connect(
        host='localhost',
        user='cf-python',
        passwd='password'
    )
    print("Connection successful!")
    conn.close()
except mysql.connector.Error as err:
    print(f"Error: {err}")

