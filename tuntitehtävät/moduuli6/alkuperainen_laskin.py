import math
komento = input("Mitä lasketaan? Anna komento: kerto/jako/keskiarvo/lopeta\n")
while komento != "lopeta":
    luku1 = int(input("Anna eka luku: "))
    luku2 = int(input("Anna toka luku: "))
    if komento == "kerto":
        print("tulo on", luku1 * luku2)
    elif komento == "jako":
        osamaara = luku1 / luku2
        osamaara_int = luku1 // luku2
        jakojaannos = luku1 % luku2
        print(luku1, "jaettuna luvulla", luku2, "on", osamaara)
        print("  Tai toisin sanoin tulos on:", osamaara_int, "ja jakojäännös", jakojaannos)
    elif komento == "keskiarvo":
        print("Aritmeettinen keskiarvo on (A + B) / 2")
        print("Geometrinen keskiarvo on neliöjuuri tulosta A * B")
        print("Aritmeettinen keskiarvo on", (luku1 + luku2)/2)
        print("Geometrinen keskiarvo on", math.sqrt(luku1 * luku2))
    else:
        print("komentoa ei tunnistettu")
    komento = input("Mitä lasketaan? Anna komento: kerto/jako/keskiarvo/lopeta\n")

print("Laskinohjelma lopetettu")