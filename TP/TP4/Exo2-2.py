from turtle import color
import numpy as np
import matplotlib.pyplot as plt

def cercle(x ,y ,r) :
    figure, axes = plt.subplots() 
    axes.set_aspect(1)
    z = int(input("Entrez la taille de la pyramide :  ")) #On demande à l'utilisateur la taille de la pyramide
    plt.xlim(-r - z*2*r ,r + z*2*r)  #On défini la taille de l'affichage
    plt.ylim(-r - z*2*r, r + z*2*r)
    for i in range(z) :
        for j in range(z - i) :   #On fait une boucle dans une boucle afin de pouvoir afficher une pyramide
            couleur= input("Choisissez la couleur de ce cercle parmis blue/green/red/cyan/magenta/yellow/black/maroon : \n")    #On demande à l'utilisateur de choisir la couleur du cercle parmis différentes couleurs proposées
            draw_circle = plt.Circle((x, y), r,fill=False, color=couleur)   #On crée le cercle de centre (x,y) et de rayon r de la couleur choisie précedement
            axes.add_artist(draw_circle)    #On trace le cercle
            x = x + 2*r     #On se décale du diamètre sur l'axe des abscisses afin que le prochain cercle soit collé à celui que l'on vient de tracer
        x = x - (z-i-0.5)*2*r   #Une fois la ligne fini (boucle for j) on replace les abscisses un rayon plus loins que la ligne du dessous
        y = y + 2*r     #Comme la ligne est finie on passe à celle plus haut en augmentant les ordonnées du diamètre
    plt.title('Pyramide de cercle')     #On met un titre au graphique
    plt.show()      #On affiche le graphique

def main() :
    x = int(input("Entrez les abscisses du centre du cercle :  "))
    y = int(input("Entrez les abscisses du centre du cercle :  "))
    r = int(input("Entrez le rayon du cercle :  "))
    cercle(x,y,r)

if __name__ == '__main__' :
    main()