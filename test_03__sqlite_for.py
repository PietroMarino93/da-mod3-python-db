import sqlite3
import os
import datetime

print("starting script")

database_path = "my_database.db"

if os.path.exists(database_path):
  os.remove(database_path)
  print("removed old database")

# database connection (creation)
con = sqlite3.connect(database_path)
cur = con.cursor()

# table creation
cur.execute("CREATE TABLE my_table(id, creation_ts)")

# for loop
for x in range(5):
    t = datetime.datetime.now()
    cur.execute(f"INSERT INTO my_table VALUES ({x}, '{t}')")
    con.commit()

# print all entries
for row in cur.execute("SELECT * FROM my_table ORDER BY id"):
    print(row)