S=0
L=[]
n=int(input("Entrez un nombre entier : "))
for p in range(1,n+1):
    L.append(p**3)
    S=S+p**3
print(L)
print("La somme des",n, "premiers cubes parfaits vaut :",S)