import random
pisteiden_maara = int(input("pisteiden määrä: "))
counterympyransisalla = 0
counter = 0

while counter < pisteiden_maara:

    xkord = random.uniform(-1,1)
    ykord = random.uniform(-1,1)

    if xkord**2 + ykord**2 < 1:
        counterympyransisalla = counterympyransisalla + 1

    counter = counter + 1


piiarvio = (4*counterympyransisalla)/(pisteiden_maara)

print(piiarvio)
