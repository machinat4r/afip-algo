
import os
#charge les donné a partir d'un fichier
#def load_data(fileName):
#    f = open(fileName,"r")
#    print(f.read())


#metre les donné dans une liste    1.
def lire_fichier(fileName):
    with open(fileName, "r") as fichier:
        lignes = fichier.readlines()
    for ligne in lignes:
        print(ligne)




#supprimer la premiere ligne de la liste 
def supprimer_ligne(fileName):
    with open(fileName, "r") as fichier:
        lignes = fichier.readlines()
    for ligne in lignes:
        print(ligne)