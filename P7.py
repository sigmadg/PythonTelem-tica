# !/usr/bin/python
# -*- coding: utf-8 -*-

from Tkinter import*

def DrawList():
    plist=['Diego', 'Matilde', 'Ramon']
    for item in plist:
        listbox.insert(END, item);

root = Tk()

listbox = Listbox(root)
boton = Button(root, text = "Presionar",  command = DrawList)

boton.pack()
listbox.pack()
root.mainloop()
