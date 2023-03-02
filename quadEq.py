from math import sqrt
import tkinter as tk

def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

def discr(a, b, c):
    global discriminant
    global numberSol
    global discLabel
    global possibLabel

    discriminant = (b*b)-(4*a*c)
    if discriminant > 0:
        numberSol = 2
    if discriminant == 0:
        numberSol = 1
    if discriminant < 0:
        numberSol = 0
    if a != 0:
        discLabel.config(text="Discriminant: " + str(discriminant))
        possibLabel.config(text="Number of roots: " + str(numberSol))

def findx():
    global discriminant
    global numberSol
    global valueLabel
    global aBox
    global bBox
    global cBox

    x1 = 0
    x2 = 0

    a = 0
    b = 0
    c = 0

    try: 
        a = float(aBox.get())
    except ValueError: 
        valueLabel.config(text="Value of x: Input not a number")
    try: 
        b = float(bBox.get())
    except ValueError: 
        valueLabel.config(text="Value of x: Input not a number")

    try: 
        c = float(cBox.get())
    except ValueError: 
        valueLabel.config(text="Value of x: Input not a number")

    discr(a, b, c)

    if isfloat(a):
        if isfloat(a) and isfloat(b) and isfloat(c):


            if numberSol == 0 or a == 0:
                valueLabel.config(text="Value of x: Imaginary/None/Error")

            elif numberSol == 1:
                x1 = (
                    (-b)/(2*a)
                )
                valueLabel.config(text="Value of x: " + str(x1))

            elif numberSol == 2:
                x1 = (
                    (-b+(sqrt(b*b-(4*a*c))))/2*a
                )
                x2 = (
                    (-b-(sqrt(b*b-(4*a*c))))/2*a
                )
                valueLabel.config(text="Value of x: " + str(x1) + " or " + str(x2))

        else:
            return

def run_quadEq():
    global discLabel
    global possibLabel
    global valueLabel
    global aBox
    global bBox
    global cBox

    totalcolumns = 2
    sqrSymb = "\u00b2"

    GUI_quadEq = tk.Tk()

    quadLabel = tk.Label(GUI_quadEq, text="Format: ax" + sqrSymb + " + bx + c = 0")
    quadLabel.grid(row=0, column=0, columnspan=totalcolumns, sticky= tk.W + tk.E)

    aLabel = tk.Label(GUI_quadEq, text="Value of a:")
    aLabel.grid(row=1, column=0)

    aBox = tk.Entry(GUI_quadEq, width=10)
    aBox.grid(row=1, column=1)

    bLabel = tk.Label(GUI_quadEq, text="Value of b:")
    bLabel.grid(row=2, column=0)

    bBox = tk.Entry(GUI_quadEq, width=10)
    bBox.grid(row=2, column=1)

    cLabel = tk.Label(GUI_quadEq, text="Value of c:")
    cLabel.grid(row=3, column=0)
    
    cBox = tk.Entry(GUI_quadEq, width=10)
    cBox.grid(row=3, column=1)

    enterBut = tk.Button(GUI_quadEq, text="Find the Value of X", command=findx)
    enterBut.grid(row=4, column=0, columnspan=totalcolumns, stick= tk.W + tk.E)

    discLabel = tk.Label(GUI_quadEq, text="Discriminant: NA")
    discLabel.grid(row=5, column=0, columnspan=totalcolumns, stick= tk.W + tk.E)

    possibLabel = tk.Label(GUI_quadEq, text="Number of roots: NA")
    possibLabel.grid(row=6, column=0, columnspan=totalcolumns, stick= tk.W + tk.E)

    valueLabel = tk.Label(GUI_quadEq, text="Value of x: NA")
    valueLabel.grid(row=7, column=0, columnspan=totalcolumns, stick= tk.W + tk.E)

    returnMain = tk.Button(GUI_quadEq, text="Close", command=GUI_quadEq.destroy)
    returnMain.grid(row=8, column=0, columnspan=totalcolumns, stick= tk.W + tk.E)

    GUI_quadEq.mainloop()