# https://api.weatherapi.com/v1/current.json?key=80ff1e17baac455ab68163540233003&q=chennai

import requests

API_KEY = "80ff1e17baac455ab68163540233003"

city = input("Enter the name of the city\n").title()

BASE_URL = f"https://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}"



response = requests.get(BASE_URL)

data = response.json()

temp = data["current"]["temp_c"]
condition = (data["current"]["condition"]["text"]).lower()
print(f"The temperature of {city} in degrees is {temp} Degree Celsius, and the conditon is {condition}. ")

