# !/usr/bin/python
# -*- coding: utf-8 -*-

from Tkinter import*
root = Tk()

li = 'Diego Matias Martin Carla Lorena Roberto'.split()
listb=Listbox(root)
for item in li:
    listb.insert(0,item)
    
listb.pack()
root.mainloop()
    
    
