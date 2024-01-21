mondat1 =  input("Első mondat: ")
mondat2 = input("Második mondat: ")


if len (mondat1)==len(mondat2):
    print("A mondatok egyenlő hosszúak!")
elif len(mondat1)>len(mondat2):
    print("Az első mondat hosszabb!")
else:
    print("A második mondat hoszabb!")
