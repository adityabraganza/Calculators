import tkinter as tk
from importsCom import isfloat

def findy():
    global mBox
    global xBox
    global cBox
    global y
    global yLabel

    if isfloat(mBox.get()) and isfloat(xBox.get()) and isfloat(cBox.get()):
        m = float(mBox.get())
        x = float(xBox.get())
        c = float(cBox.get())
        if m != 0:
            y = (m*x)+c
            yLabel.config(text="y = " + str(y))
        else:
            yLabel.config(text="m can't be 0")
    else:
        yLabel.config(text="Given values are invalid")

    y = (m*x) + c
    print(y)

def run_linEq():
    global mBox
    global xBox
    global cBox
    global y
    global yLabel

    GUI_linEq = tk.Tk()

    totalcolumns = 2

    infoLabel = tk.Label(GUI_linEq, text="Format(give m, x, and c): y = mx + c")
    infoLabel.grid(row="0", column="0", columnspan=totalcolumns, sticky= tk.W + tk.E)

    mLabel = tk.Label(GUI_linEq, text="m: ")
    mLabel.grid(row=1, column=0, sticky= tk.E)

    mBox = tk.Entry(GUI_linEq, width=10)
    mBox.grid(row=1, column=1, sticky= tk.W)

    xLabel = tk.Label(GUI_linEq, text="x: ")
    xLabel.grid(row=2, column=0, sticky= tk.E)

    xBox = tk.Entry(GUI_linEq, width=10)
    xBox.grid(row=2, column=1, sticky= tk.W)

    cLabel = tk.Label(GUI_linEq, text="c: ")
    cLabel.grid(row=3, column=0, sticky= tk.E)

    cBox = tk.Entry(GUI_linEq, width=10)
    cBox.grid(row=3, column=1, sticky= tk.W)

    enterBut = tk.Button(GUI_linEq, text = "Calculate", width = 25, command=findy)
    enterBut.grid(row=4, column=0, columnspan=totalcolumns, stick= tk.W + tk.E)

    yLabel = tk.Label(GUI_linEq, text="Press button above to calculate")
    yLabel.grid(row=5, column=0, columnspan=totalcolumns, stick= tk.W + tk.E)

    returnMain = tk.Button(GUI_linEq, text="Close", command=GUI_linEq.destroy)
    returnMain.grid(row=6, column=0, columnspan=totalcolumns, stick= tk.W + tk.E)

    GUI_linEq.mainloop()