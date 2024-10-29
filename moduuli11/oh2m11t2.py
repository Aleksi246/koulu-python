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


class Sähköauto(Auto):

    def __init__(self,akkukapasiteetti,rekisteritunnus,huippinopeus,tämänhetkinennopeus = 0,kuljettumatka = 0):
        super().__init__(rekisteritunnus, huippinopeus,tämänhetkinennopeus,kuljettumatka)
        self.akkukapasiteetti = akkukapasiteetti

class Polttomoottoriauto(Auto):

    def __init__(self,tankkilitrat,rekisteritunnus,huippinopeus,tämänhetkinennopeus = 0,kuljettumatka = 0):
        super().__init__(rekisteritunnus,huippinopeus,tämänhetkinennopeus,kuljettumatka)
        self.tankkilitrat = tankkilitrat



auto1 = Sähköauto(52.5,"ABC-123",180)
auto2 = Polttomoottoriauto(32.3,"ACD-123",165)


for i in range(0,3):
    auto1.kiihdytä()
    auto2.kiihdytä()
    auto1.kulje(1)
    auto2.kulje(1)

print(f"{auto1.rekisteritunnus:6} huippunopeus: {auto1.huippunopeus} tämänhetkinennopeus: {auto1.tämänhetkinennopeus:3} kuljettumatka: {auto1.kuljettumatka:4} akkukapasiteetti: {auto1.akkukapasiteetti}")
print(f"{auto2.rekisteritunnus:6} huippunopeus: {auto2.huippunopeus} tämänhetkinennopeus: {auto2.tämänhetkinennopeus:3} kuljettumatka: {auto2.kuljettumatka:4} akkukapasiteetti: {auto2.tankkilitrat}")