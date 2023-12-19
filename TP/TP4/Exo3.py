import csv  #On impote toutes le bibliothèques que l'on va utiliser
import numpy as np
import matplotlib.pyplot as plt

def ecrire() :
   with open("math.csv", "w", newline='') as fichier :  #on ouvre/crée le fichier math.csv et on fait ensorte qu'il n'y ait pas de retour à laligne non nécessaire
       math = csv.writer(fichier)
       for i in range(-50,51, 1) :  #On fait une boucle afin de stocker suffisament de valeur entre -5 et 5
           x = i/10
           y = np.cos(x)
           math.writerow([x,y])     #Chaque ligne sera donc composée de la valeur du x et ensuite de celle du y
    
           
def lire() :
    x = []      #On crée deux listes vides qui vont ensuite contenir les valeurs de x et y
    y = []
    with open("math.csv", "r", newline='') as fichier :     #On ouvre le fichier et on le lit
        contenu = csv.reader(fichier)
        for i in contenu :
            print(i)    #On affiche le fichier
            x.append(float(i[0]))       #On ajoutes les valeurs de x et les valeurs de y dans leurs listes respectives
            y.append(float(i[1]))
    plt.xlim(-6 ,6)     #On délimite l'affichage
    plt.ylim(-1.2, 1.2)
    plt.plot(x, y)      #On trace la courbe
    plt.title("Fonction cosinus")       #On donne un titre au graphique
    plt.show()      #On affiche le graphique


def main() :
    ecrire()
    lire()


if __name__ == '__main__' :
    main()
