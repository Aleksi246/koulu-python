import random


def noppa():
    arvo = random.randint(1,6)
    return arvo

while True:
    arvo2 = noppa()
    print(arvo2)
    if arvo2 == 6:
        break