import collections as col
import random

def elimination(liste) :
    file = col.deque(liste)
    while len(file) > 1 :
        nb_passes = random.randint(1,10)
        print(nb_passes)
        file.rotate(-nb_passes)
        file.popleft()
        print(file)
    print(f"Le gagnant est {file[0]}")


joueurs = []
nb_joueur = int(input("Combien y a-t-il de joueur ?\n"))
for i in range(nb_joueur) :
    j = input("Entrez le joueur\n")
    joueurs.append(j)

elimination(joueurs)