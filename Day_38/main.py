import requests
from datetime import datetime

API_KEY = 'b3adf7b69857213248b7598cd5320641'
API_ID = 'ad7e7029'

exercise_endpoint = 'https://trackapi.nutritionix.com/v2/natural/exercise'
sheety_endpoint = 'https://api.sheety.co/2838d76744458ccd14366e0652966f6f/myWorkouts/workouts'

params = {
    'query':input("Bol: "),
    'gender':'male',
    'weight_kg':60,
    'height_cm':185,
    'age':21,
}


headers = {
    'x-app-id':API_ID,
    'x-app-key':API_KEY
}

response = requests.post(url=exercise_endpoint,json=params,headers=headers)
result = response.json()['exercises']


today = datetime.now()

for exercise in result:
    DATE = today.strftime('%d/%m/%Y')
    TIME = today.now().strftime('%X')
    NAME_EXERCISE = exercise['name'].title()
    DURATION = exercise['duration_min']
    CALORIES = exercise['nf_calories']

    params_sheety = {

        'workout': {
            'exercise':NAME_EXERCISE,
            'duration':DURATION,
            'calories':CALORIES,
            'date':DATE,
            'time':TIME
            }
    }

    ##bsic authentication
    # sheety_response = requests.post(url=sheety_endpoint,json=params_sheety,auth=(
    #     'ritik','sdvsdvsdvsdvsdvsdgerg'
    # ))
    

    ##bearer token authentication
    Token = 'svdvfddvdf'
    bearer_headers = {
        'Authorization':f"Bearer {Token}"
    }

    sheety_response = requests.post(url=sheety_endpoint,json=params_sheety,headers = bearer_headers)

    print(sheety_response.text)