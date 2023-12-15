fichier = open("FIFA_World_Cup/FIFA-2022.txt", "r")


liste_vide = []


f = fichier.readlines()


for ligne in f:
    if(ligne[-1] == "\n"):
        liste_vide.append(ligne[:-1])
    else:
        liste_vide.append(ligne)


del liste_vide[0]


tpl = [pays[2:5] for pays in liste_vide]
print(tpl)