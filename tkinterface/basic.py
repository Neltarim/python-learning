#encoding: utf-8

from tkinter import *

win = Tk() #init la fenetre

field_label = Label(win, text="bujur") #ajoute un label simple
field_label.pack() #ajouute l'objet a la fenetre


var_entry = StringVar() #champ de saisie
field_entry = Entry(win, textvariable=var_entry, width=30)
field_entry.pack()


var_check = IntVar()
checkButton = Checkbutton(win, text="Ne plus poser cette question", variable=var_check)
checkButton.pack()
#controle de la variable via "var_check.get()"

entry_for_button = StringVar()
choice_red = Radiobutton(win, text="red", variable=entry_for_button, value="red")
choice_blue = Radiobutton(win, text="red", variable=entry_for_button, value="blue")
choice_green = Radiobutton(win, text="green", variable=entry_for_button, value="green")

choice_blue.pack()
choice_green.pack()
choice_red.pack()



listBox = Listbox(win)
listBox.pack()
listBox.insert(END, "pierre")
listBox.insert(END, "feuille")
listBox.insert(END, "ciseau")

button = Button(win, text="leave", command=win.quit)
button.pack()

win.mainloop() #definit comme fenetre principale