import requests
from pprint import pprint

from flight_data import FlightData
TEQUILA_ENDPOINT = 'https://api.tequila.kiwi.com'
TEQUILA_APIKEY = 'j2m9sl1UDJJ9Mx_xg36jYMJshuVrcTGW'



class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    
    def get_iata_code(self,city_name):
        location_endpoint = f"{TEQUILA_ENDPOINT}/locations/query"
        header =  {
            'apikey':TEQUILA_APIKEY
        }
        parameters = {
            'term':city_name,
            'location-types':'city'
        }

        response = requests.get(url=location_endpoint,params=parameters,headers=header)

        result = response.json()['locations']
        code = result[0]['code']
        return code

    def check_flights(self,origin_city_code,destination_city_code,from_time,to_time):
        headers = {
            'apikey':TEQUILA_APIKEY
        }

        query={
            'fly_from':origin_city_code,
            'fly_to':destination_city_code,
            'date_from':from_time.strftime("%d/%m/%Y") ,
            'date_to':to_time.strftime('%d/%m/%Y'),
            'nights_in_dst_from':7,
            "nights_in_dst_to":28,
            'flight_type':'round',
            'one_for_city':1,
            'curr':'GBP',
            'max_stopovers':0

        }

        response = requests.get(url = f"{TEQUILA_ENDPOINT}/v2/search",params = query,headers=headers)

        try:
            data = response.json()["data"][0]
           
        except IndexError:

            query['max_stopovers']=1
            response = requests.get(url = f"{TEQUILA_ENDPOINT}/v2/search", params = query,headers = headers)
            try:
                data = response.json()['data'][0]
                
            except IndexError:
                print(f"No flights found for {destination_city_code}.")
                return None   
            
            else:

                flight_data = FlightData(price=data['price'],origin_city=data['route'][0]['cityFrom'],origin_airport=data['route'][0]["flyFrom"],destination_city=data['route'][1]['cityTo'],destination_airport=data['route'][1]["flyTo"],out_date=data['route'][0]['local_departure'],return_date=data['route'][2]['local_departure'],stop_overs=1,via_city=data['route'][0]['cityTo'])
                return flight_data 
        
        else:
            flight_data = FlightData(price=data['price'],origin_city=data['route'][0]['cityFrom'],origin_airport=data['route'][0]["flyFrom"],destination_city=data['route'][0]['cityTo'],destination_airport=data['route'][0]["flyTo"],out_date=data['route'][0]['local_departure'],return_date=data['route'][1]['local_departure'])
            return flight_data 