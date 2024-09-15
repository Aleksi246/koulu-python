import random

rluku = random.randint(1,10)

while True:
    arvaus = int(input("arvaus: "))

    if arvaus == rluku:
        print("oikein!")
        break
    if arvaus > rluku:
        print("liian suuri arvaus")
    if arvaus < rluku:
        print("liian pieni arvaus")