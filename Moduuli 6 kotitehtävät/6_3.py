
gallona_litroina = 3.785

def gallonat_litroiksi(gallonat):
    return gallonat * gallona_litroina

while True:
    gallonat = input("Anna gallonamäärä: ")

    if gallonat == "":
        print("Tyhjä arvo. Poistutaan loopista.")
        break

    if float(gallonat) < 0:
        print("Negatiivinen määrä. Poistutaan loopista.")
        break

    print(gallonat_litroiksi(float(gallonat)))