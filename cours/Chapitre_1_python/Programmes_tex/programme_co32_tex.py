def ep(n) :
    if n<=1 :
        return(0)
    for k in range(2,n) :
        if n%k==0 : 
            return(0)
    return(1)
    
N=2
no=1
while no < 2021 :
    N=N+1
    no=no+ep(N)
print("Le 2021ème nombre premier est :",N)