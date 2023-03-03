from Calculators.stdDev import run_stdDEV
from Calculators.quadEq import run_quadEq
from Calculators.linEq import run_linEq
import tkinter as tk

GUI_Main = tk.Tk()
GUI_Main.title("Home")

but_StdDEV = tk.Button(GUI_Main, text="Standard Deviation", width=20, command=run_stdDEV)
but_StdDEV.grid(row=0, column=0)

but_quadEq = tk.Button(GUI_Main, text="Quadratic Equation", width=20, command=run_quadEq)
but_quadEq.grid(row=0, column=1)

but_linEq = tk.Button(GUI_Main, text="Linear Equation", width=20, command=run_linEq)
but_linEq.grid(row=0, column=2)

GUI_Main.mainloop()