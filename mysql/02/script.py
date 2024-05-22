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
        cont = 0
        while cont < 10:

            # Define a query to insert data into the table
            insert_query = "INSERT INTO studente (ID, Nome, Provincia, Classe) VALUES (%s, %s, %s, %s)"
            values = [
                ('15', 'Michele', 'Bologna', '1'),
            ]

            # Execute the insert query for multiple rows
            cursor.executemany(insert_query, values)

            # Commit the transaction
            connection.commit()
            print("Data inserted successfully")

        # Query to verify the inserted data
        select_query = "SELECT * FROM studente"
        cursor.execute(select_query)
        results = cursor.fetchall()

        # Print the results
        for row in results:
            print(row)

except Error as e:
    # Rollback in case of error
    if connection:
        connection.rollback()
    print(f"Error: {e}")

finally:
    # Ensure the cursor and connection are closed to free up resources
    if cursor:
        cursor.close()
    if connection and connection.is_connected():
        connection.close()