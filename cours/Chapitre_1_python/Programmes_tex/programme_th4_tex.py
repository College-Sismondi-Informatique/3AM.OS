def comptage_e(mot):
    compte_e=0
    for i in range(0,len(mot)):
        if mot[i]=="e" :
            compte_e=compte_e+1
    return(compte_e)   