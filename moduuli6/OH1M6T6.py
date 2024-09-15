import math

def europerpitsaneliömetri(pitsa:float,euro:float) -> float:
    pitsa_ala_neliometreinä = (((pitsa/2) * 0.01)**2)*math.pi
    europerpitsa = euro/pitsa_ala_neliometreinä

    return europerpitsa

pitsa1 = float(input("anna ensimmäisen pitsan halkaisija senttimetreinä: "))
hinta1 = float(input("anna ensimmäisen pitsan hinta euroina: "))
pitsa2 = float(input("anna toisen pitsan halkaisija senttimetreinä: "))
hinta2 = float(input("anna toisen pitsan hinta euroina: "))

arvo1 = europerpitsaneliömetri(pitsa1,hinta1)
arvo2 = europerpitsaneliömetri(pitsa2,hinta2)
if arvo1 < arvo2:
    print("ensimmäinen pitsa on parempi vastike rahalle")
if arvo1 == arvo2:
    print("molemmat pitsat antavat saman vastikkeen rahalle")

if arvo1 > arvo2:
    print("toinen pitsa on parempi vastike rahalle")