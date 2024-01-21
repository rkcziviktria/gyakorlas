def vizsga1(maxpont,pontszam):

    minimum = round(maxpont * 0.4)
    if pontszam>=minimum:
        return True
    else:
            return False
   
maxpont = float(input("A vizsga maximum pontszáma: "))

nev = 'None'

while nev !='':
    nev= input("Vizsgázó neve: ")
    if nev:
        pontszam = int(input("Elért pontszám: "))
        if vizsga1(maxpont,pontszam):
            print(nev+" vizsgája sikeres!")
        else:
            print(nev+" vizsgája sikertelen!")

