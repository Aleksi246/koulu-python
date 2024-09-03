
luku = int(input("luku: "))
counter = 0
for i in range(2,luku-1):

    if luku == 0:
        break
    if luku%(i) == 0:
        print(f"{luku} ei ole alkuluku se on jaollinen luvulla {i}")
        counter = 1
        break

if counter == 0:
    print(f"{luku} on alkuluku")