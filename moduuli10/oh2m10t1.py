class Hissi:
    def __init__(self,alinkerros,ylinkerros):
        self.alinkerros = alinkerros
        self.ylinkerros = ylinkerros
        self.kerros = alinkerros

    def kerros_ylös(self):
        if self.kerros != self.ylinkerros:
            self.kerros += 1
        print(f"kerros: {self.kerros}")
    def kerros_alas(self):
        if self.kerros != self.alinkerros:
            self.kerros -= 1
        print(f"kerros: {self.kerros}")
    def siirry_kerrokseen(self,kerros):
        while self.kerros != kerros:
            if self.kerros > kerros:
                self.kerros_alas()
            else:
                self.kerros_ylös()

h = Hissi(4,290)

h.siirry_kerrokseen(79)
h.siirry_kerrokseen(h.alinkerros)
