import random

def noppa(tahkot):
    tulos = random.randint(1,tahkot)
    return tulos

koko = int(input("Kuinka isoa noppaa heitetään? "))
montako = int(input("Montako kertaa?"))

for luku in range(montako):
    tulos = noppa(koko)
    print("Nopasta tuli", tulos)