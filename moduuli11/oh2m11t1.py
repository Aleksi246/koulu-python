class Julkaisu:

    def __init__(self,julkaisunnimi):

        self.julkaisunnimi = julkaisunnimi

    def tulosta_tiedot(self):
        print(f"julkaisun nimi: {self.julkaisunnimi}")

class Kirja(Julkaisu):

    def __init__(self,kirjoittaja,sivumäärä,julkaisunnimi):

        self.kirjoittaja = kirjoittaja
        self.sivumäärä = sivumäärä
        super().__init__(julkaisunnimi)

    def tulosta_tiedot(self):

        super().tulosta_tiedot()
        print(f"    kirjoittaja: {self.kirjoittaja}\n    sivumäärä: {self.sivumäärä}")


class Lehti(Julkaisu):

    def __init__(self,päätoimittaja,julkaisunnimi):

        self.päätoimittaja = päätoimittaja
        super().__init__(julkaisunnimi)

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f"    päätoimittaja: {self.päätoimittaja}")


x = Kirja("Rosa Liksom", 200, "Hytti n:o 6")
y = Lehti("Aki Hyyppä", "Aku Ankka")

x.tulosta_tiedot()
y.tulosta_tiedot()