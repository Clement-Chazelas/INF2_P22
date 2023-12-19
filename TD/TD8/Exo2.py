from tkinter import *
class Fenetre(Tk) :
    def __init__(self) :
        Tk.__init__(self)
        self.prenom()
        self.prenom_etiquette()
        self.nom()
        self.nom_etiquette()
        self.domaine()
        self.domaine_etiquette()
        self.valider()
        self.affiche()

    def prenom(self) :
        self.entrée_prénom = Entry(self)
        self.entrée_prénom.grid(row = 0, column = 10, columnspan = 3, padx = 10, pady =15)

    def prenom_etiquette(self) :
        self.etiquette = Label(self, text="Prénom : ")
        self.etiquette.grid(row = 0, column = 1, columnspan = 3, padx = 10, pady =15)

    def nom(self) :
        self.entrée_nom = Entry(self)
        self.entrée_nom.grid(row = 1, column = 10, columnspan = 3, padx = 10, pady =15)

    def nom_etiquette(self) :
        self.etiquette = Label(self, text="Nom : ")
        self.etiquette.grid(row = 1, column = 1, columnspan = 3, padx = 10, pady =15)

    def domaine(self) :
        self.entrée_domaine = Entry(self)
        self.entrée_domaine.grid(row = 2, column = 10, columnspan = 3, padx = 10, pady =15)

    def domaine_etiquette(self) :
        self.etiquette = Label(self, text="Domaine : ")
        self.etiquette.grid(row = 2, column = 1, columnspan = 3, padx = 10, pady =15)

    def valider(self) :
        self.bouton = Button(self, text="Valider", command=self.lama)
        self.bouton.grid(row = 3, column = 1, columnspan = 3, padx = 10, pady =15)

    def affiche(self) :
        self.oui = Label(self, text="")
        self.oui.grid(row = 4, column = 1, columnspan = 3, padx = 10, pady =15)

    def lama(self) :
        self.oui.config(text = f"{self.entrée_prénom.get()}.{self.entrée_nom.get()}@{self.entrée_domaine.get()}")

fenetre = Fenetre()
fenetre.mainloop()
