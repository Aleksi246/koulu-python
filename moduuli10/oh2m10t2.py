
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


class Talo:
    def __init__(self,alin,ylin,hlkm):
        self.alin = alin
        self.ylin = ylin
        self.hlkm = hlkm
        self.hissit = []
        for i in range(0, self.hlkm):
            h = Hissi(self.alin, self.ylin)
            self.hissit.append(h)




    def aja_hissiä(self,hissi_indexi,KohdeKerros):
        self.hissit[hissi_indexi].siirry_kerrokseen(KohdeKerros)

talo = Talo(1,10,4)

talo.aja_hissiä(0,5)
