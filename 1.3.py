fichier = open("FIFA_World_Cup/FIFA-2022.txt", "r")

f = fichier.readlines()


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
    print(equipe)