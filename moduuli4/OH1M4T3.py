syote = " "
suurin = int(input("luku: "))
pienin = suurin

while True :
    syote = input("luku: ")
    if syote == "":
        break
    int_syote = int(syote)

    if int_syote < pienin:
        pienin = int_syote

    if int_syote > suurin:
        suurin = int_syote

print(f"suurin: {suurin}\npienin: {pienin}")
