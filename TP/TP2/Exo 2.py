def crypter(ch) :
    mot_décalé = [] #On crée la liste qui va contenir le texte crypté
    ponctuation =('.', ',', ' ', '!', '?') #On dresse la liste de la ponctuation
    for i in range(len(ch)) :
        if ch[i] in ponctuation : 
            mot_décalé.append(ch[i]) #La ponctuation ne doit pas changer donc on la laisse telle quelle
        elif ch[i] == 'z' :
            mot_décalé.append('a') #Cela nous permet de remonter au début de l'alphabet 
        elif ch[i] == 'Z' :
            mot_décalé.append('A')
        else :
            z = chr(ord(ch[i])+1) #On décale la lettre d'une place
            mot_décalé.append(z) #On ajjoute la lettre décalée à la liste cryptée
    mot_décalé = ''.join(mot_décalé) #On transforme la liste en chaîne de caractère
    return mot_décalé

x = input('Entrez un texte ')
y = crypter(x)
print(y)
