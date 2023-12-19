from math import * #On importe toute les fonctions du module math afin de pouvoir utiliser la fonction sqrt plus tard

class Point : #On définit la classe Point
    def __init__(self, abs, ord) : #On définit le constructeur de la classe Point avec ses attributs
        self.abs = abs
        self.ord = ord
    
    @property #On définit le getter de l'atribut abs
    def abs(self) :
        return self.__abs

    @abs.setter #On definit le setter de l'atribut abs
    def abs(self, abs) :
        if not isinstance(abs, float) : #On verifie que abs est bien un flottant
            raise TypeError("L'abscisse n'est pas un float")
        self.__abs = abs 

    @property #On définit le getter de l'atribut ord
    def ord(self) :
        return self.__ord

    @ord.setter #On definit le setter de l'atribut
    def ord(self, ord) :
        if not isinstance(ord, float) : #On verifie que ord est bien un flottant
            raise TypeError("Les ordonnées ne sont pas un float")
        self.__ord = ord 
    
    def __calculerDistance__(self, p) : 
        if not isinstance(p, Point) : #On verifie que p est bien un Point
            raise TypeError("P n'est pas un Point")
        return sqrt((p.abs - self.abs)**2+(p.ord - self.ord)**2)

    def __calculerMillieu__(self, p) :
        if not isinstance(p, Point) : #On verifie que p est bien un Point
            raise TypeError("P n'est pas un Point")
        return Point((1/2)*(p.abs + self.abs), (1/2)*(p.ord + self.ord))



class TroisPoints : #On définie la classe TroisPoints
    def __init__(self, premier, deuxième, troisième) : #On définit le constructeur de la classe TroisPoints avec ses attributs
        self.premier = premier
        self.deuxième = deuxième
        self.troisième = troisième
    
    @property #On définit le getter de l'atribut premier
    def premier(self) :
        return self.__premier

    @premier.setter #On definit le setter de l'atribut premier
    def premier(self, premier) :
        if not isinstance(premier, Point) : #On verifie que premier est bien un Point
            raise TypeError("Premier n'est pas un Point")
        self.__premier = premier 

    @property #On définit le getter de l'atribut deuxième
    def deuxième(self) :
        return self.__deuxième

    @deuxième.setter #On definit le setter de l'atribut deuxième
    def deuxième(self, deuxième) :
        if not isinstance(deuxième, Point) : #On verifie que deuxième est bien un Point
            raise TypeError("Deuxième n'est pas un Point")
        self.__deuxième = deuxième 

    @property #On définit le getter de l'atribut troisième
    def troisième(self) :
        return self.__troisième

    @troisième.setter #On definit le setter de l'atribut deuxième
    def troisième(self, troisième) :
        if not isinstance(troisième, Point) : #On verifie que troisième est bien un Point
            raise TypeError("P n'est pas un Point")
        self.__troisième = troisième 

    def __sontAlignes__(self, premier, deuxième, troisième) :
        alignés = False #On crée une variable booléenne et on lui affecte la valeur False
        if (Point.__calculerDistance__(self.premier, self.deuxième) == Point.__calculerDistance__(self.premier, self.troisième) + Point.__calculerDistance__(self.deuxième, self.troisième) or Point.__calculerDistance__(self.premier, self.troisième) == Point.__calculerDistance__(self.premier, self.deuxième) + Point.__calculerDistance__(self.deuxième, self.troisième)) or Point.__calculerDistance__(self.deuxième, self.troisième) == Point.__calculerDistance__(self.premier, self.troisième) + Point.__calculerDistance__(self.premier, self.deuxième) : #On applique le raisonnement nous permettant de déterminer si 3 points sont alignés ou non en calculant leur longueur à l'aide de la méthode __calculerDistance__
            alignés = True #Si les 3 points sont alignés notre variable booléenne prend la valeur True
        return alignés 
    
    def __estIsocèle__(self, premier, deuxième, troisième) :
        isocèle = False #On crée une variable booléenne et on lui affecte la valeur False
        if (Point.__calculerDistance__(self.premier, self.deuxième) == Point.__calculerDistance__(self.premier, self.troisième) or Point.__calculerDistance__(self.premier, self.deuxième) == Point.__calculerDistance__(self.deuxième, self.troisième)) or Point.__calculerDistance__(self.deuxième, self.troisième) == Point.__calculerDistance__(self.premier, self.troisième) : #On applique le raisonnement nous permettant de déterminer si un triangle est isocèle ou non en calculant la longueur de ses côtés à l'aide de la méthode __calculerDistance__
            isocèle = True #Si le triangle est isocèle notre variable booléenne prend la valeur True
        if self.__sontAlignes__(self.premier, self.deuxième, self.troisième) == True : #On fait en sorte que si les points sont alignés mais à equidistance le programme ne dise pas que le triangle est isocèle
            isocèle = False
        return isocèle

    def __str__(self) :
        return f"Les trois points sont alignés : {self.__sontAlignes__(self.premier, self.deuxième, self.troisième)} et le triangle est isocèle : {self.__estIsocèle__(self.premier, self.deuxième, self.troisième)}" #A l'aide de la méthode __str__ on renvois le résultat de nos deux précédentes méthodes


def main() :
    p1 = Point(float(input("Entrez l'abscisse du point 1 :  ")), float(input("Entrez les ordonnées du point 1 :  "))) #On demande à l'utilisateur de rentrer les coordonnées des trois points, qui seront des objets de la classe Point
    p2 = Point(float(input("Entrez l'abscisse du point 2 :  ")), float(input("Entrez les ordonnées du point 2 :  ")))
    p3 = Point(float(input("Entrez l'abscisse du point 3 :  ")), float(input("Entrez les ordonnées du point 3 :  ")))
    print(TroisPoints(p1, p2, p3)) #On affiche si les trois points sont alignés et si le triangle formé par ces derniers est isocèle ou non 

if __name__ == '__main__' :
    main()
