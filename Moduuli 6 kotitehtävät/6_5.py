def parilliset(arvot):
    uusi_lista = []
    for arvo in arvot:
        if arvo % 2 == 0:
            uusi_lista.append(arvo)
    return uusi_lista

lista = []
while True:
    user_input = input("Anna luku (tyhjä lopettaa): ")
    if user_input == "":
        break

    arvo = int(user_input)
    lista.append(arvo)

print(f"Alkuperäinen: {lista}")
print(f"Parilliset: {parilliset(lista)}")