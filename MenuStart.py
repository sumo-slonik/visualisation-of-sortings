from tkinter import *

root = Tk()  # Creating instance of Tk class
root.title("Centering windows")
root.resizable(False, False)  # This code helps to disable windows from resizing
window_height = 500
window_width = 450
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2))
root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
one = Button(text="pojedyńcze")
one.grid(row=0,column=1,padx=20)
root.mainloop()