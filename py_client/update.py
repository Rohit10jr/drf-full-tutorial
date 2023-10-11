import requests
import json 

endpoint = "http://localhost:8000/api/products/1/update/"

data = {
    "title": "hello rohit",
    "content": "jawan is flop"
}
get_response = requests.put(endpoint, json=data) #http request used
print(get_response.json()) 

