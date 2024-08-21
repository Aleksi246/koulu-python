pituus = int(input("kuhan pituus centteinä: "))

if pituus < 37:
    print(f"kuha on {37-pituus} centtiä liian lyhyt. Heitä kuha takas")

if pituus > 100:
    print("unissas")