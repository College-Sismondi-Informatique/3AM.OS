def point_fixe(x0,n):
    for i in range(1,n+1):
        x0=f(x0)
    return(x0)