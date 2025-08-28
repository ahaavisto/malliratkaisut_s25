nimi = input("Anna nimi: ")
adjektiivi = input("Anna joku adjektiivi: ")

print("Olipa kerran opiskelija nimeltä", nimi + ".")
print(nimi, "aloitti opiskelut Metropoliassa, joka on", adjektiivi, "ammattikorkeakoulu Suomessa.",
      "\nHänen ensimmäinen kurssinsa oli", adjektiivi, "ohjelmoinnin kurssi.")

print(f"Eräänä päivänä {nimi} halusi mennä lounaalle. Mutta hän ei muistanut, missä kerroksessa ruokala on!")
komento = input(f"Mihin kerrokseen {nimi} menee? (anna numero) ")
while komento != "2":
    print("Tästä kerroksesta ei löytynyt ruokalaa.")
    komento = input(f"Mihin kerrokseen {nimi} menee seuraavaksi? (anna numero) ")
print(f"2. kerroksesta {nimi} löysi ruokalan.")



print("Ruokalassa hänellä oli vaikea valinta edessään.")
lounas = input("Syödäkö kalakeittoa vai kasvispyöryköitä? (vastaa kala tai kasvis)\n")
if lounas == "kala":
    print(f"Kalakeitto oli valitettavasti tylsän makuista ja {nimi} pettyi.")
elif lounas == "kasvis":
    print(f"Kasvispyörykät olivat tosi hyviä ja {nimi} tuli iloiseksi.")
else:
    print(f"Sellaista lounasta ei ollutkaan ja {nimi} jäi nälkäiseksi.")