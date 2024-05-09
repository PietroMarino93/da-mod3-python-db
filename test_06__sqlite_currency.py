# api reference: https://freeforexapi.com/Home/Api

import sqlite3
import os
import requests
import time

print("starting script")

pair = "EURUSD"

database_path = f"currency_{pair}.db"
api_path = f"https://www.freeforexapi.com/api/live?pairs={pair}"

# remove old database if exists
if os.path.exists(database_path):
  os.remove(database_path)
  print("removed old database")

# database connection (creation)
con = sqlite3.connect(database_path)
cur = con.cursor()

# table creation
cur.execute("CREATE TABLE currency_value(id, pair, rate)")

id = 0

# save data
while True:
    # fetch data
    response = requests.get(api_path)
    current_rate = response.json()["rates"][pair]["rate"]

    print(f"current {pair} rate is: {current_rate}")

    cur.execute(f"INSERT INTO currency_value VALUES ({id}, '{pair}', {current_rate})")
    con.commit()

    id += 1

    time.sleep(2)