import json

from flask import Flask, request, Response

def isprime(number):
    for i in range(2, int(number/2)):
        if number % i != 0:
            continue
        else:
            return False

    return True

app = Flask(__name__)

@app.route('/primecheck/<luku>')
def primecheck(luku):

    try:

        luku = int(luku) #http://127.0.0.1:3000/primecheck/13

        arvo = isprime(luku)

        tilakoodi = 200
        vastaus ={
            "tilakoodi":tilakoodi,
            "luku":luku,
            "isprime":arvo


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