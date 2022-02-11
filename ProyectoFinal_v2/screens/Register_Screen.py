
from tkinter import *
from tkinter import messagebox
from tkinter import BOTH, END, LEFT
import tkinter as tk
from tkinter import ttk 
import random
from tkinter import scrolledtext as st
from validar.Register import register_user
from screens import var


def register():

            var.screen1 = Toplevel(var.screen)
            var.screen1.title("REGISTRO")
            var.screen1.state('zoomed')
            var.screen1.configure(bg='#1e1e2d')
            var.screen1.iconphoto(False,tk.PhotoImage(file='imagenes/abc.png'))
            photo = PhotoImage(file="imagenes/bancoamigos.png")
            img = photo.subsample(2)
            label = Label(var.screen1,image=img,bg='#1e1e2d')
            label.image = img
            label.place(x=440, y=50 )

            var.username = StringVar()
            var.password = StringVar()
            var.name     = StringVar()
            var.telf     = StringVar()
            var.apellidoP = StringVar()
            var.apellidoM = StringVar()
            var.Correo_info = StringVar()
            var.option_var = StringVar()
            
            label = Label(var.screen1, text = "Nombre(s)",font = ("Lucida Console", 14),bg='#1e1e2d',fg='white')
            label.place(x=370, y=270)
            var.name_entry = Entry(var.screen1,font = ("Lucida Console",14), textvariable = var.name,bg='white', justify = "center")
            var.name_entry.place(x=370, y=300)
            
            label = Label(var.screen1, text = "Tu numero de cuenta es:",font = ("Lucida Console", 14),bg='#1e1e2d',fg='white')
            label.place(x=720, y=470)
            var.rand1=random.randint(1,100000)
            var.username=Label(var.screen1, text = var.rand1,font = ("Lucida Console", 14,'bold'),bg='#1e1e2d', fg='white')
            var.username.place(x=720, y=490)
            
            label = Label(var.screen1, text = "Apellido Paterno",font = ("Lucida Console", 14),bg='#1e1e2d',fg='white')
            label.place(x=370, y=340)
            var.apellP_entry =  Entry(var.screen1,font = ("Lucida Console",14), textvariable = var.apellidoP,bg='white', justify = "center")
            var.apellP_entry.place(x=370, y=370)
            
            label = Label(var.screen1, text = "Apellido Materno",font = ("Lucida Console", 14),bg='#1e1e2d',fg='white')
            label.place(x=370, y=410)
            var.apellM_entry =  Entry(var.screen1,font = ("Lucida Console",14), textvariable = var.apellidoM,bg='white', justify = "center")
            var.apellM_entry.place(x=370, y=440)
            
            def generar():
                  label = Label(var.screen1, text = "Tu correo es:",bg='#1e1e2d', fg='white',font = ("Lucida Console", 10))
                  label.place(x= 397, y=520)
                  def info():
                        messagebox.showinfo('Alerta',('Ingrese Nombre completo y apellidos para generar correo'))
                        var.screen1.destroy()
                        
                  if var.apellidoM.get()=="" or var.apellidoP.get()=="" or var.name.get()=="":
                        info()
                  else:
                        button1['state'] = tk.DISABLED
                        var.Correo_info= (var.name.get()[0]+var.apellidoP.get()[0:3]+var.apellidoM.get()+"@hola.com").lower()
                        label = Label(var.screen1, text = var.Correo_info,bg='#1e1e2d',fg='white',font = ("Lucida Console", 10, 'bold'))
                        label.place(x= 397, y=540)
                        
            button1= tk.Button(var.screen1,text = "Generar correo",fg='#663259', bg = "#c2d5e3", width = "16", font = ("Lucida Console", 12, 'bold'),command=generar)
            button1.place(x= 397, y=480)
            
            label = Label(var.screen1, text = "Telefono",font = ("Lucida Console", 14),bg='#1e1e2d',fg='white')
            label.place(x=720, y=270)
            var.tel_entry =  Entry(var.screen1,font = ("Lucida Console",14), textvariable = var.telf,bg='white', justify = "center")
            var.tel_entry.place(x=720, y=300)
            
            label = Label(var.screen1, text = "Contraseña",font = ("Lucida Console", 14),bg='#1e1e2d',fg='white')
            label.place(x=720, y=340)
            var.password_entry =  Entry(var.screen1,font = ("Lucida Console",14), textvariable = var.password,bg='white', justify = "center")
            var.password_entry.config(show='●')
            var.password_entry.place(x=720, y=370)
            
            languages = ('Gerente', 'Supervisor', 'Cajero')
            label = Label(var.screen1,  text='Seleciona tu Posición', font= ("Lucida Console", 14), bg='#1e1e2d',fg='white')
            label.place(x=720, y=410)
            
            option_menu = ttk.OptionMenu(var.screen1, var.option_var,languages[0],*languages)
            option_menu.place(x=720, y=440)
            button_reg = Button(var.screen1,text = "REGISTRARSE",fg='white', bg = "#663259", width = "21", height = "2", font = ("Lucida Console", 12,'bold'),command=register_user)
            button_reg.place(x=555, y=565)
            
            if var.option_var =="Gerente":
                  var.option_var = int("1")
            elif var.option_var =="Supervisor":
                  var.option_var = int("2")
            elif var.option_var =="Cajero":
                  var.option_var = int("3")
            else:
                        print("Incorrecto")
