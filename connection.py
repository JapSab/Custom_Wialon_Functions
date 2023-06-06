import requests
import json
import time
from dotenv import dotenv_values

config = dotenv_values('.env')

def authenticate_wialon():
    
    url = config['URL']

    params = {
        "svc": "token/login",
        "params": json.dumps({
        "token": config['TOKEN']
        })
    }

    response = requests.post(url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        if "error" in data:
            print("Authentication failed:", data["error"])
            return None
        else:
            sid = data["eid"]
            return sid
    else:
        print("API request failed with status code:", response.status_code)
        return None

sid = authenticate_wialon()

if sid is not None:
    print("Authentication successful!")
    print("SID:", sid)
    time.sleep(2)

