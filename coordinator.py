import requests
import json
import time
import connection
from dotenv import dotenv_values

config = dotenv_values('.env')

print("Getting coordinates.")
time.sleep(2)
print(" ")

def fetch_coordinates(id):
    
    url = config['URL']
    
    params = {
        "svc": "core/search_item",
        "params": json.dumps({"id": id, "flags": "1025"}),
        "sid": connection.sid
    }    

    response = requests.post(url, params=params)

    if response.status_code == 200:
        data = response.json()
        if "error" in data:
            print("Retrieving data failed:", data["error"])
            return None
        else:
            x = data['item']['pos']['x']
            y = data['item']['pos']['y']
            print('x: ', x)
            print('y: ', y)
            print(" ")
    else:
        print("API request failed with status code:", response.status_code)
        return None
    
    time.sleep(5)
    fetch_coordinates(id)
    

    

fetch_coordinates(3813)