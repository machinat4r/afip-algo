#import de l'addon/bibliotheque random 
import random

#ouvrir le fichier
fichier = open("FIFA_World_Cup/FIFA-2022.txt", "r")

#créer une liste
liste_vide = []

#fonction lire/récuperer les lines pour en faire un index d'une ligne
f = fichier.readlines()

#boucle for qui prend ligne par ligne sans les \n de revoi de ligne et prend les ligne meme s'il a pas de \n 
for ligne in f:
    if(ligne[-1] == "\n"):
        liste_vide.append(ligne[:-1])
    else:
        liste_vide.append(ligne)
#suprimme la premiere ligne 
del liste_vide[0]

#melange les valeurs contenue dans la liste
random.shuffle(liste_vide)

#print en colonne
for equipe in liste_vide:
    print(equipe)

#modifie le fichier random pour le 3.3
with open("FIFA_World_Cup/random.txt", "w") as fichierCopie:
    for equipe in liste_vide:
        fichierCopie.write(equipe + '\n')

