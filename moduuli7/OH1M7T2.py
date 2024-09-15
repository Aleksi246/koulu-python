
nimet = set()

while True:

    nimi = input("nimi: ")
    if nimi == "":
        break
    if nimi in nimet:
        print("aiemmin syötetty nimi")
    else:
        print("uusi nimi")
        nimet.add(nimi)
    
for i in nimet:
    print(i)