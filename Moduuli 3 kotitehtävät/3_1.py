pituus = float(input("Anna kuhan pituus senttimetreissä: "))

minimi_pituus = 37

if pituus < minimi_pituus:
    print(f"Palauta kuha veteen. Kuhan minimipituus on {minimi_pituus}, tämän kuhan pyyntimitasta puuttuu {minimi_pituus - pituus} senttimetriä.")
else:
    print("Tämän kuhan pituus on riittävä. Kuhan pituus on oltava vähintään " + str(minimi_pituus) + " senttiä.")