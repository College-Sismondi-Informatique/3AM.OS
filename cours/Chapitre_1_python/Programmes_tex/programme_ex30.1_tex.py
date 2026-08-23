def fonction_un(ch) :
    nb=0
    for v in ch :
        if v in "aeiouAEIOUéàèùû" :
            nb=nb+1
    return(nb)