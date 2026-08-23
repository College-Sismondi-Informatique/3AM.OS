def diviseurs(n) :
    L=[1]
    for j in range(2, int(n**0.5)+1) :
        if n % j==0 :
            L.append(j)
            L.append(n//j)
    L.sort()
    return(L)