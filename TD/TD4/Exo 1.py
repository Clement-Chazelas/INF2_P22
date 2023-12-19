class Sommet :
    __nb_sommet = 0
    def __init__(self, id) :
        self.id = id
        Sommet.__nb_sommet +=1
    
    @property
    def id(self) :
        return self.__id 
    
    def __str__(self) :
        return 
    
    def get_nb_sommet() :
        return Sommet.__nb_sommet
    
    def __del__(self) :
        Sommet.__nb_sommet -=1
        del(self)

    def __hash__(self) :
        return hash(self.id)

    def __eq__(self, other) :
        return self.id == other.id

    @id.setter
    def id(self, i) :
        if i.__hash__ == None :
            raise TypeError("Le sommet n'est pas hashable")
        self.__id = i