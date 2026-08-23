# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 19:56:46 2018

@author: guilh
"""

pwd=input("Entrez un mot de passe : ")
ok=False
while not ok:
    while len(pwd)<6 :
        pwd=input("Votre mot de passe doit contenir au moins 6 caractères. Veuillez en saisir un nouveau : ")
    for i in range(0,len(pwd)):
        if pwd[i] in "*#%&*$" :
            print("mot de passe : ", pwd, "correct.")
            ok=True
            break
#            for j in range(0,len(pwd)):
#                if pwd[i] in "ABCDEFGHIJKLMNOPQRSTWXYZ" :
#                    ok=True
    if not ok :
        pwd=input("Votre mot de passe doit contenir au moins un des caractères suivant *#%&*$. Veuillez en saisir un nouveau : ")
#print("mot de passe : ", pwd, "correct.")