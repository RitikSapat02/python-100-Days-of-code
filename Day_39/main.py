#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from datetime import datetime,timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

ORIGIN_CITY_IATA = 'LON'

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
flight_search = FlightSearch()
notification_manager = NotificationManager()


if(sheet_data[0]['iataCode']==''):
    from flight_search import FlightSearch
    flight_search = FlightSearch()
    for row in sheet_data:
        row['iataCode'] = flight_search.get_iata_code(row['city'])

    data_manager.destination_data = sheet_data
    data_manager.update_destination_data()


tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days = 6 * 30)

for row in sheet_data:
    flight = flight_search.check_flights(ORIGIN_CITY_IATA,row['iataCode'],from_time = tomorrow,to_time = six_month_from_today)

    if flight is None:
        continue

    if flight.price < row['lowestPrice']:
        notification_manager.send_sms(text = f"LOW PRICE ALERT! ONLY {flight.price} to fly from {flight.origin_airport} to {flight.destination_airport},from {flight.out_date} to {flight.return_date}.")

