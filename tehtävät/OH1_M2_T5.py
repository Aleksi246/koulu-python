import math

leiviskat = float(input("Leiviskät: "))
naulat = float(input("Naulat: "))
luodit = float(input("Luodit: "))

massagrammoina = luodit*13.3 + naulat*32*13.3 + leiviskat*20*32*13.3


kilot = int(massagrammoina/1000)

grammat = massagrammoina - (kilot* 10**3)

print(f"Massa: {kilot} kiloa ja {grammat} grammaa")