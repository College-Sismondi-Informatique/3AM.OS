x=eval(input("Entrer un nombre positif x strictement inférieur à 1 : "))
while x>=1 or x<0:
    x=eval(input("Entrer un nombre positif x strictement inférieur à 1 : "))
n=1
while x**n > 10**(-10) :
    n=n+1
print("La plus petite puissance n telle que x**n<=10**(-10) est : ",n)