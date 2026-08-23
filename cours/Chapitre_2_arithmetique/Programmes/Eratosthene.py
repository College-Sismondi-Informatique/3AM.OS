n=int(input("Entrer un nombre entier positif : "))
liste_entiers=list(range(0,n+1))
liste_entiers[1]=0
for k in range(2,n):
    if liste_entiers[k]!=0:
        for j in range(2,n//k+1):
            liste_entiers[j*k]=0
 
while liste_entiers.count(0)>0:
    liste_entiers.remove(0)
    
print(liste_entiers)