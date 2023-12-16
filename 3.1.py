import pandas as pd

mactrice = pd.read_csv('FIFA_World_Cup/FIFA-2022.txt', thousands=',')

sup = mactrice.drop("Points", axis=1)

sup.to_csv('FIFA_World_Cup/Colonn-sup.txt', index=False)