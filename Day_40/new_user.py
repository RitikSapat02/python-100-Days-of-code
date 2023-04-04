import requests
sheety_User_endpoint = 'https://api.sheety.co/2838d76744458ccd14366e0652966f6f/flightDeals/users'

print("Welcome to Angela's Flight Club.\nWe find the best flight deals and email you.")

f_name = input("What is your first name?")
l_name = input("What is your last name?")
email = input("What is your Email?")
confirm_email = input("Type your email again.")

if(email==confirm_email):
    print("You're in the club!")
    data = {
        'user':{
            "firstName":f_name,
            "lastName":l_name,
            'email':email
        }
    }

    response = requests.post(url=sheety_User_endpoint,json=data)