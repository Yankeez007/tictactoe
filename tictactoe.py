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

#on va faire une fonction qui va verifier le gagnant de la partie donc avec les trois symboles alignés
def verifier_gagnant(plateau, joueur):
    for i in range(3):
        if (plateau[i][0]==joueur and plateau[i][1]==joueur and plateau[i][2]==joueur):
            return True
        elif (plateau[0][i]==joueur and plateau[1][i]==joueur and plateau[2][i]==joueur):
            return True
        elif (plateau[i][i]==joueur and plateau[i][i]==joueur and plateau[i][i]==joueur):
            return True
        else :
            return False
    if (plateau[0][2]==joueur and plateau[1][1]==joueur and plateau[2][0]==joueur):
            return True

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
    position = input() # position -> '1 2' 
    if len(position) != 3 :
        print("coup invalide ! ")
        return -1

    ligne = int(position[0]) # 1 en int entre 0 et 2 
    colonne = int(position[2]) # 2 en int entre 0 et 2
    if ligne >= 0 and ligne <= 2 and colonne <= 2 and colonne >= 0 :
        return (ligne, colonne)
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
    afficher_plateau(plateau)
    joueur1 = "x"
    joueur2 = "o"
    while not est_plein(plateau) or (not verifier_gagnant(plateau, joueur1) or not verifier_gagnant(plateau, joueur2)):
        coup_j1 = demander_coup(joueur1)
        ajouter_coup(plateau, coup_j1[0], coup_j1[1], joueur1)
        coup_j2 = demander_coup(joueur2)
        ajouter_coup(plateau, coup_j2[0], coup_j2[1], joueur2)
        if est_plein(plateau):
            return "le plateau est plein, fin de partie, match nul"
        elif verifier_gagnant(plateau, joueur1):
            return "le joueur 1 à gagné !"
        elif verifier_gagnant(plateau, joueur2):
            return "le joueur 2 à gagné !"
        
        




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


## ICI : PS C:\Users\youle>python tictactoe.py