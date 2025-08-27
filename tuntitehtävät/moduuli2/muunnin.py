syote = int(input("Kuinka monta grammaa: "))


kilot = int(syote / 1000) #muutetaan kokonaisluvuksi lopuksi, jolloin grammat "katoavat"
#TOINEN TAPA:
#kilot = grammat//1000 #jakolasku joka palauttaa pelkän kokonaisosan

grammat_jaljella = syote - kilot * 1000
#TOINEN TAPA:
#grammat_jaljella = grammat%1000 #jakojäännös kun jaetaan tuhannella

print(kilot, "kg ja", grammat_jaljella, "g")