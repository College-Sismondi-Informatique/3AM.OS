# -*- coding: utf-8 -*-
"""
Created on Sun Sep  5 15:18:12 2021

@author: guilh
"""

#n=1234
#print(int(str(n)[0])+int(str(n)[1])+int(str(n)[2])+int(str(n)[3]))

compteur=0
for n in range(1000,10000):
    if int(str(n)[0])+int(str(n)[1])+int(str(n)[2])+int(str(n)[3])==19:
        compteur+=1
        # print(n)
print(compteur)

print(-6*10%4)