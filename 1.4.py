#ouvrir le fichier en 'r' read
fichier = open("FIFA_World_Cup/FIFA-2022.txt", "r")
#ouvrir le fichier en 'w' donc ecriture mais il n'existe pas donc création
new_fichier = open("FIFA_World_Cup/New-FIFA-2022.txt", "w")
#copier coller
text = fichier.read()
new_fichier.write(text)
#fermeture des fichiers
fichier.close
new_fichier.close
