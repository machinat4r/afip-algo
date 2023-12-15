import pandas as pd

fichier = open("FIFA_World_Cup/FIFA-2022.txt", "r")

with open('FIFA_World_Cup/FIFA-2022.txt', 'r') as f:
    lines = f.readlines()

f = fichier.readlines()

liste = []


for line in lines:
    columns = line.strip().split(',')
    liste.append(columns)


mactrice = pd.DataFrame(liste)


del liste[0]


mactrice = pd.DataFrame(liste, columns=['Position', 'Team', 'Games Played', 'Win', 'Draw', 'Loss', 'Goals For', 'Goals Against', 'Goal Difference', 'Points'])


mactrice['Win'] = mactrice['Win'].astype('int')
mactrice['Draw'] = mactrice['Draw'].astype('int')


mactrice['Calcul'] = 3 * mactrice['Win'] + mactrice['Draw']

pts = mactrice['Calcul']

pts_liste = pts.to_list()

pts_liste = [str(element)for element in pts_liste]


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
    

liste_ekip = []


for ligne in f:
    liste_ekip.append(recup_ekip(ligne))

del liste_ekip[0]


for equipe in liste_ekip:
    print(equipe + ":" + " " + pts_liste[liste_ekip.index(equipe)] + " " + "pts")