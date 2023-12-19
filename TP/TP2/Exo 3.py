from string import ascii_lowercase, ascii_uppercase #On importe l'alphabet minuscule et l'alphabet majuscule

def nb_min(password) :
    min =0
    for i in password :
        if i in ascii_lowercase : #On regarde un à un les caractères du password et si ils appartienent aux lettres minuscules on incrémente le compteur de 1
            min = min + 1
    return min 

def nb_maj(password) :
    maj =0
    for i in password :
        if i in ascii_uppercase : #On regarde un à un les caractères du password et si ils appartienent aux lettres majuscule on incrémente le compteur de 1
            maj = maj + 1
    return maj 

def nb_alpha(password) :
    x = 0
    for i in password :
        if i not in ascii_lowercase and i not in ascii_uppercase : #On regarde un à un les caractères du password et si ils n'appartienent pas aux lettres minuscules ou majuscules on incrémente le compteur de 1
            x = x +1
    return x    

def long_min(password) :
    longueur_max = 0
    longueur = 0
    for i in password :
        if i in ascii_lowercase : #On regarde un à un les caractères du password et si c'est une minuscule on incrémente la longueur de 1
            longueur = longueur + 1
            if longueur > longueur_max : #On fait ceci car si le mdp se termine par une minuscule on ne rentre pas dans la boucle d'après et la dernière chaîne de lettres minuscules n'est pas prise en compte
                longueur_max = longueur
        else :
            if longueur > longueur_max : #Ceci nous permet de garder en mémoire la longueure de la plus grande chaîne de minuscule
                longueur_max = longueur
            longueur = 0 #On réinitialise la longueur à 0 pour la prochaine chaîne de lettres minuscule, s'il y en a
    return longueur_max

def long_maj(password) :
    longueur_max = 0
    longueur = 0
    for i in password : 
        if i in ascii_uppercase : #On regarde un à un les caractères du password et si c'est une majuscule on incrémente la longueur de 1
            longueur = longueur + 1
            if longueur > longueur_max : #On fait ceci car si le mdp se termine par une majuscule on ne rentre pas dans la boucle d'après et la dernière chaîne de lettres majuscule n'est pas prise en compte
                longueur_max = longueur
        else :
            if longueur > longueur_max : #Ceci nous permet de garder en mémoire la longueure de la plus grande chaîne de majuscule
                longueur_max = longueur
            longueur = 0 #On réinitialise la longueur à 0 pour la prochaine chaîne de lettres majuscule, s'il y en a
    return longueur_max

def score(password) :
    score_password = 4*len(password) + 2*(len(password) - nb_maj(password)) + 3*(len(password) - nb_min(password)) + 5*nb_alpha(password) - 3*long_maj(password) - 2*long_min(password) #On calcule le score avec la convention qui nous a été fournie
    if score_password < 20 :
        return 'Très faible'
    elif score_password < 40 :
        return 'Faible'
    elif score_password < 80 :
        return 'Fort'
    else :
        return 'Très fort'



mot_de_passe = input('Entrez votre mot de passe : \n')
print(score(mot_de_passe))