#definition d'une variable
fichier = "FIFA_World_Cup/random.txt"

#ouvre le fichier, découpe le fichier ligne par ligne et virgule par virgule pour séparer les champs
with open(fichier, "r") as fichierMain:
    contenueMain = fichierMain.readlines()
    liste_main = [ligne.strip().split(",") for ligne in contenueMain]

#print la liste random
for equipe in liste_main:
    print(equipe)
#tri la liste par position 
liste_tri = sorted(liste_main, key=lambda pos: int(pos[0])) 
#print en colonne
for equipe in liste_tri:
    print(equipe)
