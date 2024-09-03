import random

def noppa(suurin: int) -> int:
    arvo = random.randint(1,suurin)
    return arvo

noppasuurin = int(input("nopan suurin luku: "))

while True:
    arvo2 = noppa(noppasuurin)
    print(arvo2)
    if arvo2 == noppasuurin:
        break

