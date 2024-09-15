import mysql.connector

def testi(maakoodi):
    sql = f" select distinct(type),count(name) over (partition by type) from airport where iso_country = '{maakoodi}'"
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

maakoodi = input("maakoodi: ")
testi(maakoodi)