vuosi = int(input("Anna vuosiluku: "))

# karkausvuoden säännöt
# vuosi jaollinen neljällä
# 100 jaollinen vain jos myös jaollinen 400

if vuosi % 4 == 0 and (vuosi % 100 != 0 or vuosi % 400 == 0):
    print(f"{vuosi} on karkausvuosi.")
else:
    print(f"{vuosi} ei ole karkausvuosi.")