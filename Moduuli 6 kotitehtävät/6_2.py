import random

def noppa(max):
    return random.randint(1,max)

maksimi = int(input("Anna maksimi silmäluku: "))


while True:
    luku = noppa(maksimi)
    print(f"Silmäluku {luku}")
    if luku == maksimi:
        break


        