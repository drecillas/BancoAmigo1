
from tkinter import *
from tkinter import BOTH, END, LEFT
import tkinter as tk
from tkinter import scrolledtext as st
import var
#from balance import Balance_Page

class MenuPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='#1e1e2d')
        self.controller = controller
        controller.shared_data['Balance'].set(var.current_balance)

        heading=tk.Label(self,text='CAJERO BANCO AMIGOS',font=('Lucida Console',45,'bold'),foreground='white',bg = "#1e1e2d")
        heading.pack(pady=25)
        slection_label=tk.Label(self,text='Selecciona una opción',font=('Lucida Console',25,'bold'),fg='white',bg='#1e1e2d')
        slection_label.pack(fill='x',pady=5)

        button_frame=tk.Frame(self,bg='#1e1e2d')
        button_frame.pack(fill='both',expand='True')

        def withdraw():
            controller.show_frame('WithdrawPage')

        withdraw_button=tk.Button(button_frame,text='RETIRO',font=('Lucida Console',13),command=withdraw,relief='raised',borderwidth=3,width=30,height=4)
        withdraw_button.place(x=100, y=100, width=300, height=100)

        def deposit():
            controller.show_frame('DepositPage')

        deposit_button=tk.Button(button_frame,text='DEPOSITO',font=('Lucida Console',13),command=deposit,relief='raised',borderwidth=3,width=30,height=4)
        deposit_button.place(x=100, y=220, width=300, height=100)
        def balance():
            controller.show_frame('BalancePage')

        def info():
            controller.show_frame('InfoPage')

        info_button=tk.Button(button_frame,text='INFO DE USUARIO',font=('Lucida Console',13),command=info,relief='raised',borderwidth=3,width=30,height=4)
        info_button.place(x=900, y=220, width=300, height=100)

        def lista():
            controller.show_frame('TablaPage')

        tabla_button=tk.Button(button_frame,text='ESTADO DE CUENTA',font=('Lucida Console',13),command=lista,relief='raised',borderwidth=3,width=30,height=4)
        tabla_button.place(x=900, y=100, width=300, height=100)

        def transfer():
            controller.show_frame('TransferPage')

        trasf_button=tk.Button(button_frame,text='TRANSFERENCIA',font=('Lucida Console',13),command=transfer,relief='raised',borderwidth=3,width=30,height=4)
        trasf_button.place(x=100, y=340, width=300, height=100)

        def about_us():
            controller.show_frame('About_Info')

        trasf_button=tk.Button(button_frame,text='ACERCA DE NOSOTROS',font=('Lucida Console',13),command=about_us,relief='raised',borderwidth=3,width=30,height=4)
        trasf_button.place(x=900, y=340, width=300, height=100)

        def exit():
            controller.show_frame('StartPage')

        ################################################################
        self.balance_var = tk.StringVar()
        controller.shared_data['Balance'].trace('w', self.on_balance_changed)
        upperframe=tk.Frame(self,bg='#1e1e2d')

        balance_label = tk.Label(self, textvariable=self.balance_var, font=('Lucida Console',15,'bold'),fg='yellow', bg='#1e1e2d')
        balance_label.place(x=530, y=193)
        #################################################################

        exit_button=tk.Button(button_frame,text='SALIR',font=('Lucida Console',13),command=exit,relief='raised',borderwidth=3,width=30,height=4)
        exit_button.place(x=620, y=390, width=100, height=50)

    def on_balance_changed(self, *args):
        self.balance_var.set('Saldo Actual: $'+str(self.controller.shared_data['Balance'].get()))
