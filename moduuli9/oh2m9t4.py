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

        nopeudenmuutos = random.randint(-10,15)
        self.tämänhetkinennopeus = self.tämänhetkinennopeus + nopeudenmuutos

        if self.tämänhetkinennopeus < 0:
            self.tämänhetkinennopeus = 0
        if self.tämänhetkinennopeus > self.huippunopeus:
            self.tämänhetkinennopeus = self.huippunopeus


for i in range(1,11):
    x = random.randint(100,200)
    auto1 = Auto(f"ABC-{i}",x)
    lista.append(auto1)

def kisa():
    while True:
        for i in lista:
            i.kiihdytä()
            i.kulje(1)
            if i.kuljettumatka >= 10000:
                return 0



kisa()
for i in lista:
    print(f"{i.rekisteritunnus} {i.huippunopeus} {i.tämänhetkinennopeus} {i.kuljettumatka}")

