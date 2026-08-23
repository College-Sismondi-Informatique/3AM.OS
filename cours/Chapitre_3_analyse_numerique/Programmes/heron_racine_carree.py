def racine_carree(a,d,n):
    u=d 
    for i in range(1,n+1):
        u = 0.5*(u+a/u)
        print("Etape ", i, " : ", u) 
    return u