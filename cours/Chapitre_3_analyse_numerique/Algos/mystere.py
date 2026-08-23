def mystere(a,b,precision):
    if b-a<=precision:
        return a,b
    else :
        c = (a+b)/2
        if f(a)*f(c) <= 0:
            return mystere(a,c,precision)
        else:
            return mystere(c,b,precision)