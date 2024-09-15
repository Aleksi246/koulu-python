tuuma = 0
while tuuma >=0:

    tuuma = int(input("tuumat: "))
    if tuuma < 0:
        exit()
    print(f"{tuuma*2.54} cm")