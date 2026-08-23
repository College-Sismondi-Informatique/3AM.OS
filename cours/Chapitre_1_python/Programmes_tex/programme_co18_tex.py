a,b,c=eval(input("Saisir les coefficient a, b et c (séparés par une virgule): "))
delta=b**2-4*a*c
if delta > 0 :
    print("Les solutions de l'équation ax"+chr(0x00B2)+"+bx+c=0 sont x1 =",
          (-b+delta**0.5)/(2*a), "et x2 =",(-b-delta**0.5)/(2*a))
elif delta == 0 :
    print("L'unique solution de l'équation ax"+chr(0x00B2)+"+bx+c=0 est x =",
          (-b)/(2*a))
else :
     print("Cette équation n'a pas de solution.")     