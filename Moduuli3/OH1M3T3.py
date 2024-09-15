
sukupuoli = input("Sukupuoli(M tai N): ")

hemo = int(input("Hemoglobiiniarvo (yksikkö: g/l): "))

if sukupuoli == "M" and hemo < 134:
    print("Hemoglobiini alhainen")

if sukupuoli == "M" and hemo > 195:
    print("Hemoglobiini korkea")

if sukupuoli == "M" and 134 <= hemo <= 195 :
    print("Hemoglobiini normaali")


if sukupuoli == "N" and hemo < 117:
    print("Hemoglobiini alhainen")

if sukupuoli == "N" and hemo > 175:
    print("Hemoglobiini korkea")

if sukupuoli == "N" and 117 <= hemo <= 175:
    print("Hemoglobiini normaali")