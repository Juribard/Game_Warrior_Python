from lib import actions
from lib import stat

import random

#le guerrier[0] -> pv
#le guerrier[1] = True = joueur; False = pc
guerriers = [[100, True], [100, False]]
tour_jeu = 1

#tour de table
while guerriers [0][0] > 0 and guerriers [1][0] > 0:
    print("---------------------------------------------------------------")
    print("Tour(s): ", tour_jeu)
    for le_guerrier in guerriers:
        
        if le_guerrier[1]:
            #joueur reel
            num_attaque = int(input("choix attaque?"))
        else:
            #joueur pc
            num_attaque = int (random.randrange(1,3,1))
        
        le_guerrier[0] = le_guerrier [0] - actions.lancer_attaque(num_attaque)

    for le_guerrier in guerriers:
        
        if le_guerrier[1]:
            nom_objet = input(" Choix objet? pomme ou potion: ")
        
        else:
            nom_objet = random.choice(["pomme", "potion"])
        
        le_guerrier[0] = le_guerrier[0] + actions.utiliser_objet(nom_objet)

    for index_guerrier, le_guerrier in enumerate(guerriers):
        print("NUMERO GUERRIER: ", index_guerrier + 1)
        stat.afficher_stat(le_guerrier)
    
    tour_jeu = tour_jeu + 1
        
    