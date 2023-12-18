#ouvrir le fichier
fichier = open("FIFA_World_Cup/FIFA-2022.txt", "r")
#fonction lire/récuperer les lines pour en faire un index d'une ligne
f = fichier.readlines()
#créer une liste 
liste_vide = []
#boucle for qui prend ligne par ligne sans les \n de revoi de ligne et prend les ligne meme s'il a pas de \n
for ligne in f:
    if(ligne[-1] == "\n"):
        liste_vide.append(ligne[:-1])
    else:
        liste_vide.append(ligne)

#suprime l'index 1 donc 0 dans la liste 
del liste_vide[0]
#affiche la liste dans la console/terminale
print(liste_vide)
