##IMPORT LIBRARIES

import requests
from datetime import date,timedelta
from twilio.rest import Client

##DECALRE CONSTANTS
STOCK_ENDPOINT = 'https://www.alphavantage.co/query'
API_KEY = '0FXGHWBOULI49B6H'
NEWS_API_KEY = 'eb50a7abc9d2491f82effe32e8000de7'
NEWS_ENDPOINT = 'https://newsapi.org/v2/everything'
STOCK_NAME = 'TSLA'
COMPANY_NAME = 'Tesla Inc'
account_sid = 'AC3def83d1d91a8e3813925730b0756aeb'
auth_token = '4af61b9739318180b390ffd05bab24fc'

##SEND REQUEST
parameters = {
    'symbol':STOCK_NAME,
    'apikey':API_KEY,
    'function':'TIME_SERIES_DAILY_ADJUSTED',
}
response = requests.get(STOCK_ENDPOINT,params=parameters)
data = response.json()["Time Series (Daily)"]

##FETCH DATA 
'''WAY_01:-
converting all data into list of dictionaries'''
# data_list = [value for (key,value) in data.items()]
# yesterday_data = data_list[0]
# day_before_yesterday_data= data_list[1]

'''WAY_02:-
finding yesterday and day before yesterdays date and based on that calling keys'''

today = date.today()
yesterday = str(today - timedelta(days = 1))
day_before_yesterday = str(today-timedelta(days=2))
yesterday_data = data[yesterday]
day_before_yesterday_data = data[day_before_yesterday]

##DIFFRENCE BETWEEN PRICES OF YESTERDAY AND DAY_BEFORE_YESTERDAY
yesterday_closing_price = yesterday_data['4. close']
day_before_yesterday_closing_price = day_before_yesterday_data['4. close']

difference =  float(yesterday_closing_price) - float(day_before_yesterday_closing_price)
up_down = None
if difference > 0:
    up_down = '🔺'
else:
    up_down = '🔻'

##PERCENTAGE DIFFERENCE
diff_percent = round((difference/float(yesterday_closing_price)) * 100)

##IF PERCENTAGE GREATER THAN 5 get news
if abs(diff_percent) > 2:

    news_params = {
        'apikey':NEWS_API_KEY,
        'q': COMPANY_NAME,
    }
    news_response = requests.get(NEWS_ENDPOINT,params=news_params)
    articles = news_response.json()['articles']
    three_articles = articles[:3]
    print(len(three_articles))

    formatted_articles = [f"{STOCK_NAME}: {up_down}{diff_percent}\n\nHeadline: {article['title']}. \n\nBrief: {article['description']}" for article in three_articles]

    client = Client(account_sid, auth_token)
    for article in formatted_articles:
        message = client.messages.create(
                        body=article,
                        from_='+14752553786',
                        to='+91 70571 35661'
                    )
        print(message.status)

