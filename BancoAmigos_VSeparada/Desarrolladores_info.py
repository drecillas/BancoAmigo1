
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

class About_Info(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='#1e1e2d')

        self.controller = controller

        heading=tk.Label(self,text='Acerca de',font=('Lucida Console',45,'bold'),foreground='white',background='#1e1e2d')
        heading.pack(pady=25)
        main_menu_label=tk.Label(self,text='DESARROLLADORES',font=('Lucida Console',20,'bold'),fg='white',bg='#1e1e2d')
        main_menu_label.pack(pady=5)

        upperframe=tk.Frame(self,bg='#1e1e2d')
        upperframe.pack(fill='both',expand='True')

        button_frame=tk.Frame(self,bg='#1e1e2d')
        button_frame.pack(fill='both')

        tk.Label(upperframe, text=f'Desarrolladores Front-End: ', font=('Lucida Console',16),fg='yellow', bg='#1e1e2d').pack(pady=5)
        tk.Label(upperframe, text= f'Jesus Aaron Dominguez Rodriguez',font=('Lucida Console',16,'bold'),fg='white',bg='#1e1e2d').pack(pady=5)
        tk.Label(upperframe, text= f'Antonio Alberto Noh Campos',font=('Lucida Console',16,'bold'),fg='white',bg='#1e1e2d').pack(pady=5)

        tk.Label(upperframe, text=f'Desarrolladores Back-End:', font=('Lucida Console',16),fg='yellow', bg='#1e1e2d').pack(pady=5)
        tk.Label(upperframe, text=f'Alexis Omar Galvan Lozano',font=('Lucida Console',16,'bold'),fg='white',bg='#1e1e2d').pack(pady=5)
        tk.Label(upperframe, text=f'David Fabrizio Recillas Abarca',font=('Lucida Console',16,'bold'),fg='white',bg='#1e1e2d').pack(pady=5)

        tk.Label(upperframe, text=f'Desarrollo Base de Datos:', font=('Lucida Console',16),fg='yellow', bg='#1e1e2d').pack(pady=5)
        tk.Label(upperframe, text=f'Guadalupe Quiroz Quiroz',font=('Lucida Console',16,'bold'),fg='white',bg='#1e1e2d').pack(pady=5)
        
        def exit():
            controller.show_frame('MenuPage')

        exit_button=tk.Button(button_frame,text='Menu',command=exit,font=('Lucida Console',13),relief='raised',borderwidth=3,width=23,height=4)
        exit_button.pack(pady=20,padx=10)

