from time import time
from random import randint
input("Appuyer sur ENTER pour commencer...")
debut=time()
juste=0
while juste < 5 :
    a,b=randint(2,9), randint(2,9)
    resultat=int(input(str(a)+"x"+str(b)+"="))
    if resultat==a*b :
        print("Juste !")
        juste=juste+1
    else:
        print("FAUX !")
fin=time()
temps=round(fin-debut,1)
print("Ton temps est de : ",temps, " secondes.")