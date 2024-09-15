
numerot = []

while True:

    luku_str = input("luku: ")
    if luku_str == "":
        break
    luku_int = int(luku_str)
    numerot.append(luku_int)



numerot.sort(reverse=True)

print(numerot[0:5])
