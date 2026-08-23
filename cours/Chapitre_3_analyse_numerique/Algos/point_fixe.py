# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 00:39:48 2020

@author: guilh
"""
#------------------------------------------
# G. Vorpe - Collège Sismondi
# APPLICATION DES MATHEMATIQUES - 3èME ANNEE
# :: Analyse Numérique ::
#------------------------------------------
# Méthode du Point Fixe
#------------------------------------------

from math import sin
from math import exp
from math import log
from math import radians
from math import degrees

def f(x):
#    return(-1/4*x+1/(3*x**2))
#    return(x**2-2)
#    return(1+2/x)
    # return((0.2*sin(x)+0.5))
    return((2*x-0.2*sin(x)-0.5))
#    return(x+log(x**2-x-1,10))
#    return(x/(3*(0.57**2+x**2)**0.5)-1/5+x)  # EX5 : Mauvais choix de fonction
    # return((3*(0.57**2+x**2)**0.5)/5) # EX5 : Bonne fonction à choisir

    
    
    
def point_fixe(x0,n):
    for i in range(1,n+1):
        print(x0, " , étape ", i)
        x0=f(x0)
    return(x0)
    
print("Méthode point_fixe", point_fixe(1,20)) 
#print(log(10,10))
#print(f(-0.11))

def point_fixe_precision(x0,precision):
    x1=f(x0)
    i=1
    while abs(x1-x0)>precision:
        x0=x1
        x1=f(x0)
        i=i+1
    return[x1,i]
    
print("Méthode point_fixe_precision", point_fixe_precision(1,0.0001)[0], "\n Etape : ", point_fixe_precision(1,0.0001)[1]) 