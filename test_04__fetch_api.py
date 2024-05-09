# requests installation
# python -m pip install requests
#
# api reference:
# https://open-meteo.com/en/docs

import requests

print("starting script")

lat = 44.88
lng = 11.05

api_path = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lng}&hourly=precipitation_probability"

# fetch data
response = requests.get(api_path)
print(response.json())