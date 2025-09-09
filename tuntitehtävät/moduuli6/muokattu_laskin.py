import math

def keskiarvo(luku1, luku2):
    print("Aritmeettinen keskiarvo on (A + B) / 2")
    print("Geometrinen keskiarvo on neliöjuuri tulosta A * B")
    print("Aritmeettinen keskiarvo on", (luku1 + luku2) / 2)
    print("Geometrinen keskiarvo on", math.sqrt(luku1 * luku2))
    return

def jakolasku(luku1, luku2):
    osamaara = luku1 / luku2
    osamaara_int = luku1 // luku2
    jakojaannos = luku1 % luku2
    print(luku1, "jaettuna luvulla", luku2, "on", osamaara)
    print("  Tai toisin sanoin tulos on:", osamaara_int, "ja jakojäännös", jakojaannos)
    return

def esimerkit():
    esim1 = 2
    esim2 = 4
    print(f"Tällä laskimella voi tehdä vaikka mitä, tässä esimerkkinä luvut {esim1} ja {esim2}")
    print("---")
    print("tulo on", esim2 * esim2)
    print("---")
    jakolasku(esim1, esim2)
    print("---")
    keskiarvo(esim1, esim2)
    print("---")
    print("Kokeile itse!")
    return

esimerkit()
komento = input("Mitä lasketaan? Anna komento: kerto/jako/keskiarvo/lopeta\n")
while komento != "lopeta":
    luku1 = int(input("Anna eka luku: "))
    luku2 = int(input("Anna toka luku: "))
    if komento == "kerto":
        print("tulo on", luku1 * luku2)
    elif komento == "jako":
        jakolasku(luku1, luku2)
    elif komento == "keskiarvo":
        keskiarvo(luku1, luku2)
    else:
        print("komentoa ei tunnistettu")
    komento = input("Mitä lasketaan? Anna komento: kerto/jako/keskiarvo/lopeta\n")

print("Laskinohjelma lopetettu")