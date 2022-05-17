# !/usr/bin/python
# -*- coding: utf-8 -*-

from Tkinter import*
root = Tk()

li = ["Diego", "Matias", "Lorena", "Roberto", "Rosario"]
movie = ["El padrino", "Naruto", " La gran estafa", "Los juegos del hambre"]
listb = Listbox(root)
listb2 = Listbox(root)
for item in li:
    listb.insert(0, item)
    
for item in movie:
    listb2.insert(0, item)
    
listb.pack()
listb2.pack()
root.mainloop()
