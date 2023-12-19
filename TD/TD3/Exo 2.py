from distutils.log import error


class Horaire :
    def __init__(self, heure, minute) :
        self.heure = heure
        self.minute = minute
   
    @property
    def heure(self) :
        return self.__heure
   
    @heure.setter
    def heure(self, heure) :
        if type(heure) != int :
            raise TypeError("L'heure n'est pas donnée dans le bon format")
        elif heure < 0 or heure > 23 :
            raise ValueError("L'heure n'est pas comprise entre 0 et 24")
        self.__heure = heure
   
    @property
    def minute(self) :
        return self.__minute
   
    @minute.setter
    def minute(self, minute) :
        if type(minute) != int :
            raise TypeError("Les minutes ne sont pas données dans le bon format")
        elif minute < 0 or minute > 60 :
            raise ValueError("Les minutes ne sont pas comprise entre 0 et 24")
        self.__minute = minute

    def __str__(self) :
        if self.minute < 10 :
            return f"{self.heure}h0{self.minute}"
        else :
            return f"{self.heure}h{self.minute}"

    def __add__(self, durée) :
        heure_vol = (self.heure + durée.heure)
        minute_vol = (self.minute + durée.minute)
        if minute_vol >= 60 :
            minute_vol = minute_vol - 60
            heure_vol = heure_vol + 1
        if heure_vol >= 24 :
            heure_vol = heure_vol - 24
        return Horaire(heure_vol, minute_vol)



class Durée :
    def __init__(self, heure, minute) :
        self.heure = heure
        self.minute = minute

    @property
    def heure(self) :
        return self.__heure

    @heure.setter
    def heure(self, heure) :
        if type(heure) != int :
            raise TypeError("L'heure n'est pas donnée dans le bon format")
        elif heure < 0 or heure > 24 :
            raise ValueError("L'heure n'est pas comprise entre 0 et 24")
        self.__heure = heure

    @property
    def minute(self) :
        return self.__minute

    @minute.setter
    def minute(self, minute) :
        if type(minute) != int :
            raise TypeError("Les minutes ne sont pas données dans le bon format")
        elif minute < 0 or minute > 60 :
            raise ValueError("Les minutes ne sont pas comprise entre 0 et 24")
        self.__minute = minute

    def __str__(self) :
        if self.minute < 10 :
            return f"{self.heure}h0{self.minute}"
        else :
            return f"{self.heure}h{self.minute}"



class Vol :
    def __init__(self, nom, horaire_départ, durée) :
        self.nom = nom
        self.horaire_départ = horaire_départ
        self.durée = durée
        self.horaire_arrivée = self.horaire_départ + self.durée

    @property
    def nom(self) :
        return self.__nom

    @nom.setter
    def nom(self, nom) :
        if not isinstance(nom, str) :
            raise TypeError("Le nom du vol n'est pas dans le bon format")
        self.__nom = nom
    
    def __str__(self) :
        return f"Le vol {self.nom} partira à {self.horaire_départ} et arrivera à {self.horaire_arrivée}"

try :
    n = input("Entrez le nom du vol :  ")
    horaire_de_départ = Horaire(int(input("Entrez l'heure de départ :  ")), int(input("Entrez les minutes du départ :  ")))
    durée_vol = Durée(int(input("Entrez les heures de vol :  ")), int(input("Entrez les minutes de vol :  ")))
    print(Vol(n, horaire_de_départ, durée_vol))
except :
    TypeError


