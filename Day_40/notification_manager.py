from twilio.rest import Client
import smtplib

my_email = "ritiksapat2@gmail.com"
password = "pjcdgtllnmulgaek"

account_sid = 'AC3def83d1d91a8e3813925730b0756aeb'
auth_token = '61d2fbb980470f97a7d90ad4810db281'


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

    def send_emails(self,emails,text,link):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email,password=password)

            for email in emails:
                connection.sendmail(my_email,email,msg=f"Subject:New Low Price Flight!\n\n{text}\n{link}".encode('utf-8'))