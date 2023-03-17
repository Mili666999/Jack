pet = []
dva = []

from tkinter import *
from random import randint

window = Tk()
window.title("JACKPOT")

def prvih_pet():
    i = 1
    while i < 6:
        i += 1
        x = randint(1,50)
        if x in pet:
            i -= 1
            continue
        pet.append(x)
        pet.sort()
        Label (window, text = (pet), bg = "white", fg = "black", font = "none 25 bold", width = 15) .grid(row = 1, column = 0)

def druga_dva():
    i = 1
    while i < 3:
        i += 1
        x = randint(1,10)
        if x in dva:
            i -= 1
            continue
        dva.append(x)
        dva.sort()
        Label (window, text = (dva), bg = "white", fg = "black", font = "none 25 bold", width = 15) .grid(row = 2, column = 0)

prvih_pet()
druga_dva()

def dugme():
    pet.clear()
    prvih_pet()
    dva.clear()
    druga_dva()
    
Label (window, text = "Vaši sretni brojevi su:", fg = "black", font = "none 20 bold") .grid(row = 0, column = 0)
Button (window, text = "Nova kombinacija", bg = "light grey", fg = "black", font = "none 15", command = dugme) .grid(row = 4, column = 0)

window.mainloop()                                                                            
