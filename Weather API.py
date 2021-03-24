import requests
import pandas as pd
import io
import json

url = "https://community-open-weather-map.p.rapidapi.com/weather"

querystring = {"q":"Kildare, Ireland","lat":"53.0853","lon":"-6.82","callback":"test","id":"2172797","lang":"English","units":"metric","mode":"xml, html"}

headers = {
    'x-rapidapi-key': "d04bf6eff3msh485cf1280775583p124e0ejsn9b0d7e8ac469",
    'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com"
    }
# Request data from open weather data
response = requests.request("GET", url, headers=headers, params=querystring)
data = response.text
print(response.text)

