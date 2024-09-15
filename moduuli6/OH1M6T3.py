

def gallonatlitroiksi(gallona: float) -> float:
    litrat = gallona*3.785
    return litrat

while True:
    gallona2 = float(input("gallonat: "))
    if gallona2 < 0:
        break
    litroina = gallonatlitroiksi(gallona2)
    print(f"litroina: {litroina}")