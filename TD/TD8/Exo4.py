from cProfile import label
from tkinter import *


class Fenetre(Tk) :
    def __init__(self) :
        Tk.__init__(self)
        self.echequier()
        self.title("Echequier")

    def echequier(self) :
        bg = True
        for i in range(1,9) :
            for j in range(1,9) : 
                if bg == True :    
                    self.chiffre = Label(self, text="", justify="center", bg='black')
                    self.chiffre.grid(row=i, column=j, ipady=5, ipadx=12)
                    bg = False
                else :
                    self.chiffre = Label(self, text="", justify="center", bg='white')
                    self.chiffre.grid(row=i , column=j , ipady=5, ipadx=12)
                    bg = True
            if bg == False :
                bg = True
            else :
                bg = False

fenetre = Fenetre()
fenetre.mainloop()
