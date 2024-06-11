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
    return plateau[ligne, colonne]==""

#on va cree une fonction qui ajoute un symbole au plateau
# joueur = 'X' soit 'O'
def ajouter_coup(plateau, ligne, colonne, joueur):
    if est_libre(plateau, ligne, colonne):
        plateau[ligne, colonne]=joueur
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

plateau = initialiser_plateau()
afficher_plateau(plateau)


## ICI : PS C:\Users\youle>python tictactoe.py