from cgitb import text
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

rep = "oui"

with open("texte.txt", "w") as fichier :
    while rep != "" :
        x = input("Entrez une chaîne de caractère")
        fichier.write(f"{x}\n")
        rep = input("Voulez-vous continuer à écrire ? (retour à la ligne pour arreter)")

liste_note = []
with open("texte.txt", "r") as fichier :
        texte = fichier.readlines()
        for ligne in texte :
            mots = ligne.split(";")
            if mots[0] == "Note" :
                note = Note(mots[1])
                liste_note.append(note)
            elif mots[0] == "Article" :
                article = Article(mots[1], mots[2])
                liste_note.append(article)
            elif mots[0] == "Image" :
                image = Image(mots[1], mots[2], mots[3])
                liste_note.append(image)
            elif mots[0] == "Document" :
                note = Document(mots[1])
                for i in range(2, len(mots - 1)) :
                    note.ajoutenote(liste_note[int(mots[1]-1)])
                liste_note.append(note)

for n in liste_note :
    n.print()
