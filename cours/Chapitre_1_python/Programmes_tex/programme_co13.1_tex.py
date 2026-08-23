nombre=int(input("Entrez un nombre à 2 chiffres : "))
unites=nombre%10
dizaines=nombre//10
nombreinverse=10*unites+dizaines
print("Le nombre inversé est : ", nombreinverse)