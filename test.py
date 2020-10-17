from tkinter import *
from tkinter import ttk
import random
from BubleSort import bubble_sort

def drawData(data,colorArr):
    canvas.delete("all")
    c_height = 380
    c_width = 600
    x_width = c_width / (len(data) + 1)
    offset = 30
    spacing = 10
    normalizedData = [i / max(data) for i in data]
    for i, height in enumerate(normalizedData):
        # górny róg
        x0 = i * x_width + offset + spacing
        y0 = c_height - height * 340
        # dolny róg
        x1 = (i + 1) * x_width + offset
        y1 = c_height
        canvas.create_rectangle(x0, y0, x1, y1, fill=colorArr[i])
        canvas.create_text(x0 + 2, y0, anchor=SW, text=str(data[i]))
    root.update_idletasks()
def Generate():
    global data
    print("wybrano algorytm:" + selected_alg.get())
    minVal= int(minEntry.get())
    maxVal=int(maxEntry.get())
    size=int(sizeEntry.get())
    data = []
    for i in range(size):
        data.append(random.randint(minVal, maxVal))
    drawData(data,["red" for x in range(len(data))])

def StartAlgorithm():
    global data
    bubble_sort(data,drawData,(speedScale.get()))

root = Tk()
root.title('sorting')
root.maxsize(900, 600)
root.config(bg='black')
# zmienne
data=[]
selected_alg = StringVar()
# baza aplikacji
UI_frame = Frame(root, width=600, height=200, bg='grey')
UI_frame.grid(row=0, column=0, padx=10, pady=5)
canvas = Canvas(root, width=600, height=380, bg="white")
canvas.grid(row=1, column=0, padx=10, pady=5)
# interfejs urzytkownika
Label(UI_frame, text="algos: ", bg="grey").grid(row=0, column=0, padx=5, pady=5, sticky=W)
algMenu = ttk.Combobox(UI_frame, textvariable=selected_alg, values=["bubble sort", "Marge sort"])
algMenu.grid(row=0, column=1, padx=5, pady=5)
algMenu.current(0)
speedScale = Scale(UI_frame, from_=0.1, to=2.0, length=200, digits=2,resolution=0.2, orient=HORIZONTAL, label="Selected Speed [s]")
speedScale.grid(row=0,column=2,padx=5,pady=5)

Button(UI_frame, text="Generate", command=Generate, bg="red").grid(row=1, column=4, padx=5, pady=5)
Button(UI_frame,text="start",command=StartAlgorithm,bg="red").grid(row=0,column=3,padx=5,pady=6)

sizeEntry = Scale(UI_frame, from_=3, to=30, length=200, digits=2,resolution=1, orient=HORIZONTAL, label="Rozmiar")
sizeEntry.grid(row=1, column=1, padx=5, pady=5)

minEntry = Scale(UI_frame, from_=0, to=10, length=200, digits=2,resolution=1, orient=HORIZONTAL, label="minimalna wartość")
minEntry.grid(row=1, column=2, padx=5, pady=5)

maxEntry = Scale(UI_frame, from_=10, to=100, length=200, digits=2,resolution=1, orient=HORIZONTAL, label="maksymalna wartość")
maxEntry.grid(row=1, column=3, padx=5, pady=5)
root.mainloop()
