import random
lista = []




class Auto:
    def __init__(self,rekisteritunnus,huippunopeus,tämänhetkinennopeus = 0,kuljettumatka = 0):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tämänhetkinennopeus = tämänhetkinennopeus
        self.kuljettumatka = kuljettumatka

    def kulje(self,tuntimäärä):
        self.kuljettumatka = self.kuljettumatka + self.tämänhetkinennopeus * tuntimäärä


    def kiihdytä(self):

        nopeudenmuutos = random.randint(-10, 15)
        self.tämänhetkinennopeus = self.tämänhetkinennopeus + nopeudenmuutos

        if self.tämänhetkinennopeus < 0:
            self.tämänhetkinennopeus = 0
        if self.tämänhetkinennopeus > self.huippunopeus:
            self.tämänhetkinennopeus = self.huippunopeus

class Kilpailu:

    def __init__(self,kilpailunimi,pituuskm,autot):
        self.kilpailunimi = kilpailunimi
        self.pituuskm = pituuskm
        self.autot = autot

    def tunti_kuluu(self):
        for i in self.autot:
            i.kiihdytä()
            i.kulje(1)


    def tulosta_tilanne(self):
        for i in self.autot:
            print(f"{i.rekisteritunnus:6} huippunopeus: {i.huippunopeus} tämänhetkinennopeus: {i.tämänhetkinennopeus:3} kuljettumatka: {i.kuljettumatka:4}")

    def kilpailu_ohi(self):
        for i in self.autot:
            if i.kuljettumatka >= self.pituuskm:
                return True
        return False


for i in range(1,11):
    x = random.randint(100,200)
    auto1 = Auto(f"ABC-{i}",x)
    lista.append(auto1)






kisa = Kilpailu("Suuri romuralli",8000,lista)

def peli():

    while True:
        for i in range(0,9):
            kisa.tunti_kuluu()
            if kisa.kilpailu_ohi() == True:
                return 0
        kisa.tulosta_tilanne()



peli()

kisa.tulosta_tilanne()

#print(type(kisa.autot[0].rekisteritunnus)) = str
#print(type(kisa.autot[0].huippunopeus)) = int
#print(type(kisa.autot[0].tämänhetkinennopeus)) = int
#print(type(kisa.autot[0].kuljettumatka)) = int

