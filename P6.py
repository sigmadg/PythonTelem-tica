# !/usr/bin/python
# -*- coding: utf-8 -*-

from Tkinter import*
root = Tk()

def Call (): 
    lab=Label(root, text='Usted presiono el boton') 
    lab.pack()
    boton['bg']='blue' 
    boton['fg']='white'
   
root = Tk()
root.geometry('100x110+335+70')
boton= Button(root, text = 'Presionar',  command = Call)
boton.pack()

root.mainloop()
