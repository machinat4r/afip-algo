import random


fichier = open("FIFA_World_Cup/FIFA-2022.txt", "r")


liste_vide = []


f = fichier.readlines()


for ligne in f:
    if(ligne[-1] == "\n"):
        liste_vide.append(ligne[:-1])
    else:
        liste_vide.append(ligne)

del liste_vide[0]


random.shuffle(liste_vide)


for equipe in liste_vide:
    print(equipe)


with open("FIFA_World_Cup/random.txt", "w") as fichierCopie:
    for equipe in liste_vide:
        fichierCopie.write(equipe + '\n')

