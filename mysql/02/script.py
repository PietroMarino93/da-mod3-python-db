import mysql.connector
from mysql.connector import Error

try:
    # Establish a connection to the MySQL database
    connection = mysql.connector.connect(
        host='your_host',
        user='your_username',
        password='your_password',
        database='your_database'
    )

    if connection.is_connected():
        # Create a cursor object to interact with the database
        cursor = connection.cursor()

        # Define a query to insert data into the table
        insert_query = "INSERT INTO your_table (column1, column2) VALUES (%s, %s)"
        values = [
            ('value1_1', 'value1_2'),
            ('value2_1', 'value2_2'),
            ('value3_1', 'value3_2')
        ]

        # Execute the insert query for multiple rows
        cursor.executemany(insert_query, values)

        # Commit the transaction
        connection.commit()
        print("Data inserted successfully")

        # Query to verify the inserted data
        select_query = "SELECT * FROM your_table"
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