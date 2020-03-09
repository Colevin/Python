from tkinter import *
from tkinter import messagebox
import sqlite3
def conexionBBDD():
    miConexion = sqlite3.connect("Usuarios")
    miCursor = miConexion.cursor()
    try:
        miCursor.execute('''
        CREATE TABLE DATOSUSUARIOS (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        NOMBRE_USUARIO VARCHAR(50),
        PASSWORD VARCHAR(50),
        APELLIDO VARCHAR(10),
        DIRECCION VARCHAR(50),
        COMENTARIOS VARCHAR(100))
        ''')
        messagebox.showinfo("BBDD", "BBDD creada con exito")
    except:
        messagebox.showinfo("!Atencion¡", "La BBDD ya existe")

root = Tk()