kanta = float(input("Anna suorakulmion kanta: "))
korkeus = float(input("Anna suorakulmion korkeus: "))

piiri = (kanta + korkeus) * 2
pintaAla = kanta * korkeus

print(f"Piiri: {piiri: <5.3f}")
print(f"Pinta-ala: {pintaAla: <5.3f}")