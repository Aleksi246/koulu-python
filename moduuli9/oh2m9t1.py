class Auto:
    def __init__(self,rekisteritunnus,huippunopeus,tämänhetkinennopeus = 0,kuljettumatka = 0):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tämänhetkinennopeus = tämänhetkinennopeus
        self.kuljettumatka = kuljettumatka

auto1 = Auto("ABC-123",142)


print(f"{auto1.rekisteritunnus} {auto1.huippunopeus} {auto1.tämänhetkinennopeus} {auto1.kuljettumatka}")