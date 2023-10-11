import requests
import json 

# endpoint = "https://httpbin.org/status/200/" 
# endpoint = "https://httpbin.org/anything"
# endpoint = "http://127.0.0.1:8000/"
endpoint = "http://localhost:8000/api/"

get_response = requests.post(endpoint, json={"title":None, "content": 123}) #http request used to scrape
# print(get_response.headers)
# print(get_response.text) # print raw html
# print(get_response.status_code)

# http request -> html
# rest api http request -> json
# print(get_response.json()['message'])
# print(get_response.json())
# print(get_response.status_code)

