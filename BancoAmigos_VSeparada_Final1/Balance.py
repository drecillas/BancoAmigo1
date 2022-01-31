
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

class BalancePage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='#1e1e2d')
        self.controller = controller
        balance_label = tk.Label(self, text='', font=('Lucida Console',30,'bold'),fg='white', bg='#1e1e2d', anchor='w')
        balance_label.pack()
        heading=tk.Label(self,text='Cajero Banco Amigos',font=('Lucida Console',45,'bold'),foreground='white',background='#1e1e2d')
        heading.pack(pady=25)

        self.balance_var = tk.StringVar()
        controller.shared_data['Balance'].trace('w', self.on_balance_changed)
        controller.shared_data['Balance'].set(var.current_balance)
        upperframe=tk.Frame(self,bg='#1e1e2d')
        upperframe.pack(fill='both',expand='True')

        balance_label = tk.Label(upperframe, textvariable=self.balance_var, font=('Lucida Console',30,'bold'),fg='white', bg='#1e1e2d', anchor='w')
        balance_label.pack(pady=7)

        button_frame=tk.Label(self,bg='#1e1e2d')
        button_frame.pack(side='left',expand='True')

        def menu():
            controller.show_frame('MenuPage')

        menu_button=tk.Button(button_frame,command=menu,text='Menu',font=('Lucida Console',13),relief='raised',borderwidth=3,width=23,height=4)
        menu_button.pack(pady=6)

        def exit():
            controller.show_frame('StartPage')

        exit_button=tk.Button(button_frame,text='Salir',command=exit,font=('Lucida Console',13),relief='raised',borderwidth=3,width=23,height=4)
        exit_button.pack(pady=7)

    def on_balance_changed(self, *args):
        self.balance_var.set('Saldo Actual: $'+str(self.controller.shared_data['Balance'].get()))
