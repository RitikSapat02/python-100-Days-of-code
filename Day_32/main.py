# # import smtplib
# import smtplib
# my_email = "ritiksapat2@gmail.com"
# password = "pjcdgtllnmulgaek"

# # # creates SMTP session
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     '''object of smtp class location of email provider's smtp server 
#     gmail = smtp.gmail.com
#     hotmail = smtp.live.com 
#     yahoo = smtp.mail.yahoo.com'''

#     # # start TLS for security
#     connection.starttls()
#     # transport layer security: way of securing our connection to our email server. so that way when we are sending email if somebody intercepts our email somewhwere along the line and try to read it so becaose this is(connection.starttls()) enable that mess would be encrypted and impossible fot them to read the content so it makes this connection secure

#     # # Authentication
#     connection.login(user = my_email,password=password)
#     # # message to be sent
#     message = "Subject:You are here\n\nThis is the body of my email."
#     # # sending the mail
#     connection.sendmail(my_email , "ritiksapat3@gmail.com",message)


# # import smtplib
# # from email.message import EmailMessage
# # import ssl 

# # sender = 'ritiksapat2@gmail.com'
# # email_password = 'pjcdgtllnmulgaek'
# # receiver = 'ritiksapat3@gmail.com'

# # sub ="check my chutiya"
# # body = """

# # This is a test message.
# # """
# # em = EmailMessage()
# # em['From'] = sender
# # em['To'] = receiver
# # em['Subject'] = sub
# # em.set_content(body)

# # context = ssl.create_default_context()

# # with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
# #     smtp.login(sender,email_password)
# #     smtp.sendmail(sender,receiver,em.as_string())


import datetime as dt 
import smtplib
import random

today = dt.datetime.now()
day_of_week = today.weekday()

my_email = "ritiksapat2@gmail.com"
password = "pjcdgtllnmulgaek"
receiver = 'ritiksapat3@gmail.com'

# with open("./quotes.txt",'r',encoding='utf-8') as quote_file:
#     all_quotes = quote_file.readlines()
#     quote = random.choice(all_quotes)

        
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user = my_email,password=password)
#     message = "This is the body of my email."
#     connection.sendmail(my_email , "ritiksapat3@gmail.com",message)

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user = my_email,password=password)
    message = "This is the body of my email."
    connection.sendmail(my_email , "ritiksapat3@gmail.com",message)
