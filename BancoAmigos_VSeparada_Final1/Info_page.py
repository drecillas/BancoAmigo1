
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
import var
#from Main import login_verify

class InfoPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='#1e1e2d')
        self.controller = controller
        heading=tk.Label(self,text='CAJERO BANCO AMIGOS',font=('Lucida Console',45,'bold'),foreground='white',background='#1e1e2d')
        heading.pack(pady=25)
        main_menu_label=tk.Label(self,text='Informacion personal',font=('Lucida Console',20,'bold'),fg='white',bg='#1e1e2d')
        main_menu_label.pack(pady=5)

        upperframe=tk.Frame(self,bg='#1e1e2d')
        upperframe.pack(fill='both',expand='True')

        button_frame=tk.Frame(self,bg='#1e1e2d')
        button_frame.pack(fill='both')

        mydb=pyodbc.connect(driver='{SQL Server}', server='10.10.58.33', database='Gangrena', trusted_Connection='yes')
        mycursor=mydb.cursor()
        mycursor.execute("use Gangrena")
        mycursor.execute(f"select pw from usuario where accit = {var.username1} ")
        pass_code=mycursor.fetchone()
        pass_code_read=''
        for i in pass_code:
            pass_code_read+=i

        name=tk.Label(upperframe, text=f'NOMBRE: ', font=('Lucida Console',16),fg='white', bg='#1e1e2d').pack(pady=5)
        name_info =tk.Label(upperframe, text= f'{var.user_display_name} {var.apep_display_name} {var.apem_display_name}',font=('Lucida Console',16,'bold'),fg='yellow',bg='#1e1e2d').pack(pady=5)

        tel= tk.Label(upperframe, text=f'NUMERO DE TELEFONO:', font=('Lucida Console',16),fg='white', bg='#1e1e2d').pack(pady=5)
        telf_info =tk.Label(upperframe, text=f'{var.telf_display_name}',font=('Lucida Console',16,'bold'),fg='yellow',bg='#1e1e2d').pack(pady=5)

        ac=tk.Label(upperframe, text=f'NUMERO DE CUENTA:', font=('Lucida Console',16),fg='white', bg='#1e1e2d').pack(pady=5)
        accid_info = tk.Label(upperframe, text=f'{var.username1}',font=('Lucida Console',16,'bold'),fg='yellow',bg='#1e1e2d').pack(pady=5)
        
        cor= tk.Label(upperframe, text=f'CORREO:', font=('Lucida Console',16),fg='white', bg='#1e1e2d').pack(pady=5)
        correo= tk.Label(upperframe, text=f'{var.mail}',font=('Lucida Console',16,'bold'),fg='yellow',bg='#1e1e2d').pack(pady=5)
        def exit():
            controller.show_frame('MenuPage')

        exit_button=tk.Button(button_frame,text='Menu',command=exit,font=('Lucida Console',13),relief='raised',borderwidth=3,width=23,height=4)
        exit_button.pack(pady=20,padx=10)
