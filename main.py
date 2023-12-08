from functions import *

# Nom de fichier à charger
fileName = "FIFA_World_Cup/FIFA-2022.txt";


manger = "FIFA_World_Cup/manger.txt"

#Charge un fichier en lecture
file = open(fileName, "r")

# Charge les données à partir d'un fichier
#data = load_data(fileName);


liste_raw = lire_fichier(fileName)


#liste_pur = supprimer_ligne(liste_raw)

print(liste_raw)

