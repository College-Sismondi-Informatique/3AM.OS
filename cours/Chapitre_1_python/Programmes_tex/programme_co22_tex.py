n=int(input("Quel est le degré du polynôme : "))
L=[]
for k in range(0,n+1) :
    coef=float(input("Saisir le coefficient de degré "+str(n-k)+" : "))
    L.append(coef)
b=float(input("Saisir la valeur à évaluer : "))
f=L[0]
for k in range(1,n+1) :
    f=f*b+L[k]
print(f)