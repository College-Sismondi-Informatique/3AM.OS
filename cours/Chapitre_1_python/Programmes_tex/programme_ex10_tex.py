x=input("Entrer un nombre : ")
y=eval(x)
L=[]
z="2**"+x+"="+str(2**y)
L.append(z)
y=y+1
u="2**"+str(y)+"="+str(2**y)
L.append(u)
print(L)