fichier = "FIFA_World_Cup/FIFA-2022.txt"


with open(fichier, "r") as fichierMain:
    contenueMain = fichierMain.read()


with open("FIFA_World_Cup/New-FIFA-alt-2022.txt", "w") as fichierCopie:
    fichierCopie.write(contenueMain)
    