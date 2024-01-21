class Diák:
    def __init__(self, név, magasság):
        self.név = név
        self.magasság = magasság

def legmagasabb_diak(diakok):
    max_magassag = -1
    legmagasabb_diak = None

    for diak in diakok:
        if max_magassag < diak.magasság:
            max_magassag = diak.magasság
            legmagasabb_diak =diak

    return legmagasabb_diak, max_magassag

diakok = []

for i in range(3):
    nev = input("Tanuló neve: ")
    magassag = int(input("Magassága (cm): "))
    diakok_adatai = Diák(nev,magassag)
    diakok.append(diakok_adatai)

    legmagasabb_diak_eredmeny, _ = legmagasabb_diak(diakok)

print()
for diakok_adatai in diakok:
    print(diakok_adatai.név,diakok_adatai.magasság, "cm magas.")

if legmagasabb_diak_eredmeny:
    with open("magas.txt", "w") as file:
        file.write(legmagasabb_diak_eredmeny.név + " a legmagasabb.")