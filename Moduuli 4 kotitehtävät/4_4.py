import random

luku = random.randint(1, 10)

while True:
    arvaus = int(input("Anna arvaus: "))

    if arvaus == luku:
        print("Oikein")
        break

    if arvaus < luku:
        print("Liian pieni arvaus")
    elif arvaus > luku:
        print("Liian suuri arvaus")