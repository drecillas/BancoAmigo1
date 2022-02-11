from tkinter import *
from tkinter import messagebox
import  tkinter.messagebox
from tkinter import BOTH, END, LEFT
import tkinter as tk
from tkinter import ttk 
import os
from PIL import Image,ImageTk
import time
import random
import pyodbc
from tkinter import scrolledtext as st
from screens.Sample_App import SampleApp
from screens import var
from BaseDatos.bd import conectar
def abcd():   
        app = SampleApp()
        app.mainloop()

def user_not_found():
      messagebox.showwarning('Alerta',('Usuario no encontrado !'))

def password_not_recognised():
  messagebox.showwarning('Atención',('Contraseña invalida!'))

def login_verify():
  var.username1 = var.username_verify.get()
  var.password1 = var.password_verify.get()
  var.username_entry1.delete(0, END)
  var.password_entry1.delete(0, END)
  login = conectar.login_bd()
  user_acc = var.user_acc
  if var.username1.isalpha():
        messagebox.showwarning('Atención',('Ingrese un numero de cuenta valido!'))
        var.screen2.destroy()

  if str(var.username1)=='':
        messagebox.showwarning('Atención',('Ingrese un numero de usuario!'))
        var.password_entry1.delete(0,END)
        var.screen2.destroy()
  elif str(var.username1).isspace():
        messagebox.showwarning('Antención',('Ingrese un numero de usuario!'))
        var.screen2.destroy()
  elif var.username1.isalnum():
      if var.username1.isdigit():
          if int(var.username1) in user_acc:
              password= conectar.login_contraBD()
              user_pass_1 = var.user_pass_1
              if var.password1=='':
                  messagebox.showwarning('Alerta',('Ingrese una contraseña!'))
                  var.username_entry1.delete(0, END)
                  var.password_entry1.delete(0,END)
              elif var.password1 == str(user_pass_1) :
                  comprobacion = conectar.login_comprobacionBD()
                  var.screen2.destroy()
                  var.screen.destroy()
                  abcd()
              elif var.password1!= str(user_pass_1):
                  password_not_recognised()
          else:
              user_not_found()
      else:
          user_not_found()
  else:
        user_not_found()
