
'''# The best way to succeed in this world is to act on the advice you give to others.'''
#send motivational quotes on monday
import datetime as dt 
import smtplib
import random
from email.message import EmailMessage

today = dt.datetime.now()
day_of_week = today.weekday()



if day_of_week==5:
    with open("./quotes.txt",'r',encoding='utf-8') as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)


    my_email = "ritiksapat2@gmail.com"
    password = "pjcdgtllnmulgaek"
    receiver = 'ritiksapat3@gmail.com'
            
    
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls() 
        connection.login(user = my_email,password=password)

        sub ="monday Motivation"
        body = quote
        em = EmailMessage()
        em['From'] = my_email
        em['To'] = receiver
        em['Subject'] = sub
        em.set_content(body)
        connection.sendmail(my_email , "ritiksapat3@gmail.com",em.as_string())
