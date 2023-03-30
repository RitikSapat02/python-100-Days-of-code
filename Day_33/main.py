import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 21.152451 #your latitude
MY_LONG = 79.080559

MY_EMAIL = "ritiksapat2@gmail.com"
MY_PASSWORD = "pjcdgtllnmulgaek"

def is_iss_overhead():
    response = requests.get(url = 'http://api.open-notify.org/iss-now.json')
    response.raise_for_status()
    data = response.json()

    iss_longitude = float(data['iss_position']['longitude'])
    iss_latitude = float(data['iss_position']['latitude'])


    #your position is within +5 or -5 degrees of the ISS position
    if MY_LAT-5<=iss_latitude <= MY_LAT+5 and MY_LONG - 5 <=iss_latitude <=MY_LONG + 5:
        return True
    return False

def is_night():
    parameters = {
        "lat" : MY_LAT,
        "lng" : MY_LONG,
        'formatted':0,
    }
    response = requests.get('https://api.sunrise-sunset.org/json',params = parameters)
    response.raise_for_status()
    data=response.json()
    sunrise = int(data['results']['sunrise'].split('T')[1].split(':')[0])
    sunset = int(data['results']['sunset'].split('T')[1].split(':')[0])
    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True
    return False



#If the ISS is close to my current positon
#and it is currently dark
#then send me an email to tell me to look up.
#BONUS: run the code every 60 seconds.

while(True):
    time.sleep(60)
    if is_iss_overhead() and is_night():
        connection = smtplib.SMTP("smtp@gmail.com")
        connection.starttls()
        connection.login(MY_EMAIL,MY_PASSWORD)

        connection.sendmail(MY_EMAIL,'ritiksapat3@gmail.com',msg="SUbject:Look UP\n\nThe ISS is above you in the sky.")
