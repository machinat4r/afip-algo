
import os
#charge les donné a partir d'un fichier
def load_data(fileName):
    f = open(fileName,"r")
    #print(f.read())
    data = [];
    for x in f:
        data += [x];
    return data;

