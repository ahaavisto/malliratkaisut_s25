import math

# ympyrän säde
sade = float(input("Anna ympyrän säde: "))

pintaAla = math.pi * (sade ** 2)

#print("Pinta-ala = " + str(pintaAla))
print(f"Pinta-ala = {pintaAla: <5.3f}")