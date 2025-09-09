oikea_tunnus = "python"
oikea_salasana = "rules"

arvaukset = 0

while arvaukset < 5:
    tunnus = input("Anna tunnus: ")
    salasana = input("Anna salasana: ")

    if tunnus == oikea_tunnus and salasana == oikea_salasana:
        print("Tervetuloa")
        break

    arvaukset = arvaukset + 1

else:
    print("Pääsy evätty")