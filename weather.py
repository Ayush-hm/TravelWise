import requests
def get_weather(tokens):
   CITY = tokens[-1]

   url = "https://weather-by-api-ninjas.p.rapidapi.com/v1/weather"
   querystring = {"city":CITY}
   headers = {
	   "X-RapidAPI-Key": "0d439840f2msh881603f7327d99ap134d44jsn6addd9c2e1fa",
	   "X-RapidAPI-Host": "weather-by-api-ninjas.p.rapidapi.com"
   }
   response = requests.get(url, headers=headers, params=querystring)

   # checking the status code of the request
   if response.status_code == 200:
      # getting data in the json format
      data = response.json()
      
      # getting temperature
      temperature = data['temp']
      # getting the humidity
      humidity = data['humidity']
      # getting the pressure
      feelslike = data['feels_like']
      # getting the wind speed
      windspeed = data['wind_speed']
      # getting min and max temperature
      mintemp = data['min_temp']
      maxtemp = data['max_temp']
      # getting the cloud cover
      cloudcover = data['cloud_pct']
      print(f"{CITY:-^30}")
      print(f"Temperature: {temperature}")
      print(f"Feels Like: {feelslike}")
      print(f"Minimum Temperature: {mintemp}")
      print(f"Maximum Temperature: {maxtemp}")      
      print(f"Humidity: {humidity}")
      print(f"Wind Speed: {windspeed}")
      print(f"Percentage of cloud cover: {cloudcover}")
      # print(f"Weather Report: {report[0]['description']}")
   else:
      # showing the error message
      print("Error in the HTTP request")