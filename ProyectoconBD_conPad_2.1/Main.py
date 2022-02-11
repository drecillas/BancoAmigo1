    ################## IMPORTAMOS MODULOS #################################
from tkinter import *
from tkinter import BOTH, END, LEFT
import tkinter as tk
from PIL import Image,ImageTk
from tkinter import scrolledtext as st
from Register_Screen import register
from Login_Screen import login
import var
                              
################## Nuestro Saldo  #################################
current_balance=0.00

################## ABOUT SCREEN #################################
def about():
    global screen3
    screen3 = Toplevel(var.screen)
    screen3.title("About")
    screen3.geometry("380x90+750+230")
    screen3.configure(bg='lightblue')
    screen3.iconphoto(False,tk.PhotoImage(file='imagenes/abc.png'))
################## REGISTER/LOGIN SCREEN #################################
def main_screen():
    global screen
    var.screen = Tk()
    var.screen.state('zoomed')
    var.screen.title("BANCO AMIGOS")
    var.screen.configure(bg='#1e1e2d')
    var.screen.iconphoto(False,tk.PhotoImage(file="imagenes/abc.png"))
    Label(text = "", width = "300",bg='#1e1e2d').pack()
    img = ImageTk.PhotoImage(Image.open("imagenes/bancoamigos.png"))
    panel = Label(var.screen, image = img,bg='#1e1e2d',width = "550", height = "350")
    panel.pack()
    Label(text = "",bg='#1e1e2d').pack()
    Button(text = "INGRESAR",fg='#663259', bg = "#c2d5e3", width = "21", height = "2", font = ("Lucida Console", 12,'bold'),command=login).pack(pady=5)
    Label(text = "",bg='#1e1e2d').pack()
    Button(text = "REGISTRARSE",fg='white', bg = "#663259", width = "21", height = "2", font = ("Lucida Console", 12,'bold'),command=register).pack(pady=5)
    Label(text = "",bg='#1e1e2d').pack()
    var.screen.mainloop()
main_screen()