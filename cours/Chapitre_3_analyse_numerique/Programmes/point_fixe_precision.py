def point_fixe_precision(x0,precision):
    x1=f(x0)
    while abs(x1-x0)>precision:
        x0=x1
        x1=f(x0)
    return(x1)