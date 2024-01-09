import requests
import json
from pandas import json_normalize

def get_user_input():
    return input("Enter the city name: ")

def fetch_places_in_city(city):
    url = f"https://api.foursquare.com/v3/places/search?&near=Mumbai&categories=16043"

    headers = {
        "accept": "application/json",
        "Authorization": "fsq3MNePWZGDo4U5qDFB+aL7olLWFp4SvvCbxbgAvUH5yFU="
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response
    else:
        print(f"Error: {response.status_code}, {response.text}")
        return None
    
def extract_name_and_address(data):
    if data:
        extracted_data = []
        for place in data.get("data", {}).get("places", []):
            name = place.get("name", "")
            address = place.get("address", "")
            extracted_data.append({"name": name, "address": address})
        return extracted_data
    else:
        return None

def pretty_print_json(data):
    if data:
        print(json.dumps(data, indent=2))
    else:
        print("No data to display.")

def filter_data(results):
    venues = results['response']['venues']

    # tranform venues into a pandas dataframe
    dataframe = json_normalize(venues)
    dataframe.head()


if __name__ == "__main__":
    city_name = get_user_input()
    places_data = fetch_places_in_city(city_name)
    filter_data(places_data)
