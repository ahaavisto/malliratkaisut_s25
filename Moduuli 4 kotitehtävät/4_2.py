# 1 tuuma = 2.54 cm

while True:
    tuuma = float(input("Anna tuuma: "))
    if tuuma < 0:
        break

    print(f"{tuuma} tuumaa on {tuuma*2.54} cm.")