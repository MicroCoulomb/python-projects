from data_manager import DataManager
from flight_data import FlightData, find_cheapest_flight
from flight_search import FlightSearch
from notification_manager import NotificationManager
import time
from datetime import datetime, timedelta
from notification_manager import NotificationManager

ORIGIN_CITY_IATA = "MNL"

FORMS_LINK = "https://docs.google.com/forms/d/e/1FAIpQLSfQmF5NSb2vX5HcP47qcO0VkzMUsESLQJp9nAmWp_vXduOAAQ/viewform?usp=publish-editor"

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
flight_search = FlightSearch()

# update IATA codes
for row in sheet_data:
    if row["iataCode"] == "":
        row["iataCode"] = flight_search.search_iata(row["city"])
        time.sleep(2)
# print(destination_data)

data_manager.destination_data = sheet_data
data_manager.update_destination_codes()

user_data = data_manager.get_user_emails()
user_email_list = [row["emailAddress"] for row in user_data]

# check flights window
tomorrow = datetime.today() + timedelta(days=1)
six_months_from_today = datetime.today() + timedelta(days=(6*30))
notification_manager = NotificationManager()

for destination in sheet_data:
    print(f"Getting flights for {destination['city']}...")
    flights = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_months_from_today
    )
    cheapest_flight = find_cheapest_flight(flights)
    print(f"{destination['city']}: PHP{cheapest_flight.price}")

    time.sleep(2)

    if cheapest_flight.price == "N/A":
        print(f"No direct flight to {destination['city']}. Looking for indirect flights...")
        stopover_flights = flight_search.check_flights(
            ORIGIN_CITY_IATA,
            destination["iataCode"],
            from_time=tomorrow,
            to_time=six_months_from_today,
            is_direct=False
        )
        cheapest_flight = find_cheapest_flight(stopover_flights)
        print(f"Cheapest indirect flight price is: PHP{cheapest_flight.price}")

    if cheapest_flight.price != "N/A" and cheapest_flight.price < destination["lowestPrice"]:
        # SMS MESSAGE SINGULAR
        # print(f"Lower price flight found to {destination['city']}!")
        #
        # notification_manager.send_whatsapp(
        #     message_body= f"Low price alert! Only £{cheapest_flight.price} to fly "
        #                  f"from {cheapest_flight.origin_airport} to {cheapest_flight.destination_airport}, "
        #                  f"on {cheapest_flight.out_date} until {cheapest_flight.return_date}."
        # )

        # EMAIL MULTIPLE
        if cheapest_flight.stops == 0:
            message = (f"Low price alert! Only PHP{cheapest_flight.price} to fly from {cheapest_flight.origin_airport} "
                       f"to {cheapest_flight.destination_airport} on {cheapest_flight.out_date} "
                       f"until {cheapest_flight.return_date}.")

        else:
            message = (f"Low price alert! Only PHP{cheapest_flight.price} to fly from {cheapest_flight.origin_airport} "
                       f"to {cheapest_flight.destination_airport} with {cheapest_flight.stops} stop(s) "
                       f"on {cheapest_flight.out_date} until {cheapest_flight.return_date}.")

        notification_manager.send_emails(user_email_list, message)