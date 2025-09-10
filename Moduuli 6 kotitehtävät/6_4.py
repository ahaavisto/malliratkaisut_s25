def summaa(arvot):
    tulos = 0
    for arvo in arvot:
        tulos = tulos + arvo
    return tulos

lista = []
while True:
    user_input = input("Anna luku (tyhjä lopettaa): ")
    if user_input == "":
        break

    arvo = int(user_input)
    lista.append(arvo)

print(f"Summa: {summaa(lista)}")