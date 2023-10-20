import random

def lancer_attaque(num_attaque):

    import random

    esquive = random.choice([True,False])
    if esquive == True:
        print("esquive")
        degat = 0

    else:

        if num_attaque == 1:
            print("coup de poing")
            degat_max = 9
        elif num_attaque == 2:
            print("coup de pied")
            degat_max = 15
        elif num_attaque == 3:
            print("coup de boule")
            degat_max = 30
        else:
            print("rien")
            degat_max = 0
        
        print("degats max :", degat_max)
        if degat_max > 0:
            degat = random.randrange(1, degat_max, 1)
        else:
            degat = 0

    print("degats : -", degat, " pv")

    return degat

def utiliser_objet(nom_objet):
    print("J'utilise l'objet : ", nom_objet)
    if nom_objet == "potion":
        pv_bonus = random.randrange(1,10,1)
    elif nom_objet == "pomme":
        pv_bonus = 3
    else:
        pv_bonus = 0
    
    print("Ce guerrier a gagné :", pv_bonus, "pv")

    return pv_bonus