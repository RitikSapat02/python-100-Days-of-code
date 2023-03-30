
from twilio.rest import Client
import requests

account_sid = 'AC3def83d1d91a8e3813925730b0756aeb'
auth_token = '4af61b9739318180b390ffd05bab24fc'
API_KEY = 'fd502c1b025cc0db92e8ba14b7ade1d1'
endpoint = 'http://api.weatherapi.com/v1/forecast.json'


parameters = {
    'q':'London',
    'key':'8c7b514dee264c7396f51913232203',
    'days':1,
    'aqi':'no',
    'alerts':'no'
   
}

response = requests.get(endpoint,params=parameters)

data = response.json()
weather_slice = data['forecast']['forecastday'][0]['hour'][7:19]

bad_weather = False
for hour_data in weather_slice:
    code = hour_data['condition']['code']
    if(code>1030):
        bad_weather = True

if(bad_weather):
    client = Client(account_sid, auth_token)
    message = client.messages \
                .create(
                     body="Its bad weather today! remember to get all necessary things like an umbrella",
                     from_='+14752553786',
                     to='+91 70571 35661'
                 )
    print(message.status)






# print(message.sid)

# message =  client.messages(
#         body = "",
#         from_ ="+91 70571 35661",
#         to="+91 70571 35661"
#     )