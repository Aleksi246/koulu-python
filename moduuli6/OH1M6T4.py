

def summa(l: list) -> int:
    summaarvo = 0
    for i in l:
        summaarvo = summaarvo + i

    return summaarvo

print("anna summattavia lukuja anna viimeisenä lukuna nolla")

lista = []
while True:

    luku = int(input("luku: "))
    if luku == 0:
        break
    lista.append(luku)

print(summa(lista))
