def fonction_deux(n) :
    nb=str(n)
    ch=""
    for k in range(0,len(nb)) :
        if nb[k] !="0" :
            ch=ch+nb[k]
    return(int(ch))