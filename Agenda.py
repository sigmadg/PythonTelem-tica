#! usr/bin/python
# -*- coding: utf-8 -*-
import sqlite3
import time
import os

con = sqlite3.connect("agenda.db")
cursor = con.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS datos (nombre TEXT, apellido TEXT, telefono TEXT, correo TEXT)""")
cursor.close()

def limpiar():

    if os.name == "posix":
        os.system("clear")
    elif os.name == ("ce", "nt", "dos"):
        os.system("cls")

def agregar():

    print "Agregar contacto"
    print "----------------"
    print ""

    con = sqlite3.connect("agenda.db")
    cursor = con.cursor()
    nombre = raw_input("Nombre: ")
    apellido = raw_input("Apellido: ")
    telefono = raw_input("Telefono: ")
    correo = raw_input("Correo: ")

    cursor.execute("insert into datos (nombre, apellido, telefono, correo) values ('%s','%s','%s','%s')" % (nombre, apellido, telefono, correo))

    con.commit()

    print "Los datos fueron agregados correctamente"

    cursor.close()
    time.sleep(2)
    main()

def ver():

    print "Lista de contactos"
    print "------------------"
    print ""

    con = sqlite3.connect("agenda.db")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM datos")
    resultado = cursor.fetchall()

    for i in resultado:
        print "%s %s %s %s" % (i[0], i[1], i[2], i[3])

    cursor.close()

    print ""
    raw_input("Presione una tecla para continuar...")

    main()

def buscar():

    print "Buscar contacto"
    print "---------------"
    print ""

    con = sqlite3.connect("agenda.db")
    cursor = con.cursor()

    buscar = raw_input("Nombre a buscar: ")

    cursor.execute("SELECT * FROM datos WHERE nombre = '%s'" % (buscar))

    x = cursor.fetchall()

    print ""

    for i in x:
        print "Nombre:", i[0]
        print "Apellido:", i[1]
        print "Telefono:", i[2]
        print "Correo:", i[3]
        print ""

    cursor.close()

    print ""
    raw_input("Presione una tecla para continuar...")

    main()

def eliminar():

    print "Eliminar contacto"
    print "-----------------"
    print ""

    con = sqlite3.connect("agenda.db")
    cursor = con.cursor()

    eliminar = raw_input("Nombre de contacto a eliminar: ")

    cursor.execute("DELETE FROM datos WHERE nombre='%s'" % (eliminar))

    con.commit()

    cursor.close()

    print "Contacto eliminao correctamente..."

    raw_input()

    main()

def main():

    limpiar()
    
    print """
    [1] Ingresar Contacto
    [2] Listar Contactos
    [3] Buscar Contacto
    [4] Eliminar Contacto
    [0] Salir
    """
    opcion = raw_input("Ingresa una opción -> ")

    if opcion != "1" and opcion != "2" and opcion != "3" and opcion != "4" and opcion != "5" and opcion != "0":
        print "Opcion incorrecta"
        raw_input()
        main()

    elif opcion == "1":
        limpiar()
        agregar()

    elif opcion == "2":
        limpiar()
        ver()

    elif opcion == "3":
        limpiar()
        buscar()

    elif opcion == "4":
        limpiar()
        eliminar()

    elif opcion == "0":
        print ""
        print "Bye..."
        print ""
        print ""
        time.sleep(3)
        exit()
main()