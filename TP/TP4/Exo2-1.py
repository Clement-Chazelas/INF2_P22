from turtle import color
import numpy as np
import matplotlib.pyplot as plt

def cercle(x ,y ,r) :
    figure, axes = plt.subplots()
    axes.set_aspect(1)
    plt.xlim(-r - 5 ,r + 5)     #On défini la taille de l'affichage
    plt.ylim(-r - 5, r + 5)
    for i in range(r) :
        couleur= input("Choisissez la couleur de ce cercle parmis blue/green/red/cyan/magenta/yellow/black/maroon : \n")    #On demande à l'utilisateur de choisir la couleur du cercle parmis différentes couleurs proposées
        draw_circle = plt.Circle((x, y), r,fill=False, color=couleur)   #On crée le cercle de centre (x,y) et de rayon r de la couleur choisie précedement
        axes.add_artist(draw_circle)
        r = r - 1
    plt.title('Cercle')
    plt.show()

def main() :
    x = int(input("Entrez les abscisses du centre du cercle :  "))
    y = int(input("Entrez les abscisses du centre du cercle :  "))
    r = int(input("Entrez le rayon du cercle :  "))
    cercle(x,y,r)

if __name__ == '__main__' :
    main()