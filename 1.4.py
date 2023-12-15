fichier = open("FIFA_World_Cup/FIFA-2022.txt", "r")
new_fichier = open("FIFA_World_Cup/New-FIFA-2022.txt", "w")

text = fichier.read()
new_fichier.write(text)

fichier.close
new_fichier.close
