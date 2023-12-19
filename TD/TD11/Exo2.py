from numpy import *
import matplotlib.pyplot as plt
from random import randint




def graphique1(dico):
    n = len(dico)
    plt.figure(figsize=(12,20))
    for k, i in zip(dico.keys(), range(1, n + 1)) :
        x = arange(0, len(dico[k]))
        plt.subplot(n, 1, i)
        plt.plot(x, dico[k])
        plt.title(k)
    plt.show()

    

def graphique2(dico) :
    n = len(dico)
    plt.figure(figsize=(12,20))
    for k in zip(dico.keys(), range(1, n + 1)) :
        x = arange(0, len(dico[k]))
        couleur= input("Choisissez la couleur de cette courbe parmis blue/green/red/cyan/magenta/yellow/black/maroon : \n")
        plt.plot(x, dico[k], color=couleur)   
    plt.title('Graphiques')
    plt.show()


def affiche_stats(dico) :
    n = len(dico)
    for k, i in zip(dico.keys(), range(n)) :
        print(f"Graphique {i} : min = {dico[k].min()} max = {dico[k].max()} moyenne = {dico[k].mean()} écart type = {dico[k].std()}")


def graphique3(dico) :
    n = len(dico)
    plt.figure(figsize=(12,20))
    for k in zip(dico.keys(), range(1, n + 1)) :
        x = arange(0, len(dico[k]))
        plt.plot(x, dico[k].min())
        plt.plot(x, dico[k].max())
        plt.plot(x, dico[k].var())
        plt.legend(k)
    plt.show()



    for k, i in zip(dico.keys(), range(n)) :
        print(f"Graphique {i} : min = {dico[k].min()} max = {dico[k].max()} moyenne = {dico[k].mean()} écart type = {dico[k].std()}")

n = int(input("Combien de courbes voulez vous ? "))
jeux = {f"jeux {i}" : random.randn(20) for i in range(n) }

graphique1(jeux)

reshape()