#import de l'addon/bibliotheque pandas qui fait des matrices et as qui un racourcis pour pandas
import pandas as pd
#convertion du txt en mactice 
mactrice = pd.read_csv('FIFA_World_Cup/FIFA-2022.txt', thousands=',')
#supression de la colonne Points 
sup = mactrice.drop("Points", axis=1)
#colle le résultat dans un document sans l'index 
sup.to_csv('FIFA_World_Cup/Colonn-sup.txt', index=False)