from lib import attaque

import random

print ("-------------------------------------------------------------------------------------------------------")
print("PARAMETRE DE LA PARTIE:")
pv_user = int(input("PV (Points de vie) par guerriers: "))
pv_pc = pv_user
count_tour = 0
soin_user = 2
soin_pc = soin_user
special_user = 2
special_pc = special_user
print ("-------------------------------------------------------------------------------------------------------")

print("BUT: Gagner le combat en faisant en sorte que les points de vie du GUERRIER IA soit entre 0 et -2  pv ou inférieur à -15 pv tout en economisant ces capacités.")
print("CONSEIL:")
conseil = random.randrange(1,3,1)
if conseil == 1:
    print("• Les Coups spéciaux ne sont pas esquivables mais sont limités")
elif conseil == 2:
    print("• Vous et le GUERRIER IA gagnez +1 coup special tout les 5 tours (jusqu'au tours 25)")
else:
    print("Si vous ou votre adversaire n'a plus de potion de soin, vous aurez 1 chance sur 5 pour en récupérer une!")
print(".")
print("BONNE CHANCE!")
print(".")
print("SYNTHESE:")
print ("GUERRIER JOUEUR:    pv: ",pv_user, "   Potion de soin: ", soin_user, "    Coup special: ", special_user)
print ("GUERRIER IA:        pv: ",pv_pc,   "   Potion de soin: ", soin_pc,   "    Coup special: ", special_pc)
print ("-------------------------------------------------------------------------------------------------------")

while pv_user > 0 and pv_pc > 0:
   # tour joueur
    count_tour = count_tour + 1
    print( "TOUR(S)=", count_tour)
    print("Coup de poing= '1'(1 à 9 dg); Coup de pied= '2' (5 à 15 dg); Coup de boule= '3' (10 à 30 dg); Coup special= '4' (40 dg); Potion de soin= '5'")
  
    print ("-------------------------------------------------------------------------------------------------------")

    pv_pc = pv_pc - attaque.lancer_attaque(int(input("Choix = ")))
    """ elif choix == 4: 
        if special_user <=0:
            pert_user = random.randrange(1,10,1)
            pv_user = pv_user - pert_user
            print ("Tu n'as plus assez de Mana pour un coup special! Tu perds -", pert_user, "pv")
        else: 
            print("Je prépare mon coup spécial...              KAAMMEEHHAAMMEEHHAA!!")
            pv_pc = pv_pc - 40
            if special_user > 0:
                special_user = special_user - 1
                print ("Le GUERRIER JOUEUR a infligé au GUERRIER IA 40 pv de dégats; Il lui reste ", pv_pc, "pv")
            else:
                special_user = 0
    elif choix == 5:
        if soin_user <= 0:
            print ("Tu n'as plus de potions de soin! Tu passes ton tours!")
        else:
            print("je consomme 1 potion de soin")
            sante = random.randrange(1,30,1)
            pv_user = pv_user + sante
            soin_user = soin_user - 1
            print ("En buvant cette potion, tu regagnes +", sante,"pv. Mais il ne te reste plus que ", soin_user, "potion(s)")
        else:
        print ("Tu passes son tour; Il reste ", pv_pc, "pv au guerrier ia.") """

    print ("-----------------")
    # tour ia

    pv_user = pv_user - attaque.lancer_attaque(random.randrange(1,6,1))
    print ("Le GUERRIER IA a infligé au GUERRIER JOUEUR", attaque.lancer_attaque(choix) , "pv de dégats; Il lui reste ", pv_user, "pv")
    """     elif choix == 4: 
            if special_pc <=0:
                pert_pc = random.randrange(1,10,1)
                pv_pc = pv_pc - pert_pc
                print ("Le GUERRIER IA n'a plus assez de Mana pour un coup special! il perd -", pert_pc, "pv")
            else:
                print("Le GUERRIER IA fait un coup spécial...              KAAMMEEHHAAMMEEHHAA!!")
                pv_user = pv_user - 40
                if special_pc > 0:
                    special_pc = special_pc - 1
                    print ("Le GUERRIER IA a infligé au GUERRIER JOUEUR 40 pv de dégats; Il reste ", pv_user, "pv") 
                else:
                    special_pc = 0
        elif choix == 5:
            if soin_pc <= 0:
                print ("Il tente de trouver une potion dans son inventaire...  Mais il constate qu'il n'en a plus! Il passe alors son tours!")
            else:
                print("Le GUERRIER IA consomme 1 potion de soin")
                sante = random.randrange(1,30,1)
                pv_pc = pv_pc + sante
                soin_pc = soin_pc - 1
                print ("En buvant cette potion, le GUERRIER IA regagne +", sante,"pv. Mais il ne lui reste plus que ", soin_pc, "potion(s)")
        else:
            print ("Le guerrier ia est choqué! Donc, il passe son tour; Il lui reste ", pv_pc, "pv") """

        #Bilan fin de tours
    print ("-------------------------------------------------------------------------------------------------------")
    print ("TOUR BONUS")
    if count_tour == 5 or count_tour == 10 or count_tour == 15 or count_tour == 20 or count_tour == 25:
        special_user = special_user + 1
        special_pc = special_pc + 1
        print("Tous les 5 tours, le GUERRIER JOUEUR et GUERRIER IA gagne chacun +1 coup special!")
    # vie faible +1 coup special!
    if pv_user <= 10 and pv_user > 0:
        special_user = special_user + 1
        print("Le GUERRIER Joueur a une vie très faible. Mais il mise sur l'espoir pour contre-attaquer! +1 coup special!")
    if pv_pc <= 10 and pv_pc > 0:
        special_pc = special_pc + 1
        print("Le GUERRIER IA a une vie très faible. Mais il mise sur l'espoir pour contre-attaquer! +1 coup special!")
    #soin bonus
    if soin_user ==0:
        print("Plus de potion de soin? 1 chance sur 5 pour en trouver une!")
        chance = random.randrange(1,5,1)
        if chance == 1:
            soin_user = soin_user +1
            print ("Tu as de la chance! le GUERRIER JOUEUR trouve +1 potion de soin")
        else:
            soin_user = 0
            print("Pas de bol! Tu n'a pas pu trouver de potion à temps")
    if soin_pc ==0:
        chance = random.randrange(1,5,1)
        if chance == 1:
            soin_user = soin_pc+1
            print ("ZUT! Le GUERRIER IA a trouvé +1 potion de soin")
    # dernier coup?
    if (pv_user < -2 and pv_user >= -15 and special_user >= 1):
        #esquive
        chance = random.randrange(1,2,1)
        if chance == 1:
            print("Le GUERRIER IA esquive la dernière attaque du GUERRIER JOUEUR")
        else:
            degat = random.randrange(10,20,1)
            pv_pc = pv_pc - degat
            print("Une attaque desesperée! le GUERRIER JOUEUR inflige au GUERRIER IA -", degat)
    if (pv_pc < -2 and pv_pc >= -15 and special_pc >= 1):
        #esquive
        print("1 chance sur 2 d'esquiver la dernière attaque du GUERRIER IA! Choisir entre '1' et '2'!")
        choix = int(input("choix = "))
        if choix == random.randrange(1,2,1):
            print("Le GUERRIER JOUEUR esquive la dernière attaque du GUERRIER IA")
        else:
            degat = random.randrange(10,20,1)
            pv_user = pv_user - degat
            print("Une attaque desesperée! le GUERRIER IA inflige au GUERRIER JOUEUR -", degat)

    print ("-------------------------------------------------------------------------------------------------------")
    print ("BILAN DU TOUR(s)", count_tour)
    print ("GUERRIER JOUEUR:    pv: ",pv_user, "   Potion de soin: ", soin_user, "    Coup special: ", special_user)
    print ("GUERRIER IA:        pv: ",pv_pc,   "   Potion de soin: ", soin_pc,   "    Coup special: ", special_pc)
    print ("-------------------------------------------------------------------------------------------------------")
    print ("-------------------------------------------------------------------------------------------------------")
# BILAN
print("FIN DE PARTIE!")
if pv_pc >= 10 or pv_user >= 10:
    if pv_pc > 10:
        print("LE GUERRIER IA DOMINE COMPLETEMENT SON ADVERSAIRE!!!")
        score = pv_pc + soin_pc + special_pc - 10
        print("SCORE= ", score, "pt")
    else:
        print("LE GUERRIER JOUEUR DOMINE COMPLETEMENT SON ADVERSAIRE!!!")
        score = pv_user + soin_user + special_user - 10
        print("SCORE= ", score, "pt")
elif pv_pc >= 0 or pv_user >=0:
    if pv_pc >= 0:
        print("LE GUERRIER IA GAGNE DE JUSTESSE!!!")
        score = 5 + soin_pc + special_pc
        print("SCORE= ", score, "pt")
    else:
        print("LE GUERRIER JOUEUR GAGNE DE JUSTESSE!!!")
        score = 5 + soin_user + special_user
        print("SCORE= ", score, "pt")
else:
    if pv_pc > pv_user:
        print("LE GUERRIER IA GAGNE AVEC DIFFICULTER")
        score = soin_pc + special_pc
        print("SCORE= ", score, "pt")
    else:
        print( "LE GUERRIER JOUEUR GAGNE AVEC DIFFICULTER")
        score = soin_user + special_user
        print("SCORE= ", score, "pt")
print ("-------------------------------------------------END----------------------------------------------------")