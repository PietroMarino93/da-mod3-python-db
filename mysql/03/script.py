import mysql.connector
from mysql.connector import Error

try:
    # Establish a connection to the MySQL database
    connection = mysql.connector.connect(
        host='localhost',
        user='python_user',
        password='Python',
        database='test_join'
    )

    if connection.is_connected():
        # Create a cursor object to interact with the database
        cursor = connection.cursor()

        # Define a parameterized query to retrieve data
        query = "SELECT * FROM studente WHERE Classe = %s"
        value = ('2',)

        # Execute the parameterized query
        cursor.execute(query, value)

        # Fetch all the rows from the executed query
        results = cursor.fetchall()

        # Print the results
        for row in results:
            print(row)

except Error as e:
    print(f"Error: {e}")

finally:
    # Ensure the cursor and connection are closed to free up resources
    if cursor:
        cursor.close()
    if connection and connection.is_connected():
        connection.close()