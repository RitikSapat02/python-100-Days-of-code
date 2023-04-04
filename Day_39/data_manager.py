import requests
from pprint import pprint

sheety_endpoint = 'https://api.sheety.co/2838d76744458ccd14366e0652966f6f/flightDeals/prices'


class DataManager:
    #This class is responsible for talking to the Google Sheet.

    def __init__(self):
        self.destination_data = {}
    
    def get_destination_data(self):
        #get data in sheet
        response = requests.get(url = sheety_endpoint)
        data = response.json()
        self.destination_data = data['prices']
        
        #priting data using pprint in a formatted way
        # pprint(data)
        return self.destination_data

    def update_destination_data(self):
        for row in self.destination_data:
            updated_row = {
                'price':{
                    'iataCode':row['iataCode']
                }
            }

        
            response = requests.put(url=f"{sheety_endpoint}/{row['id']}",json=updated_row)

            print(response.text)


