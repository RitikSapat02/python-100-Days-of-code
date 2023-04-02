from twilio.rest import Client
account_sid = 'AC3def83d1d91a8e3813925730b0756aeb'
auth_token = '85dbc779d1174ec13930433f6d266545'


class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    
    def send_sms(self,text):
        client = Client(account_sid, auth_token)
        message = client.messages.create( 
            body = text,
            from_ ='+14752553786',
            to = '+91 7057135661' 
            )
        print(message.status)