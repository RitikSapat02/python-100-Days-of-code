import smtplib 
import datetime as dt 
import random
from email.message import EmailMessage
import pandas

today = dt.datetime.now()
month = today.month
day = today.day

with open("birthdays.csv") as data_file:
    data = pandas.read_csv(data_file)
    data_list = data.to_dict(orient="records")
    
    for item in data_list:
        if item['month']==month and item['day']==day:
            my_email = "ritiksapat2@gmail.com"
            password = "pjcdgtllnmulgaek"
            receiver_email = item['email']
            receiver_name = item['name']


            with smtplib.SMTP('smtp.gmail.com') as connection:
                connection.starttls()
                connection.login(user=my_email,password=password)

                em = EmailMessage()
                em['Subject'] = 'Birthday wishes'
                em['From'] = my_email
                em['To'] = receiver_email

                file = f"letter_{random.randint(1,3)}.txt"
                with open(file) as data:
                    body = data.read().replace('[Name]',receiver_name)
               
                em.set_content(body)
            
                connection.sendmail(my_email,receiver_email,em.as_string())
