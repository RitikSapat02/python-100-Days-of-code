import requests
from datetime import date

USERNAME = "ritiksapat"
TOKEN = 'shds0dvsdv8sd'
GRAPH_ID = 'graph1'

pixela_endpoint = 'https://pixe.la/v1/users'

user_params = {
    "token":TOKEN,
    "username":USERNAME,
    "agreeTermsOfService":'yes',
    'notMinor':'yes',

}

'''below code run only for one time to create user'''
# response = requests.post(url=pixela_endpoint,json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

greaph_config = {
    "id":GRAPH_ID,
    "name":"Reading Graph",
    "unit":'pages',
    "type":"int",
    "color":"ajisai"
}

headers = {
    "X-USER-TOKEN":TOKEN
}

'''below code run only for one time to create graph'''
# response = requests.post(url=graph_endpoint,json=greaph_config,headers=headers)

# print(response.text)


'''POSTING DATA'''

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = date.today().strftime("%Y%m%d")

# print(today.strftime("%Y%m%d"))
# str(date.today()).replace('-','')

pixel_data = {
    'date':today,
    'quantity':input("How many pages did you read today?"),
}

response = requests.post(url=pixel_creation_endpoint,json=pixel_data,headers=headers )
print(response.text)



'''updating pixel'''
update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{date(2023,3,23).strftime('%Y%m%d')}"

new_pixel_data = {
    "quantity":'19'
}
# response = requests.put(url=update_endpoint,json=new_pixel_data,headers=headers)




'''delete pixel'''
delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{date(2023,3,23).strftime('%Y%m%d')}"

# response = requests.delete(url=delete_endpoint,headers=headers)
# print(response.text)