import mysql.connector

# Establish a connection to the MySQL database
# Replace 'your_host', 'your_username', 'your_password', and 'your_database' with your actual database credentials
connection = mysql.connector.connect(
    host='your_host',
    user='your_username',
    password='your_password',
    database='your_database'
)

# Create a cursor object to interact with the database
cursor = connection.cursor()

# Define a simple query to retrieve data from a table
query = "SELECT * FROM classi LIMIT 5"

# Execute the query
cursor.execute(query)

# Fetch all the rows from the executed query
results = cursor.fetchall()

# Print the results
for row in results:
    print(row)

# Close the cursor and connection to free up resources
cursor.close()
connection.close()