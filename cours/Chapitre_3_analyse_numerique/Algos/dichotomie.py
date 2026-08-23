#!/usr/bin/python3
# -*- coding: utf-8 -*-

#------------------------------------------
# Dichotomie
#------------------------------------------
from math import exp
from math import sin

# La fonction
def f(x):
#    return 4*x**4-12*x**3+x**2+12*x+4
#     return x**2-2
#     return x-0.3
    return exp(x-1)-x**4/4
#    return sin(x)**2+x/3
#    return x**12 - 1.1
#    return(x/(3*(0.57**2+x**2)**0.5)-1/5)
#    return((3*(0.57**2+x**2)**0.5)/5)
    return x-0.2*sin(x)-0.5 # Exercice E4.19


# Dichotomie itératif (n est le nombre d'étape)
def dichotomie_etape(a,b,n):    
    for i in range(1,n+1):
        c = (a+b)/2
        if f(a)*f(c) <= 0:
            b = c
        else:
            a = c
        print("Etape ", i, " : ", a,"    ", b) 
    return a,b


# Dichotomie itératif (prec est la précision)
def dichotomie_precision(a,b,precision):  
    i=0
    while b-a>precision:
        i=i+1
        c = (a+b)/2
        if f(a)*f(c) <= 0:
            b = c
        else:
            a = c  
#        print("Etape ", " : ", a,"    ", b) 
    return a,b,i



# Dichotomie récursif
def dichotomie(a,b,precision):
    if b-a<=precision:
        return a,b
    else :
        c = (a+b)/2
        if f(a)*f(c) <= 0:
            return dichotomie(a,c,precision)
        else:
            return dichotomie(c,b,precision)
        
#----------- Calculs -----------

#Exercice E4.19
print("Zéro de la fonctionf : " , dichotomie_precision(0.5,1,0.001))    
    
    
    
    
    
#print("Calcul de exp(x-1)+x**4/4=0 par la dichotomie")
##print(dichotomie_etape(0,5,20))  
##print(dichotomie_etape(-0.1,0.1,18))  
#print(dichotomie_precision(-3,-2,0.0001)) 
#print(dichotomie_precision(-1,0,0.0001)) 
#print(dichotomie_precision(0,1,0.001)) 
#print(f(1))
#print(dichotomie(1,2,0.000001))  

    
#print("Calcul de 1,1^(1/12) par la dichotomie")
#print(dicho(1,1.1,8)) 
#print(dichobis(1,1.1,0.001))  
#print(dichotomie(1,1.1,0.00001))  



#---------------------------------------------------------------------
# EXEMPLE INTERESSANT OU LA METHODE DE DICHOTOMIE PEUT ECHOUER.
#---------------------------------------------------------------------
# En théorie g(x) ne possède qu'un zéro en 0. Mais on constate que numériquement,
# la fonction change de signe un grand nombre de fois autour de 0.
# Cela provient (probablement) des erreurs de calculs (approximations) inhérentes à la machine.
#def g(x):
#    return(exp(x)-1-x-x**2/2)
#    
#   
#for i in range(1,10):
#    print("Image de  : ", (-1)**i*10**(-1*i) , " = ", g((-1)**i*10**(-1*i)))






