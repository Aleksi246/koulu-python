n = 0
while n < 5:
    kayttaja = input("käyttäjätunnus: ")
    sal = input("salasana: ")
    if kayttaja == "python" and sal == "rules":
        print("tervetuloo")
        exit()

    n = n+1
print("pääsy evästetty")