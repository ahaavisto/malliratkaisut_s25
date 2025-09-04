'''
3.	Tee lisätoimintoja tehtävään 2.
Tarkista python-koodilla, että onko luku 10 mukana listassa.
Jos luku 10 on mukana, niin tulosta "luku 10 löytyi", muuten "lukua 10 ei löytynyt".

Järjestä listan luvut suurimmasta pienimpään.
Tulosta listan luvut allekkain yksi kerrallaan.
Vinkki: listalla on myös reverse() -toiminto
'''

# tehdään uusi, tyhjä lista käyttäjän antamia lukuja varten
luvut = []

# kysytään käyttäjältä kokonaislukuja ja tallennetaan ne listaan.
# Negatiivinen luku lopettaa kyselyn, negatiivista lukua ei talleteta listaan.
arvo = int( input("Anna kokonaisluku, negatiivinen arvo lopettaa ") )     # eka arvo ennen while-ehtoa

while arvo >= 0:
    luvut.append(arvo)      # uusi arvo menee listan loppuun.
    arvo = int( input("Anna kokonaisluku, negatiivinen arvo lopettaa ") )

# lajittelen numerot suuruusjärjestykseen, pienin ensin.
luvut.sort()

print("Antamasi luvut suuruusjärjestyksessä:")
print(luvut)

# === Uudet ominaisuudet ===

# onko luku 10 listassa?
if 10 in luvut:
    # \n tekee rivinvaihdon tulostukseen.
    print("Voiko python koodaus olla näin helppoa? \nluku 10 löytyi listasta")
else:
    print("luku 10 ei ollut listassa")

# käännetään listan luvut alenevaan eli käänteiseen järjestykseen
luvut.reverse()
# luvut.sort(reverse=True)      # vaihtoehtoinen tapa

# tulostetaan listan alkiot yksitellen
print("-- listan alkiot suurimmasta pienimpään")
for luku in luvut:
    print(luku)