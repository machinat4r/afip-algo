#ouvrir le fichier
fichier = open("FIFA_World_Cup/FIFA-2022.txt", "r")
#fonction lire/récuperer les lines pour en faire un index d'une ligne
f = fichier.readlines()

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
#suprimme la premiere ligne tea
del liste_ekip[0]
#tri par ordre alphabetique
liste_tri = sorted(liste_ekip)

#print en colonne
for equipe in liste_tri:
    print(equipe)
