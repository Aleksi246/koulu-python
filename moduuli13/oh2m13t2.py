import json

from flask import Flask, request, Response

import mysql.connector


yhteys = mysql.connector.connect(
    host="localhost",
    port= 3306,
    database="flight_game",
    user="user2",
    password="salasana",
    autocommit=True
)

def testi(icao):
    sql = f"select name,municipality from airport where ident='{icao}'"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()

    return tulos



app = Flask(__name__)

@app.route('/kenttä/<icao>')
def kentta(icao):

    try:

        #http://127.0.0.1:3000/kenttä/EFKH
        info = testi(icao)
        nimi = info[0][0]
        munipicapyty = info[0][1]

        tilakoodi = 200
        vastaus ={
            "ICAO":icao,
            "Name":nimi,
            "munipicaty":munipicapyty

        }


    except ValueError:

        tilakoodi = 400
        vastaus = {
            "tilakoodi":tilakoodi,
            "kuvaus": "virhe"
        }

    json_vastaus = json.dumps(vastaus)
    return Response(response=json_vastaus, status=tilakoodi, mimetype='application/json')

@app.errorhandler(404)
def not_found(error):
    vastaus = {
        "tilakoodi":"404",
        "kuvaus": "polussa virhe"

    }
    json_vastaus = json.dumps(vastaus)
    return Response(response=json_vastaus, status=404, mimetype='application/json')

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)