from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Телефонная книга Валерона")
root.geometry("250x200")

contacts = [
    ("Ирина", "555-555-555"),
    ("Мама", "456-777-888"),
     ("Бабушка", "999-777-888"),
    ]
var = Variable(value=contacts)

listbox = Listbox(root)
#for i in range(0, len(contacts)):
 #   listbox.insert(contacts[i][0], contacts[i][1])

listbox.column(0, width=15, anchor="w")
listbox.column(1, width=5, anchor="w")



listbox.pack(anchor=NW, fill=X, padx=5, pady=5)

root.mainloop()