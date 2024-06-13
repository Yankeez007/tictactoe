#projet morpion, on va cree un jeu où deux joueurs vont d'affronter sur un plateau 3x3 et le but est de formé une ligne de trois symboles identiques

#on va cree le plateau de jeu
def initialiser_plateau():
    plateau = [["","",""],
               ["","",""],
               ["","",""]]
    return plateau 
#on va maintenant l'afficher
def afficher_plateau(plateau):
    for i in range(3):
        print(plateau[i])

#cree une fonction qui verifie les cases
def est_libre(plateau, ligne, colonne):
    return plateau[ligne][colonne]==""

#on va cree une fonction qui ajoute un symbole au plateau
# joueur = 'X' soit 'O'
def ajouter_coup(plateau, ligne, colonne, joueur):
    if est_libre(plateau, ligne, colonne):
        plateau[ligne][colonne]=joueur
    else:
        print("la case n'est pas libre")
        return -1

#on va faire une fonction qui va verifier le gagnant de la partie donc avec les trois symboles alignés
def verifier_gagnant(plateau, joueur):
    for i in range(3):
        if (plateau[i][0]==joueur and plateau[i][1]==joueur and plateau[i][2]==joueur):
            return True
        elif (plateau[0][i]==joueur and plateau[1][i]==joueur and plateau[2][i]==joueur):
            return True
    if (plateau[0][0]==joueur and plateau[1][1]==joueur and plateau[2][2]==joueur):
            return True
    elif (plateau[0][2]==joueur and plateau[1][1]==joueur and plateau[2][0]==joueur):
            return True
    return False

#maintenant nous allons verifier si le plateau est rempli ou non
def est_plein(plateau):
    for i in range(3):
        for j in range(3):
            if plateau[i][j]=="":
                return False
    return True

#on va maintenant demander aux joueurs de faire un coup 

def demander_coup(joueur):
    # la fonction va demander un coup au joueur et renvoi la position sous forme de tuple (ligne,colonne) ou -1 coup invalide
    print("au tour de :", joueur)
    position = input("Donnez votre coup :") # position -> '1 2' et on va aussi demander le coup directement dans le input
    #on va modifier la condition et faire au cas par cas (pour corriger l'erreur quand on rentre un coup invalide)
    #on va utiliser la méthode .isdigit() car je viens de la voir dans les sites pythons et qu'elle est utile dans ce cas
    if (len(position) == 3) and (position[1] == " ") and (position[0].isdigit()) and (position[2].isdigit()):
        ligne = int(position[0]) # 1 en int entre 0 et 2 
        colonne = int(position[2]) # 2 en int entre 0 et 2
        if ligne >= 0 and ligne <= 2 and colonne <= 2 and colonne >= 0 :
            return (ligne, colonne)
        else :
            print("coup invalide ! ")
            return -1    
    else :
        print("coup invalide !")
        return -1

#on va mtn faire la boucle principale du jeu, alterner entre "o" et "x"
def jouer():
    """
    1. on pose un plateau vide 
    2. on demande au joueur d'ajouter un coup
    3. on place le coup sur le plateau si il est valide
    4. on vérifie s'il y a un gagnant
    5. on vérifie si le plateau est plein (match nul ou une victoire)
    6. s'il n'y a pas de gagnant on demande à l'autre joueur de placer un coup
    
    on s'arrete s'il y a un gagnant ou si le plateau est plein
    """
    plateau = initialiser_plateau()
    joueur1 = "x"
    joueur2 = "o"
    joueur_actuel = joueur1 #cette variable va nous servir à alterner entre les deux joueurs
    i = 1 #on crée un indice qui va compter le nombre de tour dans la boucle
    while not est_plein(plateau) or (not verifier_gagnant(plateau, joueur1) or not verifier_gagnant(plateau, joueur2)):
        afficher_plateau(plateau)
        coup = demander_coup(joueur_actuel) #prends la valeur de demander_coup sous la forme d'un couple (ligne,colonne) du joueur actuel
        #une erreur "TypeError: 'int' object is not subscriptable" se produit car il prend en compte le -1 de la fontion demander_coup, ajustons cela
        if coup != -1:
            if ajouter_coup(plateau, coup[0], coup[1], joueur_actuel) == -1 : #si la fonction ajouter_coup renvoi -1 on va demander de reesayer
                    continue #saute l'étape et va à l'itération suivante
            else : 
                if verifier_gagnant(plateau, joueur_actuel): #on verifie s'il y a un gagnant et si oui on return et ça met fin à la boucle
                    afficher_plateau(plateau)
                    return f"Le joueur {joueur_actuel} a gagné !"
                elif est_plein(plateau): #pareil mais pour le plateau plein, on verifie si le plateau est plein
                    afficher_plateau(plateau)
                    return "Le plateau est plein, fin de parti, match nul"
                #maintenant il faut passer au joueurs suivant
                if joueur_actuel == joueur1: #on alterne entre les deux joueurs
                    joueur_actuel = joueur2 
                else :
                    joueur_actuel = joueur1
                i = i + 1 #le tour augmente de 1 à chaque passage dans la boucle si la partie n'est pas terminée
        else :
            print("coup invalide, veuillez réesayer.")
    afficher_plateau(plateau)
    return "fin de la partie"
        





"""
plateau = initialiser_plateau()
afficher_plateau(plateau)
ajouter_coup(plateau, 0, 2, "X")
print(est_libre(plateau, 0, 2))
ajouter_coup(plateau, 0, 0, "X")
ajouter_coup(plateau, 0, 1, "X")
print(f'{verifier_gagnant(plateau, "X")=}')
plateau_plein = [["x","x","o"],["o","o","x"],["x","o","x"]]
print("est_plein(plateau) = ", est_plein(plateau))
print("est_plein(plateau_plein) = ", est_plein(plateau_plein))
#j1="x"
#demander_coup(j1)




#on met les conditions, si le plateau est plein ou qu'il y a un gagnant, la partie est finie sinon on place les coups
        elif est_plein(plateau):
            return "le plateau est plein, fin de partie, match nul"
        elif verifier_gagnant(plateau, joueur1):
            return "le joueur 1 à gagné !"
        elif verifier_gagnant(plateau, joueur2):
            return "le joueur 2 à gagné !"
        elif i % 2 == 0 : #idem mais pour le joueur 2
            if ajouter_coup(plateau, coup_j2[0], coup_j2[1], joueur2) == -1 :
                print("coup invalide, veuillez réessayer.")
            else :
                ajouter_coup(plateau, coup_j2[0], coup_j2[1], joueur2)
                i = i + 1
        elif 
            ajout_coupj1
            if coup_j1 == -1 :
                print("veuillez réessayer")
                ajout_coupj1
            else  :
                afficher_plateau(plateau)
                i = i + 1
        elif 
            if coup_j2 == -1 :
                print("veuillez réessayer")
                ajout_coupj2
            else  :
                afficher_plateau(plateau)
                i = i + 1
            """

jouer()


## ICI : PS C:\Users\youle>python tictactoe.py