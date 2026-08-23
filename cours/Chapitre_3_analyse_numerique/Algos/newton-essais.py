#!/usr/bin/python3
# -*- coding: utf-8 -*-

#------------------------------------------
# Newton
#------------------------------------------


# Cas de la racine carrée sqrt(a)
# n est le nombre d'itérations
def racine_carree(a,d,n):
    u=d                # Valeur de dépaert. N'importe qu'elle valeur > 0
    for i in range(1,n+1):
        u = 0.5*(u+a/u)
        print("Etape ", i, " : ", u) 
    return u
    

# La fonction f(x)
def f(x):
#    return x**12 - 1.1
    return x**(1/3)


# La fonction dérivée f'(x)
def df(x):
#    return 12*x**11  
    return 1/(3*x**(2/3))


# Méthode de Newton 
# u est le terme initial, n est le nombre d'étapes
def newton(u,n):  
    for i in range(1,n+1):
        u = u-f(u)/df(u)
        print("Etape ", i, " : ", u) 
    return u


    
#print("Calcul de 1,1^(1/12) par la méthode de Newton")
#print(newton(1,5)) 

print(racine_carree(2,1,5))

