import requests
import os
from datetime import datetime
from dotenv import load_dotenv
from amadeus import Client

load_dotenv()

CITY_DATA_ENDPOINT = "https://test.api.amadeus.com/v1/reference-data/locations/cities"
FLIGHT_ENDPOINT = "https://test.api.amadeus.com/v2/shopping/flight-offers"
TOKEN_ENDPOINT = "https://test.api.amadeus.com/v1/security/oauth2/token"

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self._api_key = os.environ.get("FLIGHT_API_KEY")
        self._api_secret = os.environ.get("FLIGHT_API_SECRET")
        self._token = self._get_new_token()
        # self.search_iata("Paris")

    def _get_new_token(self):
        header = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        body = {
            'grant_type': 'client_credentials',
            'client_id': self._api_key,
            'client_secret': self._api_secret,
        }

        r_flight_api = requests.post(url=TOKEN_ENDPOINT, headers=header, data=body)
        print(f"Your token is {r_flight_api.json()['access_token']}")
        print(f"Your token expires in {r_flight_api.json()['expires_in']} seconds")
        return r_flight_api.json()['access_token']

    def search_iata(self, city_name: str):
        header = {
            "Authorization": f"Bearer {self._token}"
        }
        params = {
            "keyword": city_name,
            "max": 1,
            "include": "AIRPORTS"
        }

        r_city_get = requests.get(url=CITY_DATA_ENDPOINT, headers=header, params=params)
        data_city = r_city_get.json()
        # print(data_city)
        try:
            code = data_city["data"][0]['iataCode']
        except IndexError:
            print("Index Error N/A")
            return "N/A"
        except KeyError:
            print("KeyError not found")
            return "not found"
        return code

    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time, is_direct=True):
        headers = {"Authorization": f"Bearer {self._token}"}
        query = {
            "originLocationCode": origin_city_code,
            "destinationLocationCode": destination_city_code,
            "departureDate": from_time.strftime("%Y-%m-%d"),
            "returnDate": to_time.strftime("%Y-%m-%d"),
            "adults": 1,
            "nonStop": "true" if is_direct else "false",
            "currencyCode": "PHP",
            "max": "10",
        }

        r_flights_get = requests.get(
            url=FLIGHT_ENDPOINT,
            headers=headers,
            params=query,
        )

        if r_flights_get.status_code != 200:
            print(f"check_flights() response code: {r_flights_get.status_code}")
            print("Response body:", r_flights_get.text)
            return None

        return r_flights_get.json()