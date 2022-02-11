from tkinter import *
from tkinter import BOTH, END, LEFT
import tkinter as tk
from tkinter import ttk 
from tkinter import scrolledtext as st
from validar.Login import login_verify
from screens import var

def login():
  var.screen2 = Toplevel(var.screen)
  var.screen2.title("INGRESO")
  var.screen2.state('zoomed')
  var.screen2.configure(bg='#1e1e2d')
  var.screen2.iconphoto(False,tk.PhotoImage(file='imagenes/abc.png'))
  photo = PhotoImage(file="imagenes/bancoamigos.png")
  photo1 = PhotoImage(file="imagenes/barra.png")
  label = Label(var.screen2, image=photo , bg='#1e1e2d')
  label.image = photo
  label.place(x=90, y=100)
  label = Label(var.screen2, width=10, image=photo1 , bg='#1e1e2d')
  label.image = photo1
  label.place(x=800, y=180)
  label1 = Label(var.screen2, text="Bienvenido", bg='#1e1e2d',fg='white', font=("Comic Sans MS", 50))
  label1.place(x=500, y=100)
  var.username_verify = StringVar()
  var.password_verify = StringVar()
  global username_entry1
  global password_entry1
  label = ttk.Label(var.screen2, text = "Numero de cuenta",font = ("Lucida Console", 14), background = '#1e1e2d', foreground="white")
  label.place(x=880, y=255)
  var.username_entry1 = ttk.Entry(var.screen2,font = ("Lucida Console",14) ,textvariable = var.username_verify, justify = "center")
  var.username_entry1.place(x=860, y=290)
  label = ttk.Label(var.screen2, text = "Contraseña",font = ("Lucida Console", 14), background = '#1e1e2d', foreground="white")
  label.place(x=920, y=320)
  var.password_entry1 = ttk.Entry(var.screen2,font = ("Lucida Console",14), textvariable = var.password_verify, justify = "center")
  var.password_entry1.config(show='●')
  var.password_entry1.place(x=860, y=350)

  button_log = tk.Button(var.screen2,text = "Iniciar Sesión", background = '#663259', foreground = '#c2d5e3', width = "20", font = ("Lucida Console",14),command=login_verify)
  button_log.place(x=860, y=430)
