fichier = open("FIFA_World_Cup/FIFA-2022.txt", "r")

f = fichier.readlines()

liste_vide = []

for ligne in f:
    if(ligne[-1] == "\n"):
        liste_vide.append(ligne[:-1])
    else:
        liste_vide.append(ligne)


del liste_vide[0]

trois_premieres_lettres = [pays[2:5] for pays in liste_vide]
print(trois_premieres_lettres)