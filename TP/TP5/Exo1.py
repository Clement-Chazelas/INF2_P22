from tkinter import *
from math import *
from matplotlib.pyplot import text

class Fenetre(Tk) :
    def __init__(self) :
        Tk.__init__(self)
        self.calcul = StringVar()
        self.title('TP calculatrice')
        self.chiffres()
        self.titre()
        self.plus()
        self.moins()
        self.diviser()
        self.fois()
        self.zero()
        self.valider()
        self.virgule()
        self.pi()
        self.tangente()
        self.cos()
        self.sin()
        self.racine()
        self.carré()
        self.champ()
        self.clear()
        self.parenthèses()
        self.histo = []
        self.bhistorique()
        self.compteur = IntVar()

    
    def champ(self) :
        self.ch = Entry(self, width=50,justify='center', relief='sunken', borderwidth=15, textvariable=self.calcul)
        self.ch.grid(row= 2, column=1, columnspan=6)

    def titre(self) :
        self.titr = Label(self , text='Calculatrice', justify='center')
        self.titr.grid(row=1, column=2, columnspan=4, sticky='ew')
    
    def plus(self) :
        self.p = Button(self, text='+', justify='center', bg='lightblue', activebackground='lightblue', borderwidth=10, command=lambda: self.addcalc('+'))
        self.p.grid(row=3, column=4, ipady=5, ipadx=7.5, padx=10, pady=10)

    def moins(self) :
        self.m = Button(self, text='-', justify='center', bg='lightblue', activebackground='lightblue', borderwidth=10, command=lambda: self.addcalc('-'))
        self.m.grid(row=4, column=4, ipady=5, ipadx=7.5, padx=10, pady=10)

    def fois(self) :
        self.f = Button(self, text='*', justify='center', bg='lightblue', activebackground='lightblue', borderwidth=10, command=lambda: self.addcalc('*'))
        self.f.grid(row=5, column=4, ipady=5, ipadx=7.5, padx=10, pady=10)

    def diviser(self) :
        self.d = Button(self, text='/', justify='center', bg='lightblue', activebackground='lightblue', borderwidth=10, command=lambda: self.addcalc('/'))
        self.d.grid(row=6, column=4, ipady=5, ipadx=7.5, padx=10, pady=10)

    def zero(self) :
        self.z = Button(self, text='0', justify='center', bg='yellow', activebackground='yellow', borderwidth=10, command=lambda: self.addcalc(0))
        self.z.grid(row=6, column=1, ipady=5, ipadx=7.5, padx=10, pady=10)

    def valider(self) :
        self.v = Button(self, text='=', justify='center', bg='red', activebackground='red', borderwidth=10, command= self.triggeregal)
        self.v.grid(row=6, column=2, ipady=5, ipadx=7.5, padx=10, pady=10)

    def virgule(self) :
        self.vi = Button(self, text='.', justify='center', bg='yellow', activebackground='yellow', borderwidth=10)
        self.vi.grid(row=6, column=3, ipady=5, ipadx=7.5, padx=10, pady=10)

    def cos(self) :
        self.c = Button(self, text='cos(x)', justify='center', bg='#87C7A5', activebackground='#87C7A5', borderwidth=10, command=lambda: self.addcalc('cos('))
        self.c.grid(row=3, column=5, ipady=5, ipadx=7.5, padx=10, pady=10)

    def sin(self) :
        self.s = Button(self, text='sin(x)', justify='center', bg='#87C7A5', activebackground='#87C7A5', borderwidth=10, command=lambda: self.addcalc('sin('))
        self.s.grid(row=4, column=5, ipady=5, ipadx=7.5, padx=10, pady=10)

    def tangente(self) :
        self.t = Button(self, text='tan(x)', justify='center', bg='#87C7A5', activebackground='#87C7A5', borderwidth=10, command=lambda: self.addcalc('tan('))
        self.t.grid(row=5, column=5, ipady=5, ipadx=7.5, padx=10, pady=10)

    def pi(self) :
        self.pii = Button(self, text='π', justify='center', bg='#87C7A5', activebackground='#87C7A5', borderwidth=10, command=lambda: self.addcalc('pi'))
        self.pii.grid(row=5, column=6, ipady=5, ipadx=7.5, padx=10, pady=10)

    def racine(self) :
        self.r = Button(self, text='√x', justify='center', bg='#87C7A5', activebackground='#87C7A5', borderwidth=10, command=lambda: self.addcalc('sqrt('))
        self.r.grid(row=4, column=6, ipady=5, ipadx=7.5, padx=10, pady=10)

    def carré(self) :
        self.car = Button(self, text='x²', justify='center', bg='#87C7A5', activebackground='#87C7A5', borderwidth=10, command=lambda: self.addcalc('**2'))
        self.car.grid(row=3, column=6, ipady=5, ipadx=7.5, padx=10, pady=10)

    def chiffres(self) :
        self.chiffre1 = Button(self, text="1", justify="center", relief='raised', bg='yellow', activebackground='yellow', borderwidth=10, command=lambda: self.addcalc(1))
        self.chiffre1.grid(row=3 , column= 1, ipady=5, ipadx=7.5, padx=10, pady=10)

        self.chiffre2 = Button(self, text="2", justify="center", relief='raised', bg='yellow', activebackground='yellow', borderwidth=10, command=lambda: self.addcalc(2))
        self.chiffre2.grid(row=3 , column= 2, ipady=5, ipadx=7.5, padx=10, pady=10)

        self.chiffre3 = Button(self, text="3", justify="center", relief='raised', bg='yellow', activebackground='yellow', borderwidth=10, command=lambda: self.addcalc(3))
        self.chiffre3.grid(row=3 , column= 3, ipady=5, ipadx=7.5, padx=10, pady=10)

        self.chiffre4 = Button(self, text="4", justify="center", relief='raised', bg='yellow', activebackground='yellow', borderwidth=10, command=lambda: self.addcalc(4))
        self.chiffre4.grid(row=4 , column= 1, ipady=5, ipadx=7.5, padx=10, pady=10)

        self.chiffre5 = Button(self, text="5", justify="center", relief='raised', bg='yellow', activebackground='yellow', borderwidth=10, command=lambda: self.addcalc(5))
        self.chiffre5.grid(row=4 , column= 2, ipady=5, ipadx=7.5, padx=10, pady=10)

        self.chiffre6 = Button(self, text="6", justify="center", relief='raised', bg='yellow', activebackground='yellow', borderwidth=10, command=lambda: self.addcalc(6))
        self.chiffre6.grid(row=4 , column= 3, ipady=5, ipadx=7.5, padx=10, pady=10)

        self.chiffre7 = Button(self, text="7", justify="center", relief='raised', bg='yellow', activebackground='yellow', borderwidth=10, command=lambda: self.addcalc(7))
        self.chiffre7.grid(row=5 , column= 1, ipady=5, ipadx=7.5, padx=10, pady=10)

        self.chiffre8 = Button(self, text="8", justify="center", relief='raised', bg='yellow', activebackground='yellow', borderwidth=10, command=lambda: self.addcalc(8))
        self.chiffre8.grid(row=5 , column= 2, ipady=5, ipadx=7.5, padx=10, pady=10)

        self.chiffre9 = Button(self, text="9", justify="center", relief='raised', bg='yellow', activebackground='yellow', borderwidth=10, command=lambda: self.addcalc(9))
        self.chiffre9.grid(row=5 , column= 3, ipady=5, ipadx=7.5, padx=10, pady=10)

    def parenthèses(self) :
        self.parenth = Button(self, text='(', justify="center", relief='raised', bg='#0acfaa', activebackground='#0acfaa', borderwidth=10, command=lambda: self.addcalc('('))
        self.parenth.grid(row=3, column= 7, ipady=5, ipadx=7.5, padx=10, pady=10)

        self.parenth = Button(self, text=')', justify="center", relief='raised', bg='#0acfaa', activebackground='#0acfaa', borderwidth=10, command=lambda: self.addcalc(')'))
        self.parenth.grid(row=4, column= 7, ipady=5, ipadx=7.5, padx=10, pady=10)


    def clear(self):
        self.clea = Button(self, text='Clear all', justify='center', borderwidth=10, bg='lightgreen', activebackground='lightgreen', command=self.effacer)
        self.clea.grid(row= 6, column=5, ipady=5, ipadx=7.5, padx=10, pady=10)

    def effacer(self) :
        self.calcul.set('')

    def addcalc(self, num) :
        self.calcul.set(self.calcul.get() + str(num))

    def bhistorique(self) :
        self.bhisto = Button(self, text='<', justify='center', borderwidth=10, bg='lightgreen', activebackground='lightgreen', command=self.retourhistorique)
        self.bhisto.grid(row=6, column= 6, ipady=5, ipadx=7.5, padx=10, pady=10)
        
        self.bhisto = Button(self, text='>', justify='center', borderwidth=10, bg='lightgreen', activebackground='lightgreen', command=self.avanthistorique)
        self.bhisto.grid(row=6, column= 7, ipady=5, ipadx=7.5, padx=10, pady=10)

    def retourhistorique(self) :
        self.compteur.set(self.compteur.get() + 1)
        self.calcul.set(self.histo[len(self.histo)-self.compteur.get()])
        


    def avanthistorique(self) :
        if self.compteur.get() == 0 :
            self.effacer()
        else :
            self.compteur.set(self.compteur.get() - 1)
            self.calcul.set(self.histo[len(self.histo)-self.compteur.get()])
            



    def triggeregal(self): #Définition de la fonction
        try: #Puisque nous exécutons le code entré, plusieurs erreurs peuvent arriver, nous utilisons un try
            self.compteur.set(0)
            result = eval(self.calcul.get()) #On exécute le code
            float(result) #L'instruction exécutée par le eval peut ne pas être un calcul, on vérifie donc si l'entrée est un nombre, sinon, on traite l'erreur de conversion plus tard dans le code du except
            result = round(result,10) #On arrondit le résultat
            self.histo.append(f"{self.calcul.get()} = {result}")
            self.calcul.set(result) #on arrondit le calcul tout en donnant le plus de précision possible
 
 
        except ZeroDivisionError: #Si il y a une division par 0, on retourne l'erreur à l'utilisateur via la barre d'entrée
            self.calcul.set("Division par 0 impossible !")
 
        except OverflowError: #Si l'ordinateur n'est pas capable d'effectuer le calcul, on retourne l'erreur à l'utilisateur via la barre d'entrée
            self.calcul.set("Nombre trop gros !")
  
        except  ValueError as e: #On vérifie chaque erreur de valeur possibles
            if e == "math domain error": #Si on a un calcul hors du domaine de définition des fonction (ex: racine d'un nombre négatif), on retourne l'erreur à l'utilisateur via la barre d'entrée
                self.calcul.set("Calcul hors du domaine de définition de la fonction")
            elif e.startswith("could not convert string to float"): #Si le résultat retourné n'est pas un nombre, alors le calcul entré n'était pas un calcul, on retourne l'erreur à l'utilisateur via la barre d'entrée
                self.calcul.set("Calcul invalide !")



fenetre = Fenetre()
fenetre.mainloop()