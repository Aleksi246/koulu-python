import json
import requests

try:
    vitsi = requests.get("https://api.chucknorris.io/jokes/random")
    if vitsi.status_code == 200:
        jsonvitsi = vitsi.json()

        print(jsonvitsi["value"])


except requests.exceptions.RequestException as e:
    print("virhe")