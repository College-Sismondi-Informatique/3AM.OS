def dichotomie_etape_indiquee(a,b,n):    
    for i in range(1,n+1):
        c = (a+b)/2
        if f(a)*f(c) <= 0:
            b = c
        else:
            a = c
        print('Etape ', i, ' : ', a,'    ', b) 
    return a,b