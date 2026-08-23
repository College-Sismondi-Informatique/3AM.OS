a=int(input("Entrer un nombre : "))
D="("+str(a)+"+X)"+chr(0x00B2)+"="+str(a**2)+"+"+str(2*a)+"X+X"+chr(0x00B2)
print(D)