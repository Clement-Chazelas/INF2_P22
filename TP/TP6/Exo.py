from tkinter import *
from sqlite3 import *


class Fenetre(Tk) :
    def __init__(self) :
        Tk.__init__(self)
        self.title('TP6')
        self.prenom()
        self.prenom_etiquette()
        self.nom()
        self.nom_etiquette()
        self.valider()
        self.reinitialiser()
        self.affiche()
        self.Quitter()


    def prenom(self) :
        self.entrée_prénom = Entry(self)
        self.entrée_prénom.grid(row = 1, column = 10, columnspan = 3, padx = 10, pady =15)

    def prenom_etiquette(self) :
        self.etiquette = Label(self, text="Prénom du logeur : ")
        self.etiquette.grid(row = 1, column = 1, columnspan = 3, padx = 10, pady =15)

    def nom(self) :
        self.entrée_nom = Entry(self)
        self.entrée_nom.grid(row = 0, column = 10, columnspan = 3, padx = 10, pady =15)

    def nom_etiquette(self) :
        self.etiquette = Label(self, text="Nom du logeur : ")
        self.etiquette.grid(row = 0, column = 1, columnspan = 3, padx = 10, pady =15)

    def valider(self) :
        self.bouton = Button(self, text="Valider", command=self.affiche)
        self.bouton.grid(row = 3, column = 1, padx = 10, pady =15)

    def reinitialiser(self) :
        self.rei = Button(self, text="Reinitaliser", command=self.effacer)
        self.rei.grid(row = 3, column = 3, padx = 10, pady =15)

    def Quitter(self) :
        self.rei = Button(self, text="Quitter", command=self.quitter)
        self.rei.grid(row = 3, column = 4, padx = 10, pady =15)

    def quitter(self) :
        e

    def effacer(self) :
        e

    def données(self, nom, prenom) :
         fichier_bdd= "C:/Users/clemc/Desktop/UTC/TC02/INF2/TP/TP6/BDD.sqlite"
         connexion = connect(fichier_bdd)
         curseur = connexion.cursor()

         curseur.execute(f'''Select id_logeur FROM logeur WHERE nom = '{nom}' AND prenom = '{prenom}' ''')
         for i in curseur :
             global idlogeur
             idlogeur = i

         curseur.execute(f'''Select id_logement FROM logement WHERE id_logeur = '{idlogeur}' ''')
         for i in curseur :
             global idlogement
             idlogement.append(i)
        
         for j in idlogement :
            curseur.execute(f'''Select num_rue FROM logement WHERE id_logement = {j}''')
            for i in curseur :
                global numero_rue
                numero_rue = i
        
         for j in idlogement :
            curseur.execute(f'''Select nom_rue FROM logement WHERE id_logement = {j}''')
            for i in curseur :
                global nom_rue
                nom_rue.append(i)

         for j in idlogement :
            curseur.execute(f'''Select code_postal FROM logement WHERE id_logement = {j}''')
            for i in curseur :
                global code_postal
                code_postal.append(i)

         for j in idlogement :
            curseur.execute(f'''Select ville FROM logement WHERE id_logement = {j}''')
            for i in curseur :
                global ville
                ville.append(i)

         for j in idlogement :
            curseur.execute(f'''Select type FROM logement WHERE id_logement = {j}''')
            for i in curseur :
                global type
                type.append(i)


         connexion.commit()
         curseur.close()
         connexion.close()   



    def affiche(self) :
        nom = self.entrée_nom.get()
        prenom = self.entrée_prénom.get()
        self.données(nom, prenom)
        
        
        fichier_bdd= "C:/Users/clemc/Desktop/UTC/TC02/INF2/TP/TP6/BDD.sqlite"
        connexion = connect(fichier_bdd)
        curseur = connexion.cursor()

        x = 1
        y = 0
        
        
        for j in idlogement :
            curseur.execute(f'''Select nom, prenom FROM etudiant WHERE id_logement = '{j}' ''')
            
            numero = numero_rue[y]
            nom = nom_rue[y]
            post = code_postal[y]
            typ = type[y]

            self.y = Label(self, text = f'logement {y+1}')
            self.y.grid(row = 3 + x, column = 1)
            
            self.w = Label(self, text = f'{numero} {nom} {post} {typ}')
            self.w.grid(row = 4 + x, column = 1)   
         
            for i in curseur :
                self.a = Label(self, text="Nom de l'étudiant")
                self.a.grid(row = 5 + x, column = 1, padx = 5, pady =7)
                self.b = Label(self, text=i)
                self.b.grid(row = 5 + x, column = 2, columnspan = 3, padx = 10, pady =15)
                x = x + 2
            x = x + 2
            y = y + 1
       
        connexion.commit()
        curseur.close()
        connexion.close()






idlogement = []
idlogeur = ''
type = []
ville = []
code_postal = []
numero_rue = []
nom_rue = []

fenetre = Fenetre()
fenetre.mainloop()
