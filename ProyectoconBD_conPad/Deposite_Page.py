
from tkinter import *
from tkinter import messagebox
from tkinter import BOTH, END, LEFT
import tkinter as tk
import random
import pyodbc
from tkinter import scrolledtext as st
import var
from bd import conectar
from math import *
nums=""
class DepositPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='#1e1e2d')
        self.controller = controller
        self.balance_var = tk.StringVar()
        controller.shared_data['Balance'].trace('w', self.on_balance_changed)
        controller.shared_data['Balance'].set(var.current_balance)
        upperframe=tk.Frame(self,bg='#1e1e2d')
        upperframe.pack(fill='both',expand='True')
        rightframe=tk.Frame(self,bg='#1e1e2d')
        rightframe.pack(fill='y',expand='False',side='right')
        balance_label = tk.Label(self, textvariable=self.balance_var, font=('Lucida Console',15,'bold'),fg='yellow', bg='#1e1e2d')
        balance_label.place(x=530, y=193)
        heading=tk.Label(self,text='Cajero Banco Amigos',font=('Lucida Console',45,'bold'),foreground='white',background='#1e1e2d')
        heading.place(x=330, y=93)
        enter_amount_label=tk.Label(self,text='INGRESA LA CANTIDAD A DEPOSITAR',font=('Lucida Console',13,'bold'),bg='#1e1e2d',fg='white')
        enter_amount_label.place(x=500, y=270)
        cash=tk.StringVar()
        deposit_entry=tk.Entry(self,textvariable=cash,font=('Lucida Console',20,'bold'),width=22,justify="right")
        deposit_entry.place(x=480, y=330)
        deposit_entry.focus_set()
        nums=""
        
        def btnClik(num):
            global nums
            nums=nums+str(num)
            cash.set(nums)
        
        def clear():
            global nums
            nums=("")
            cash.set("")
            
        def deposit_cash(self):
            global current_balance
            try:
                val=int(cash.get())
                if int(val)<0:
                    messagebox.showwarning('Alerta','Ingresa una cantidad correcta!')
                    cash.set('')
                else:
                    var.current_balance += int(val)
                    var.curr2=str(val)
                    curr = str(var.current_balance)
                    messagebox.askquestion('Confirmación','Estas seguro que deseas realizar el deposito?')
                    messagebox.showinfo('DEPOSITO','Deposito exitoso!')
                    controller.shared_data['Balance'].set(var.current_balance)
                    cash.set('')
                    deposito = conectar.deposito_bd()
            except ValueError:
                messagebox.showwarning('WARNING','Invadlid Input!')
                cash.set('')
        
        deposit_entry.bind('<Return>',deposit_cash)
        
        enter_button=tk.Button(self,text='Depositar',font=('Lucida Console',13),command=lambda:[deposit_cash(self)],relief='raised',borderwidth=3,width=23,height=3)
        enter_button.place(x=560,y=450)
        
        Button(self, text="1",width=8,height=5,command=lambda:btnClik(1)).place(x=1050,y=290)
        Button(self, text="2",width=8,height=5,command=lambda:btnClik(2)).place(x=1130,y=290)
        Button(self, text="3",width=8,height=5,command=lambda:btnClik(3)).place(x=1210,y=290)
        
        Button(self, text="4",width=8,height=5,command=lambda:btnClik(4)).place(x=1050,y=390)
        Button(self, text="5",width=8,height=5,command=lambda:btnClik(5)).place(x=1130,y=390)
        Button(self, text="6",width=8,height=5,command=lambda:btnClik(6)).place(x=1210,y=390)

        Button(self, text="7",width=8,height=5,command=lambda:btnClik(7)).place(x=1050,y=490)
        Button(self, text="8",width=8,height=5,command=lambda:btnClik(8)).place(x=1130,y=490)
        Button(self, text="9",width=8,height=5,command=lambda:btnClik(9)).place(x=1210,y=490)

        Button(self, text="0",width=8,height=5,command=lambda:btnClik(0)).place(x=1050,y=590)
        Button(self, text="C",width=8,height=5,command=clear).place(x=1210,y=590)
        
        
        def exit():
            controller.show_frame('MenuPage')

        exit_button=tk.Button(self,text='REGRESAR AL MENU',font=('Lucida Console',13),command=exit,relief='raised',borderwidth=3,width=23,height=3)
        exit_button.pack(pady=10)
    def on_balance_changed(self, *args):
        self.balance_var.set('Saldo Actual: $'+str(self.controller.shared_data['Balance'].get()))
