def sommerec(n) :
    if n==0 :
        return(0)
    else :
        S=n**2+sommerec(n-1)
    return(S)