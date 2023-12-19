from math import *

liste_x = []
liste_y = []
lecture = False
x = int(input("Entrez la valeur min : \n"))
xmax = int(input("Entrez la valeur max : \n"))

fichier = open("distance_sinus.txt", "w")
fichier.write("sin(x)          Distance a l'origine\n")
while x != xmax + 1 :
    Sin = sin(x)
    distance = sqrt(x**2 + sin(x)**2)
    fichier.write(f'{Sin:.3f}           {distance:.3f}\n')
    x = x + 1
fichier.close()

if input("Voulez vous lire le fichier (oui/non") == "oui" :
    lecture = True
else :
    lecture = False

if lecture :
    with open("distance_sinus.txt", "r") as fichier :
        texte = fichier.readlines()
        for ligne in texte :
            coord = ligne.split(' ')
            liste_x.append (float(coord[0]))
            liste_y.append (float(coord[1]))
    for i in range(len(liste_x)) :
        print(liste_x[i])
        print(liste_y[i])