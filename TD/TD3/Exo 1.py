class Date() :
    def __init__(self, jour, mois, année) :
        self.__jour = jour
        self.__mois = mois
        self.__année = année
   
    def __str__(self) :
        return f"{self.__jour}/{self.__mois}/{self.__année}"
   
    def __jourDuLendemain__() :
        jour31 = [1,3,5,7,8,10,12]
        jour30 = [4,6,9,11]
        demain = Date(self.__jour, self.__mois, self.__année)
        if self.__mois == 2 :
            if self.__jour == 28 :
                self.__mois == self.__mois + 1
                self.__jour == 1
            else :
                self.__jour == self.__jour + 1
    
    def get_jour(self) :
        return self.__jour
   
    def get_mois(self) :
        return self.__mois
   
    def get_année(self) :
        return self.__année
   
    def set_jour(self, j) :
        self.__jour = j
   
    def set_mois(self, m) :
        self.__mois = m
   
    def set_année(self, a) :
        self.__année = a
    