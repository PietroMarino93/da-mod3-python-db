import sqlite3
import os
import requests

print("starting script")

lat = 44.88
lng = 11.05

database_path = f"weather_location_latitude_{lat}_longitude_{lng}.db"
api_path = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lng}&hourly=temperature_2m,relativehumidity_2m"

# remove old database if exists
if os.path.exists(database_path):
  os.remove(database_path)
  print("removed old database")

# database connection (creation)
con = sqlite3.connect(database_path)
cur = con.cursor()

# table creation
cur.execute("CREATE TABLE my_table(id, time, temperature_2m)")

# fetch data
response = requests.get(api_path)

# save data
for i in range(len(response.json()["hourly"]["time"])):
    time = response.json()["hourly"]["time"][i]
    temperature_2m = response.json()["hourly"]["temperature_2m"][i]

    cur.execute(f"INSERT INTO my_table VALUES ({i}, '{time}', '{temperature_2m}')")
    con.commit()