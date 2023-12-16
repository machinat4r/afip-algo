fichier = "FIFA_World_Cup/random.txt"


with open(fichier, "r") as fichierMain:
    contenueMain = fichierMain.readlines()
    liste_main = [ligne.strip().split(",") for ligne in contenueMain]


for equipe in liste_main:
    print(equipe)

liste_tri = sorted(liste_main, key=lambda pos: int(pos[0])) 

for equipe in liste_tri:
    print(equipe)
