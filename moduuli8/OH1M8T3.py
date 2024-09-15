import geopy
import mysql.connector
from geopy.distance import distance
"""
def latitude(icao):
    sql = f" select latitude_deg from airport where ident= '{icao}'"

    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()

    return tulos

def longitude (icao):
    sql = f" select longitude_deg from airport where ident= '{icao}'"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()

    return tulos

yhteys = mysql.connector.connect(
    host="localhost",
    port= 3306,
    database="flight_game",
    user="user2",
    password="salasana",
    autocommit=True
)

icao1 = input("anna ensimmäinen ICAO: ")
icao2 = input("anna toinen ICAO :")

paikka1 = (float(latitude(icao1)),float(longitude(icao1)))
paikka2 = (float(latitude(icao2)),float(longitude(icao2)))



print(paikka1)
print(paikka2)
print(type(paikka1))
print(type(latitude(icao1)))

print(distance(paikka1,paikka2))
"""


def lalo(icao):
    sql = f" select latitude_deg, longitude_deg from airport where ident= '{icao}'"

    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()

    return tulos


yhteys = mysql.connector.connect(
    host="localhost",
    port= 3306,
    database="flight_game",
    user="user2",
    password="salasana",
    autocommit=True
)

paikka1 = input("anna 1 ICOA: ")
paikka2 = input("anna 2 ICOA: ")

paikka1kord = lalo(paikka1)
paikka2kord = lalo(paikka2)
print(paikka1kord[0])
etaisyys = distance(paikka1kord[0],paikka2kord[0])
print(etaisyys)
