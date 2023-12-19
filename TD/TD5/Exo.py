import os
import PIL.Image


class Note :
    def __init__(self, titre) :
        self.titre = titre
    
    @property
    def titre(self) :
        return self.__titre

    @titre.setter 
    def titre(self, titre) :
        if not isinstance(titre, str) :
            raise TypeError("Le titre doit être une chaîne de caractère")
        self.__titre = titre
    
    def print(self):
        print(f"Titre de la note : {self.titre}")



class Article(Note) :
    def __init__(self, titre, texte) :
        super().__init__(titre)
        self.texte = texte

    @property
    def texte(self) :
        return self.__texte

    @texte.setter 
    def texte(self, texte) :
        if type(texte) != str :
            raise TypeError("Le texte doit être une chaîne de caractère")
        self.__texte = texte


    def print(self) :
        print(f"{self.titre} \n{self.texte}")



class Image(Note) :
    def __init__(self, titre, description, chemin) :
        super().__init__(titre)
        self.description = description
        self.chemin = chemin

    @property
    def description(self) :
        return self.__description

    @description.setter 
    def description(self, description) :
        self.__description = description

    @property
    def chemin(self) :
        return self.__chemin

    @chemin.setter 
    def chemin(self, chemin) :
        if os.path.isfile(chemin) == False :
            raise TypeError("Ce fichier n'existe pas")
        self.__chemin = chemin

    def print(self) :
        img = PIL.Image.open(self.chemin)
        print(f"{self.titre} \n{self.description} \n{img.show()}")



class Document(Note) :
    def __init__(self, titre) :
        super().__init__(titre)
        self.__list = []

    def ajoutenote(self, note) :
        if note == self :
            raise ValueError("Attention à la récursion")
        if not isinstance(note, Note) :
            raise TypeError("La note doit être une Note ou en hériter")
        self.__list.append(note)
    
    def supprimernote(self, note) :
        self.__list.remove(note)

    def print(self) :
        super().print()
        for note in self.__list :
            note.print()



image = Image("Oui", "LAMAAAAAAAAAAAAAAAAAAA", "Canard dessiné sur paint.png")
image.print()