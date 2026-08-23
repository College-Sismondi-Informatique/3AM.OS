def dichotomie_etape(a,b,n):    
    for i in range(1,n+1):
        c = (a+b)/2
        if f(a)*f(c) <= 0:
            b = c
        else:
            a = c
    return a,b