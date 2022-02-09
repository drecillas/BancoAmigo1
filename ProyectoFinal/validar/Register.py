
from tkinter import *
from tkinter import messagebox
from tkinter import BOTH, END, LEFT
import random
import pyodbc
from tkinter import scrolledtext as st
from screens import var
from BaseDatos.bd import conectar
def register_user():
    
  global username_info
  rand=random.randint(1,100000)
  rand = str(rand)
  username_info = str(rand)
  password_info = var.password.get()
  name_info     = var.name.get().upper()
  telf_info     = var.telf.get()
  apellidoP_info= var.apellidoP.get().upper()
  apellidoM_info= var.apellidoM.get().upper()
  Correo_info  = Correo_info= (var.name.get()[0]+var.apellidoP.get()[0:3]+var.apellidoM.get()+"@hola.com").lower()

  
  ################## COMPROBACION CON BD ##################
  global label_may
  global label_con
  global mycursor
  registro = conectar.registro_bd()
  a = var.a
  b = var.b
  if username_info in b:
    label = Label(var.screen1, text = "El Usuario ingresado ya existe  ",bg='#1e1e2d', fg='orange',font = ("Lucida Console", 11,'bold'))
    label.place(x= 720, y=520)
    var.name_entry.delete(0,END)
  elif telf_info in a:
    label = Label(var.screen1, text = "El telefono ingresado ya existe",bg='#1e1e2d', fg='orange',font = ("Lucida Console", 11,'bold'))
    label.place(x= 720, y=520)
    var.tel_entry.delete(0,END)
  elif name_info=='' :
        label = Label(var.screen1, text = "Ingresa un nombre",bg='#1e1e2d', fg='orange',font = ("Lucida Console", 11,'bold'))
        label.place(x= 720, y=520)
        var.password_entry.delete(0,END)
  elif password_info=='' or len(password_info)<=8 :
        label_con = Label(var.screen1, text = "Ingresa una Contraseña valida            ",bg='#1e1e2d', fg='orange',font = ("Lucida Console", 11,'bold'))
        label_con.place(x= 720, y=520)
        var.password_entry.delete(0,END)
  elif re.search('[0-9]',password_info) is None:
        label_num = Label(var.screen1, text = "Contraseña con por lo menos un numero    ",bg='#1e1e2d', fg='orange',font = ("Lucida Console", 11,'bold'))
        label_num.place(x= 720, y=520)
        var.password_entry.delete(0,END)
  elif re.search('[A-Z]',password_info) is None:
        label_may = Label(var.screen1, text = "Contraseña con minimo una letra mayuscula",bg='#1e1e2d', fg='orange',font = ("Lucida Console", 11,'bold'))
        label_may.place(x= 720, y=520)
        var.password_entry.delete(0,END)
  elif telf_info=='' or len(telf_info) != 10 :
        label = Label(var.screen1, text = "Numero de telefono invalido       ",bg='#1e1e2d', fg='orange',font = ("Lucida Console", 11,'bold'))
        label.place(x= 720, y=520)
        var.password_entry.delete(0,END)
        var.tel_entry.delete(0,END)
  elif apellidoP_info=='' :
        label = Label(var.screen1, text = "Ingresa apellido paterno          ",bg='#1e1e2d', fg='orange',font = ("Lucida Console", 11,'bold'))
        label.place(x= 720, y=520)
        var.password_entry.delete(0,END)

  elif apellidoM_info=='' :
        label = Label(var.screen1, text = "Ingresa apellido materno          ",bg='#1e1e2d', fg='orange',font = ("Lucida Console", 11,'bold'))
        label.place(x= 720, y=520)
        var.password_entry.delete(0,END)

  else:       
        registro_puesto = conectar.regis_bd_puesto()
        messagebox.showinfo('Registro',('Exitoso!'))
        var.screen1.destroy()