import requests
import json 

endpoint = "http://localhost:8000/api/products/1/"

get_response = requests.get(endpoint) #http request used
print(get_response.json()) 

