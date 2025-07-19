# test_connection.py
import MySQLdb

try:
    db = MySQLdb.connect(
        host="localhost",
        user="cf-python",
        passwd="password",
        db="my_database"
    )
    print("Connection successful!")
except MySQLdb.Error as e:
    print(f"Connection failed: {e}")
finally:
    db.close()

