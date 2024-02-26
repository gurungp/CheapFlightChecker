import requests
import pprint
from datetime import datetime,timedelta

API_KEY = "3Sq4fS3WOO8FCKZR4j5dpCU-7EI2wf2Z"
ENDPOINT = "https://api.tequila.kiwi.com"

class FlightSearch:
    def __init__(self,api_key=API_KEY,endpoint=ENDPOINT):
        self.api_key = api_key
        self.endpoint = endpoint
        self.header = {
            "apikey" : API_KEY
        }
        self.today = datetime.now()
        self.tomorrow = (datetime.now() + timedelta(days=1))

    def get_desitination_code(self,city_name):
        query = {
            "term": city_name,
            "location_types": "city"
        }
        response = requests.get(f"{ENDPOINT}/locations/query",headers=self.header,params=query)
        code = response.json()["locations"][0]["code"]
        return code
    def search_flights(self,destination,depart_date_from,depart_date_to,return_date_from,return_date_to):
        query = {
            "fly_from" : "LON",
            "fly_to" : destination,
            "date_from" : depart_date_from.strftime("%d/%m/%Y"),
            "date_to" : depart_date_to.strftime("%d/%m/%Y"),
            "return_from" : return_date_from.strftime("%d/%m/%Y"),
            "return_to": return_date_to.strftime("%d/%m/%Y"),
            "curr" : "EUR",
            "max_stopovers" : 2 # 0 for direct flights
        }
        response = requests.get(f"{ENDPOINT}/v2/search", headers=self.header, params=query)
        return response.json()


