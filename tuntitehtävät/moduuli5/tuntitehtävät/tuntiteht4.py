'''
4.	Kirjoita ohjelma, joka pyytää käyttäjältä lukuja siihen saakka,
kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi.
Luvut tallennetaan listaan.
Tämän jälkeen ohjelman tulee käydä listan alkiot läpi ja tulostaa ne luvut,
jotka ovat suurempia kuin 100. Tulosta jokainen luku vain kerran,
vaikka se olisi syötetty useammin kuin kerran.
'''

# lista, johon käyttäjän antamat luvut talletetaan
luvut = []
# lista, johon laitetaan jo tulostetut luvut
tulostetut_luvut = []

# kysytään lukuja, kunnes saadaan tyhjä merkkijono (ahaa, syöte luettava merkkijonona)
arvo_str = input("Anna kokonaisluku, tyhjä lopettaa ")

while arvo_str != "":
    arvo = int(arvo_str)        # merkkijono muutetaan kokonaisluvuksi
    luvut.append(arvo)          # kokonaisluku lisätään listan loppuun
    arvo_str = input("Anna kokonaisluku, tyhjä lopettaa ")

# tulostetaan käyttäjän antamista luvuista ne, joiden arvo on yli 100.
# Jos sama arvo on annettu useamman kerran, niin se tulostetaan vain kerran.
for luku in luvut:
    if luku > 100:
        # tarkistetaan, että lukua ei ole vielä tulostettu
        if luku not in tulostetut_luvut:
            print(luku)
            # lisätään äsken tulostettu luku jo tulostettuihin arvoihin
            tulostetut_luvut.append(luku)