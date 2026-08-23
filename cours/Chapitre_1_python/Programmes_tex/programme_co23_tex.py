from random import randint
secret=randint(1,20)
essai=1
nb=int(input("Je pense à un nombre entre 1 et 20. Devine ce nombre : "))
while nb != secret :
    if nb < secret :
        print("Ton nombre est trop petit!")
    elif nb > secret :
        print("Ton nombre est trop grand!")
    essai=essai+1
    nb=int(input("Essaye encore : "))
print("Bravo! Tu as trouvé le nombre en", essai, " essai(s)!")