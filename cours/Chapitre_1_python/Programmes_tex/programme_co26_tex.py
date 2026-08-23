pwd=input("Entrez un mot de passe : ")
ok=False
while not ok:
    while len(pwd)<6 :
        pwd=input("Votre mot de passe doit contenir au moins 6 caractères.
                   Veuillez en saisir un nouveau : ")
    for lettre in pwd:
        if lettre in "*#&%$" :
            ok=True
    if not ok :
        pwd=input("Votre mot de passe doit contenir au moins un des caractères 
                   suivants *#%&*$. Veuillez en saisir un nouveau : ")
print("Mot de passe : ", pwd, "correct.")