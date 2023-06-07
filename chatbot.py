import nltk
from nltk.corpus import stopwords
import random
import json
import requests
query = input("Enter your query")
tokens=nltk.word_tokenize(query)




#Preprocessing
stop_words = set(stopwords.words('english'))

filtered_sentence = [w for w in tokens if not w.lower() in stop_words]
#with no lower case conversion
filtered_sentence = []
 
for w in tokens:
    if w not in stop_words:
        filtered_sentence.append(w)




#Greetings
greeting_words = json.loads(open('greeting.txt', 'r').read())
def greet():
    print(random.choice(greeting_words))







#Farewell
farewell_words = json.loads(open('farewell.txt', 'r').read())
def farewell():
    print(random.choice(farewell_words))









#Ability
def get_ability():
    if (query.lower() == "what can you do"):
        capable = '''"I'm a travel chatbot designed to assist you with all things related to travel. Here's what I can do for you:

    1. Destination recommendations: Let me know your preferences, and I can suggest popular travel destinations based on your interests, budget, and travel dates.

    2. Flight and hotel search: I can help you find and compare flight options, check prices, and assist with hotel bookings for your desired destinations.

    3. Travel planning: Need assistance with creating itineraries or planning your trip? I can provide suggestions for attractions, landmarks, and activities to include in your travel plans.

    4. Local insights: Wondering about local customs, culture, or cuisine? I can offer insights and recommendations on local experiences to enhance your travel.

    5. Travel tips and advice: Whether it's packing tips, visa requirements, or safety guidelines, I'm here to provide useful information and advice to make your trip smooth.

    6. Weather updates: Curious about the weather conditions at your destination? I can provide real-time weather updates to help you prepare accordingly.

    7. Currency conversion: Need to convert currencies? Just let me know the amount and the currencies involved, and I'll assist you with the latest exchange rates.

    8. Language assistance: Traveling to a place with a different language? I can help with basic translations, common phrases, and language tips to facilitate communication.

    9. Local transportation: Looking for transportation options within your destination? I can provide information on public transportation, car rentals, and other local transport services.

    10. Travel inspiration: If you're looking for travel inspiration or want to explore new destinations, I can share travel stories, tips, and recommendations from fellow travelers.

    Feel free to ask me anything travel-related, and I'll do my best to assist you in planning a memorable trip!"'''
        print(capable)







#Get Weather
def get_weather():
   CITY = tokens[-1]
   BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
   # City Name CITY = "Hyderabad"
   # API key API_KEY = "Your API Key"
   # upadting the URL
   URL = BASE_URL + "q=" + CITY + "&appid=" + API_KEY
   # HTTP request
   response = requests.get(URL)
   # checking the status code of the request
   if response.status_code == 200:
      # getting data in the json format
      data = response.json()
      # getting the main dict block
      main = data['main']
      # getting temperature
      temperature = main['temp']
      # getting the humidity
      humidity = main['humidity']
      # getting the pressure
      pressure = main['pressure']
      # weather report
      report = data['weather']
      print(f"{CITY:-^30}")
      print(f"Temperature: {temperature}")
      print(f"Humidity: {humidity}")
      print(f"Pressure: {pressure}")
      print(f"Weather Report: {report[0]['description']}")
   else:
      # showing the error message
      print("Error in the HTTP request")









#Intent Recognition
import re

def get_intent(user_input):
    user_input = user_input.lower()

    # Define patterns and corresponding intents
    patterns = {
        r"(hello|hi|hey|howdy)": "greeting",
        r"(?:what can you do\??|(?:tell me your|what are your) abilit(?:y|ies))": "ability",
        r"(bye|goodbye|see you)": "farewell",
        r"(\b(?:search|find)\b.*)": "search",
        r"(\b(?:book|reserve)\b.*)": "booking",
        r"(\b(?:weather|forecast|climate)\b.*)": "weather",
        r"(\b(?:help|support)\b.*)": "help"
    }

    # Iterate over the patterns and check for matches
    for pattern, intent in patterns.items():
        if re.search(pattern, user_input):
            return intent
    
    # If no match is found, assume it as a general inquiry intent
    return "inquiry"

# Test the intent recognition function
intent = get_intent(query)
print("Intent:", intent)









#Conditional Function Invoke
match intent:
    case "greeting": greet()
    case "ability": get_ability()
    case "farewell": farewell()
    case "weather": get_weather()
    case _: greet()


