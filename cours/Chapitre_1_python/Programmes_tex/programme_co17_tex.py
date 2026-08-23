a,b=eval(input("Saisir les coefficient a et b (séparés par une virgule): "))
if a != 0 :
    print("La solution de l'équation ax+b=0 est x =",-b/a)
elif a==0 and b==0 :
    print("Tout nombre est solution de cette équation.")
else :
     print("Cette équation n'a pas de solution.")   