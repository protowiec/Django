from tkinter import *

root = Tk()
root.mainloop()

root.title("Prosty interfejs GUI")
root.geometry("400x150")
app = Frame(root)

lbl = Label(app, text = "Jestem etykieta !")
lbl.grid()
bttn1 = Button(app, text = "Przycisk pierwszy")
bttn1.grid()

root.mainloop()
