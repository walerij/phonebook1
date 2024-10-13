from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Телефонная книга Валерона")
root.geometry("250x200")

contacts = ["Иван", "Ирина", "Мама", "Бабушка"]
languages_var = Variable(value=contacts)

languages_listbox = Listbox(listvariable=languages_var)

languages_listbox.pack(anchor=NW, fill=X, padx=5, pady=5)

root.mainloop()