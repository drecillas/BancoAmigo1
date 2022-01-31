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
from Sample_App import SampleApp
import var

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

  mydb=pyodbc.connect(driver='{SQL Server}', server='10.10.58.33', database='Gangrena', trusted_Connection='yes')
  mycursor=mydb.cursor()
  mycursor.execute("use Gangrena")
  mycursor.execute("select accit from usuario")
  values=mycursor.fetchall()
  user_acc=[]
  for i in values:
    user_acc.append(i[0])

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

              mycursor.execute(f"SELECT pw FROM usuario WHERE accit={var.username1}")
              values=mycursor.fetchall()
              mydb.commit()
              user_pass=[]
              for i in values:
                  user_pass.append(i[0])

              user_pass_1=str(user_pass[0])

              if var.password1=='':
                  messagebox.showwarning('Alerta',('Ingrese una contraseña!'))
                  var.username_entry1.delete(0, END)
                  var.password_entry1.delete(0,END)
              elif var.password1 == str(user_pass_1) :
                  mycursor.execute(f"select nombre from usuario where accit={var.username1}")
                  values=mycursor.fetchall()
                  user_name=[]
                  for i in values:
                    user_name.append(i[0])
                  var.user_display_name=str(user_name[0])

                  mycursor.execute(f"select apellido_pa from usuario where accit={var.username1}")
                  values=mycursor.fetchall()
                  apep_name=[]
                  for i in values:
                    apep_name.append(i[0])
                  var.apep_display_name=str(apep_name[0])

                  mycursor.execute(f"select apellido_ma from usuario where accit={var.username1}")
                  values=mycursor.fetchall()
                  apem_name=[]
                  for i in values:
                    apem_name.append(i[0])
                  var.apem_display_name=str(apem_name[0])

                  mycursor.execute(f"select correo from usuario where accit={var.username1}")
                  values=mycursor.fetchall()
                  mail_name=[]
                  for i in values:
                    mail_name.append(i[0])
                  var.mail=str(mail_name[0])

                  mycursor.execute(f"select id_usuario from usuario where accit={var.username1}")
                  values=mycursor.fetchall()
                  apem_name=[]
                  for i in values:
                    apem_name.append(i[0])
                  var.ID_display=str(apem_name[0])

                  mycursor.execute(f"select telefono from usuario where accit={var.username1}")
                  values=mycursor.fetchall()
                  telf_name=[]
                  for i in values:
                    telf_name.append(i[0])
                  var.telf_display_name=str(telf_name[0])
                  mydb=pyodbc.connect(driver='{SQL Server}', server='10.10.58.33', database='Gangrena', trusted_Connection='yes')
                  mycursor=mydb.cursor()
                  mycursor.execute("use Gangrena")
                  mycursor.execute(f'select balance from usuario where accit={var.username1}')
                  values=mycursor.fetchall()
                  user_balance=[]
                  for i in values:
                    user_balance.append(i[0])
                  user_balance_1=float(user_balance[0])
                  var.current_balance=user_balance_1

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
