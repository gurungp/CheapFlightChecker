

import pprint
from datetime import timedelta
from notification_manager import NotificationManager
from data_manager import DataManager
from flight_search import FlightSearch

PHONE_NUM_FROM = "PHONE NUMBER HERE"
PHONE_NUM_TO = "SOME PHONE NUMBER"

notification = NotificationManager()
flight = FlightSearch()

sheety = DataManager()
sheetyJSON = sheety.get().json()  # all the values received and converted to JSON which is Dictionary
sheetyDict = sheetyJSON["prices"]  # value inside prices are list with required data from the rows and column

tomorrow = flight.tomorrow
six_months_away = tomorrow + timedelta(days=180)
return_date_from = six_months_away + timedelta(days=7)
return_date_to = return_date_from + timedelta(days=28)

def update_iataCode(dictFromSheety):
    for data in dictFromSheety:
        iata_code = flight.get_desitination_code(data["city"])
        data["iataCode"] = iata_code
        new_data = {"price": {"iataCode": iata_code}}
        response = sheety.put(data["id"], new_data)
def get_prices_from(dictFromSheety):
    dict={}
    for data in dictFromSheety:
        destination = data["iataCode"]
        result = flight.search_flights(destination,tomorrow,six_months_away,return_date_from,return_date_to)["data"][0]
        print(f"City : {result['cityTo']}  -  Price : {result['price']}")
        dict[result["cityTo"]] = result["price"]

    return dict

def check_if_price_lower():
    dict_result = get_prices_from(sheetyDict)
    pp = pprint.PrettyPrinter(width=150)
    for data_sheety,data_tequila in zip(sheetyDict,dict_result):
        pp.pprint(f"{data_sheety['city']} : {data_sheety['lowestPrice']}")
        pp.pprint(f"{data_tequila} : {dict_result[data_tequila]}")
        if (dict_result[data_tequila]) <= (data_sheety['lowestPrice']):
            message = f"Price for {data_tequila} is lower at {dict_result[data_tequila]} EUR"
            notification.send_message(PHONE_NUM_FROM,PHONE_NUM_TO,message)


check_if_price_lower()




