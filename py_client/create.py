import requests
import json 


headers = {'Authorization': 'Bearer 1cba07d1e053043a4e0da72f21666d221f0810d8'}
endpoint = "http://localhost:8000/api/products/"
#  "http://localhost:8000/admin/
#  session -> post data
# selenium

data  = {
    "title":"car",
    "content":"jdm",
    "price": 400
}
get_response = requests.post(endpoint, json=data, headers=headers) #http request used
# get_response = requests.post(endpoint) #http request used
print(get_response.json()) 

