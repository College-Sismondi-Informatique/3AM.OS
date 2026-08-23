from random import randint
print("Il faut un 6 pour gagner !")
ok=False
while not ok :
    n=randint(1,6)
    if n==6 :
        print("6 ! C’est gagné !")
        ok=True
    else :
        print(n,"... C’est raté.")