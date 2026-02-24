import os
import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv

load_dotenv()

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/93697e62e046e8072155653409168db3/flightDeals/prices"
SHEETY_USER_ENDPOINT = "https://api.sheety.co/93697e62e046e8072155653409168db3/flightDeals/users"

class DataManager:
    def __init__(self):
        self._user = os.environ.get("SHEETY_USER")
        self._pw = os.environ.get("SHEETY_PW")
        self._auth = HTTPBasicAuth(self._user, self._pw)
        self.destination_data = {}
        self.user_data = {}

    def get_destination_data(self):
        r_sheet_get = requests.get(url=f"{SHEETY_PRICES_ENDPOINT}", auth=self._auth)
        data_sheet = r_sheet_get.json()
        # print(data_sheet)
        self.destination_data = data_sheet["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            iata_code = {
                "price": {
                    "iataCode": city["iataCode"],
                }
            }
            r_prices_put = requests.put(url=f"{SHEETY_PRICES_ENDPOINT}/{city["id"]}", auth=self._auth, json=iata_code)
            # print(r_sheet_put.text)

    def get_user_emails(self):
        r_email_get = requests.get(url=f"{SHEETY_USER_ENDPOINT}", auth=self._auth)
        data_users = r_email_get.json()
        self.user_data = data_users["users"]
        return self.user_data
