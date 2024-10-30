import json
import requests

paikka = input("paikkakunta: ")
apikey = "09ab3da31290908c1d9df35726424338"

pyynto = f"https://api.openweathermap.org/data/2.5/weather?q={paikka}&units=metric&appid={apikey}"

try:
    weather = requests.get(pyynto)
    if weather.status_code == 200:
        jsonweather = weather.json()
       # print(json.dumps(jsonweather, indent=2))
        print(jsonweather["weather"][0]["main"])
        print(jsonweather["weather"][0]["description"])
        print(f"{jsonweather["main"]["temp"]} celscius")
except requests.exceptions.RequestException as e:
    print("virhe")

#säätilan teksti ja lämpötila C
#main antaa säätilan description antaa kuvailun