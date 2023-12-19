import csv
import os
from affichage_graphique import affiche_courbe

taux = []
année = []
os.chdir("C:/Users/clemc/Desktop/UTC/TC02/INF2/TD/TD7")
with open("co2-annmean-mlo.csv", "r") as fichier :
    contenu = csv.reader(fichier)
    for i in contenu :
        print(i)
        try :
            année.append(float(i[0][0:4]))
            taux.append(float(i[1]))
        except :
            pass
    affiche_courbe(année, taux, "Evolution taux CO²", "Année", "Taux de CO²")