from math import sqrt
import tkinter as tk

insList_stillInp = str()
insList_x = 1
insList_tempAdd_raw = str()
insList_tempAdd_list = list()

getstdDev_list = list()
getstdDev_mean = int()
getstdDev_ToF = int()
getstdDev_stdDev = int()

listVal = list()

def insList(abc, inp):
    global insList_stillInp
    global insList_x
    global insList_tempAdd_raw
    global insList_tempAdd_list

    while insList_x == 1:
        insList_tempAdd_raw = (inp)
        insList_tempAdd_list = insList_tempAdd_raw.split()
        for val in insList_tempAdd_list:
            abc.append(int(val))

        else:
            break

def findstdDev(abc):
    global getstdDev_list
    global getstdDev_mean
    global getstdDev_ToF
    global getstdDev_stdDev

    print(abc)
    getstdDev_ToF = 0
    getstdDev_list = abc
    getstdDev_len = len(abc)
    getstdDev_mean = sum(abc)/getstdDev_len
    for num in abc:
        getstdDev_ToF += (num-getstdDev_mean)*(num-getstdDev_mean)
    getstdDev_stdDev = sqrt(getstdDev_ToF/getstdDev_len)
    print(getstdDev_stdDev)

def stdDev():
    global InpList
    global stdDEVLabel
    global GUI_stdDEV
    global getstdDev_stdDev
    global inpBox

    print(InpList)
    if inpBox.get() != "":
        InpList = []
        insList(InpList, inpBox.get())
        findstdDev(InpList)
        stdDEVLabel.config(text = getstdDev_stdDev)
        GUI_stdDEV.update

def clearList():
    global InpList 
    global inpBox
    inpBox.delete(0, (len(inpBox.get()))+1)
    InpList = list()

def run_stdDEV():
    global InpList
    global stdDEVLabel
    global GUI_stdDEV
    global inpBox

    InpList = list()

    GUI_stdDEV = tk.Tk()
    GUI_stdDEV.title("Standard Deviation")

    inpBox = tk.Entry(GUI_stdDEV,width=75)
    inpBox.grid(row=0, column=0)

    clearBut = tk.Button(GUI_stdDEV, text="Clear current list", command = clearList)
    clearBut.grid(row=3, column=0)

    enterBut = tk.Button(GUI_stdDEV, text="Calculate Standard Deviation", command=stdDev)
    enterBut.grid(row=4, column=0)

    stdDEVLabel = tk.Label(GUI_stdDEV, text="Click Above To Calculate")
    stdDEVLabel.grid(row=5, column=0)

    returnMain = tk.Button(GUI_stdDEV, text="Close", command=GUI_stdDEV.destroy)
    returnMain.grid(row=6, column=0)

    GUI_stdDEV.mainloop()
    #insList(listVal, InpList)

