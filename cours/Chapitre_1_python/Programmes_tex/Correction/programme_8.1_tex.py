a=int(input("Entrer un nombre : "))
D="("+str(a)+"+X)"+"("+str(a)+"-X)"+chr(0x00B2)+"="+str(a**2)+"-"+"X"+chr(0x00B2)
print(D)