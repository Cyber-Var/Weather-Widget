import requests
import json


# Get IP address:
ip = requests.get('https://checkip.amazonaws.com').text

# Get latitude and longitude from IP address:
request_url = 'https://geolocation-db.com/jsonp/' + ip
response = requests.get(request_url)
result = response.content.decode()
result = result.split("(")[1].strip(")")
result = json.loads(result)
latitude = result['latitude']
longitude = result['longitude']

# Get location key using latitude and longitude:
location_url = "http://dataservice.accuweather.com/locations/v1/cities/geoposition/search?apikey=l1xeuPlkJkMUnQOTQWkUn4W3eJ8arGWG&q={}%2C{}".format(latitude, longitude)
location = requests.get(location_url)
location_data = location.json()
location_key = location_data['Key']

# Get current weather data using location key:
forecast_url = "http://dataservice.accuweather.com/currentconditions/v1/{}?apikey=l1xeuPlkJkMUnQOTQWkUn4W3eJ8arGWG".format(location_key, latitude, longitude)
forecast = requests.get(forecast_url)
forecast_data = forecast.json()

# Print weather data:
print(json.dumps(forecast_data, indent=4, sort_keys=True))

# API key:
''' 
API key:         l1xeuPlkJkMUnQOTQWkUn4W3eJ8arGWG 
'''