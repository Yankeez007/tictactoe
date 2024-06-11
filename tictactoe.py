#projet morpion, on va cree un jeu où deux joueurs vont d'affronter sur un plateau 3x3 et le but est de formé une ligne de trois symboles identiques

#on va cree le plateau de jeu
def initialiser_plateau():
    plateau = [["","",""],["","",""],["","",""]]
    return plateau 
#on va maintenant l'afficher
def afficher_plateau(plateau):
    initialiser_plateau()
    for i in range(3):
        print(plateau[i])