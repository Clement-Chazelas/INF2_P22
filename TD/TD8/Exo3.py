from random import randint
from tkinter import *


class Fenetre(Tk) :
    def __init__(self) :
        Tk.__init__(self)
        self.lancer1()
        self.lancer2()
        self.lancer3()
        self.affiche1()
        self.affiche2()
        self.affiche3()
        self.count = IntVar()
        self.affichecount()

        
    def lancer1(self):
        self.l = Button(self, text='Lancer 1', command=self.lama)
        self.l.grid(row=1, column=1)
    
    def lancer2(self):
        self.la = Button(self, text='Lancer 2', command=self.lamasticot)
        self.la.grid(row=2, column=1)

    def lancer3(self):
        self.lan = Button(self, text='Lancer 3', command=self.oui)
        self.lan.grid(row=3, column=1)

    def affiche1(self) :
        self.a = Label(self, text="", relief="sunken", bg="white", width=7)
        self.a.grid(row = 1, column = 2)

    def affiche2(self) :
        self.af = Label(self, text="", relief="sunken", bg="white", width=7)
        self.af.grid(row = 2, column = 2)

    def affiche3(self) :
        self.aff = Label(self, text="", relief="sunken", bg="white", width=7)
        self.aff.grid(row = 3, column = 2)

    def lama(self) :
        x = randint(1,6)
        self.a.config(text = f"{x}")
        self.count.set(self.count.get() + 1)

    def lamasticot(self) :
        x = randint(1,6)
        self.af.config(text = f"{x}")
        self.count.set(self.count.get() + 1)

    def oui(self) :
        x = randint(1,6)
        self.aff.config(text = f"{x}")
        self.count.set(self.count.get() + 1)

    def affichecount(self) :
        self.c = Label(self, textvariable=self.count, relief="sunken", bg="white", width=7)
        self.c.grid(row=4, column=1)




fenetre = Fenetre()
fenetre.mainloop()
