

class Auto:
    def __init__(self,rekisteritunnus,huippunopeus,tämänhetkinennopeus = 0,kuljettumatka = 0):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tämänhetkinennopeus = tämänhetkinennopeus
        self.kuljettumatka = kuljettumatka





    def kiihdytä(self, nopeudenmuutos):

        self.tämänhetkinennopeus = self.tämänhetkinennopeus + nopeudenmuutos

        if self.tämänhetkinennopeus < 0:
            self.tämänhetkinennopeus = 0
        if self.tämänhetkinennopeus > self.huippunopeus:
            self.tämänhetkinennopeus = self.huippunopeus



auto1 = Auto("ABC-123",142)

auto1.kiihdytä(30)
auto1.kiihdytä(50)
auto1.kiihdytä(70)

print(f"{auto1.tämänhetkinennopeus}")

auto1.kiihdytä(-200)

print(f"{auto1.tämänhetkinennopeus}")

print(f"{auto1.rekisteritunnus} {auto1.huippunopeus} {auto1.tämänhetkinennopeus} {auto1.kuljettumatka}")