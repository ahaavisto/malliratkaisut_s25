import random

def satunnainen():
    return random.randint(1,6)

while True:
    luku = satunnainen()
    print(f"Silmäluku {luku}")
    if luku == 6:
        break