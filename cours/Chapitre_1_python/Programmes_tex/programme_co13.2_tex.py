nombre=int(input("Entrez un nombre à 2 chiffres : "))
unites=nombre%10
dizaines=nombre//10%10
centaines=nombre//100
nombreinverse=100*unites+10*dizaines+centaines
print("Le nombre inversé est : ", nombreinverse)