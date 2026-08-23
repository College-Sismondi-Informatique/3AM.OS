from random import randint
print("Il faut un 6 pour gagner !")
ok=True
while ok :
    n=randint(1,6)
    if n==6 :
        print("6 ! C’est gagné !")
        rejouer=input("Voulez-vous rejouer? (O/N) : ")
        if rejouer=="N":
            ok=False
    else :
        print(n,"... C’est raté.")