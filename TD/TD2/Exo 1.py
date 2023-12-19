def nombre(fonction):
    def wrapper(x) :
        chiffres = ('0123456789')
        chiffre = True
        if type(x) == str :
            for i in x :
                if i not in chiffres :
                    chiffre = False
            if chiffre == True :
                x = int(x)
                return fonction(x)
            elif  type(x) == int :
                return fonction(x)
            else :
                return fonction(0)
    return wrapper

@nombre
def somme_chiffres(x) :
    s = 0
    x = str(x)
    for i in x :
        c = int(i)
        s = s + c
    return(s)

@nombre
def nombre_chiffres(x) :
    x = str(x)
    n = len(x)
    print(n)

@nombre
def separe_nombre(x) :
    y = 0
    x = str(x)
    partie_droite = []
    partie_gauche = []
    for i in x :
        if y >= len(x)/2 :
            partie_gauche.append(i)
            y = y + 1
        else :
            partie_droite.append(i)
            y = y + 1
    partie_d = int( "".join(partie_droite))
    partie_g = int( "".join(partie_gauche))
    return partie_d, partie_g

couicable = True 


x = input('Entrez un nombre entier : \n')
if len(x)%2 == 0 :
    d, g = separe_nombre(x)
    somme_partie_droite = somme_chiffres(d)
    somme_partie_gauche = somme_chiffres(g)

    print(d,g,somme_partie_droite,somme_partie_gauche)

    if somme_partie_droite != somme_partie_gauche :
        couicable = False
    if len(str(d)) != len(str(g)) :
        couicable = False

    if couicable == True :
        print(x, 'est couicable')
    else :
        print(x, "n'est pas couicable")
else :
    print("Ce nombre ne comporte pas un nombre de chiffres pair, veullez en entrer un autre")