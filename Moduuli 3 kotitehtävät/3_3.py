sukupuoli = input("Anna sukupuoli: ")
hemoglobiini = float(input("Anna hemoglobiiniarvo (g/l): "))

if sukupuoli == "nainen":
    if hemoglobiini < 117:
        print("Alhainen")
    elif 117 <= hemoglobiini <= 175:
        print("Normaali")
    else:
        print("Korkea")

elif sukupuoli == "mies":
    if hemoglobiini < 134:
        print("Alhainen")
    elif 134 <= hemoglobiini <= 195:
        print("Normaali")
    else:
        print("Korkea")
else:
    print("Sukupuoli tulee olla pienellä kirjoitettu mies tai nainen.")