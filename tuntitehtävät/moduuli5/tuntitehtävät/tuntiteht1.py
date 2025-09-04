# Kirjoita ohjelma, joka kysyy käyttäjältä kokonaisluvun.
# Ohjelman tulee laskea ja tulostaa kaikki parilliset luvut 0:sta käyttäjän antamaan lukuun asti käyttäen for-silmukkaa.
# Jos käyttäjä antaa negatiivisen luvun tai nollan, ohjelma tulostaa virheilmoituksen.

luku = int( input("Anna kokonaisluku ") )

# jos saatu arvo on nolla tai negatiivinen, niin tulostetaan virheilmoitus
if luku <= 0:
    print("Halusimme positiivisen kokonaisluvun!")
else:
    # käydään yksitellen läpi arvot 0, 1, 2, ..., käyttäjän antama luku.
    # jos arvo on parillinen, niin tulostetaan se
    for laskuri in range(luku + 1):
        if laskuri % 2 == 0:
            print(laskuri)
