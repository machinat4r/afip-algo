#import de l'addon/bibliotheque pandas qui fait des matrices et as qui un racourcis pour pandas
import pandas as pd
#ouvrir le fichier
fichier = open("FIFA_World_Cup/FIFA-2022.txt", "r")

with open('FIFA_World_Cup/FIFA-2022.txt', 'r') as f:
    lines = f.readlines()
#fonction lire/récuperer les lines pour en faire un index d'une ligne
f = fichier.readlines()
#créer une liste
liste = []

#découpe le contenue de la liste pour que ça rentre parfaitement dans la matrice
for line in lines:
    columns = line.strip().split(',')
    liste.append(columns)

#creation de la mactrice
mactrice = pd.DataFrame(liste)

#suprimme la premiere ligne
del liste[0]

#initialisation de la colonne 
mactrice = pd.DataFrame(liste, columns=['Position', 'Team', 'Games Played', 'Win', 'Draw', 'Loss', 'Goals For', 'Goals Against', 'Goal Difference', 'Points'])

#les colonnes en int
mactrice['Goals For'] = mactrice['Goals For'].astype('int')
mactrice['Goals Against'] = mactrice['Goals Against'].astype('int')
#calcule 
mactrice['Calcul'] = mactrice['Goals For'] - mactrice['Goals Against']
#creation de variable
pts = mactrice['Calcul']
#on fait une liste du calcul
pts_liste = pts.to_list()
#re en str
pts_liste = [str(element)for element in pts_liste]

#création de fonction pour cibler dans un index, separer et recuperer les données
def recup_ekip(ligne):


    sepa = ","
    acc = 0
    sequence = []


    for pos_actu in ligne:
        if pos_actu == sepa:
            acc = acc + 1
        if acc > 0 and acc <= 1 and pos_actu != sepa:
            sequence += pos_actu
    return sequence[0] + sequence[1] + sequence[2]
    
#créer une liste
liste_ekip = []

# boucle for qui recupère les 3 lettres de la fonction et qui les met dans la liste
for ligne in f:
    liste_ekip.append(recup_ekip(ligne))
#suprimme la premiere ligne 
del liste_ekip[0]

#concaténation 
for equipe in liste_ekip:
    print(equipe + ":" + " " + pts_liste[liste_ekip.index(equipe)] + " " + "but(s) d'écart(s)")