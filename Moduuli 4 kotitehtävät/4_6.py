import random, math

# iteraatioiden määrä
# suuremmat luvut = pidempi suoritusaika
pisteiden_määrä = 1000000

laskuri = 0
ympyrän_sisällä = 0

while laskuri < pisteiden_määrä:
    laskuri = laskuri + 1

    x = random.randint(-100000, 100000) / 100000
    y = random.randint(-100000, 100000) / 100000

    if x ** 2 + y**2 < 1:
        ympyrän_sisällä = ympyrän_sisällä + 1

print(f"Oma Pi: {(ympyrän_sisällä / pisteiden_määrä) * 4 }")
print(f"Math.pi: {math.pi}")