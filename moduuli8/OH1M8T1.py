import mysql.connector


def testi(icao):
    sql = f"select name from airport where ident='{icao}'"
    print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    for i in tulos:
        print(i)
    return

yhteys = mysql.connector.connect(
    host="localhost",
    port= 3306,
    database="flight_game",
    user="user2",
    password="salasana",
    autocommit=True
)

ICAO = input("anna ICAO-koodi: ")
testi(ICAO)