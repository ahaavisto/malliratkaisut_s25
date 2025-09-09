vuosi = int(input("Anna vuosiluku: "))
while vuosi >= 1896:

    if vuosi % 4 == 0:
        print("On olympiavuosi")
    else:
        print("Ei ole olympiavuosi")

    vuosi = int(input("Anna vuosiluku: "))

print("Ohjelma ohi")