import math

def pizza_price_per_m2(halkaisija, hinta):
    säde = halkaisija / 2
    pinta_ala = math.pi * (säde ** 2)
    return hinta / (pinta_ala / 1000)

print("Pizza 1:")
pizza_1_halkaisija = float(input("Halkaisija (cm): "))
pizza_1_hinta = float(input("Hinta: "))

print("Pizza 2:")
pizza_2_halkaisija = float(input("Halkaisija (cm): "))
pizza_2_hinta = float(input("Hinta: "))

pizza1_price_per_m2 = pizza_price_per_m2(pizza_1_halkaisija, pizza_1_hinta)
pizza2_price_per_m2 = pizza_price_per_m2(pizza_2_halkaisija, pizza_2_hinta)

print(f"pizza1_price_per_m2 = {pizza1_price_per_m2: <.2f}")
print(f"pizza2_price_per_m2 = {pizza2_price_per_m2: <.2f}")

# jos ensimmäisen pizzan neliöhinta pienempi kuin toisen
if pizza1_price_per_m2 < pizza2_price_per_m2:
    print("Pizza 1 antaa paremman vastineen rahoille.")
else:
    print("Pizza 2 antaa paremman vastineen rahoille.")