'''
2.	Tee ohjelma, joka kysy käyttäjältä kokonaislukuja, kunnes käyttäjä antaa negatiivisen luvun.
Luvut talletetaan listaan, viimeistä eli negatiiivista lukua ei kuitenkaan talleteta listaan.
Järjestä luvut suuruusjärjestykseen, pienin ensin.
Tulosta sen sen jälkeen listan kaikki luvut.
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