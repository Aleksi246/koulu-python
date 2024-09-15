

def parilista(l:list) -> list:
    lista1 = []
    for i in l:
        if i%2 == 0:
            lista1.append(i)

    return lista1

print("anna lista numeroita päätä syöttö syöttämällä tyhjä merkkirivi")
lista2 = []
while True:
    luku_str = input("luku: ")
    if luku_str == "":
        break

    luku_int = int(luku_str)

    lista2.append(luku_int)

print(lista2)
print(parilista(lista2))