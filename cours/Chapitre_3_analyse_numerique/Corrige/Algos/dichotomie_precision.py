def dichotomie_precision(a,b,precision):    
    while b-a>precision:
        c = (a+b)/2
        if f(a)*f(c) <= 0:
            b = c
        else:
            a = c   
    return a,b