arvo = input("Anna luku: ")
luku = int(arvo)

pienin = luku
suurin = luku

while True:
    arvo = input("Anna luku: ")
    if arvo == "":
        break

    luku = int(arvo)

    if luku < pienin:
        pienin = luku
    if luku > suurin:
        suurin = luku

print(f"Pienin: {pienin}")
print(f"Suurin: {suurin}")