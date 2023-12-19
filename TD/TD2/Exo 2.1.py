from Exo_2 import*

def affiche_test_cm(*args) :
    for i in args :
        if magique(i) == False :
            print("Ce carré n'est pas magique")
        else :
            print("Ce carré est magique")
            if carre_magique_normal(i) == False :
                print("Ce carré magique n'est pas normal")
            else :
                print("Ce carré magique est normal")
         



Carre= [[8, 1, 6], [3, 5, 7], [4, 9, 2]]
affiche_test_cm(Carre)
