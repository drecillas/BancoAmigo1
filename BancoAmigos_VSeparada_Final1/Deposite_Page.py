
from tkinter import *
from tkinter import messagebox
from tkinter import BOTH, END, LEFT
import tkinter as tk
import random
import pyodbc
from tkinter import scrolledtext as st
import var

class DepositPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='#1e1e2d')
        self.controller = controller

        self.balance_var = tk.StringVar()
        controller.shared_data['Balance'].trace('w', self.on_balance_changed)
        upperframe=tk.Frame(self,bg='#1e1e2d')
        upperframe.pack(fill='both',expand='True')

        balance_label = tk.Label(self, textvariable=self.balance_var, font=('Lucida Console',15,'bold'),fg='yellow', bg='#1e1e2d')
        balance_label.place(x=540, y=193)

        heading=tk.Label(self,text='Cajero Banco Amigos',font=('Lucida Console',45,'bold'),foreground='white',background='#1e1e2d')
        heading.place(x=330, y=93)

        space_label=tk.Label(self,height=4,bg='#1e1e2d').pack()

        enter_amount_label=tk.Label(self,text='INGRESA LA CANTIDAD A DEPOSITAR',font=('Lucida Console',13,'bold'),bg='#1e1e2d',fg='white').pack(pady=10)

        cash=tk.StringVar()
        deposit_entry=tk.Entry(self,textvariable=cash,font=('Lucida Console',20,'bold'),width=22)
        deposit_entry.pack(ipady=7)

        def deposit_cash(self):
            global current_balance
            try:
                val=int(cash.get())
                if int(val)<0:
                    messagebox.showwarning('Alerta','Ingresa una cantidad correcta!')
                    cash.set('')
                else:
                    var.current_balance += int(val)
                    curr2=str(val)
                    curr = str(var.current_balance)
                    messagebox.askquestion('Confirmación','Estas seguro que deseas realizar el deposito?')
                    messagebox.showinfo('DEPOSITO','Deposito exitoso!')
                    controller.shared_data['Balance'].set(var.current_balance)

                    cash.set('')
                    mydb=pyodbc.connect(driver='{SQL Server}', server='10.10.58.33', database='Gangrena', trusted_Connection='yes')
                    mycursor=mydb.cursor()
                    mycursor.execute("use Gangrena")
                    mycursor.execute(f"update usuario set balance ={var.current_balance} where accit = {var.username1} ")

                    sql = "select SYSDATETIME ()"
                    mycursor.execute(sql)
                    fecha_alt = mycursor.fetchval()
                    fecha_alt = str(fecha_alt)
        
                    sql="select id_cat_operaciones from cat_operaciones where id_cat_operaciones = 3"
                    mycursor.execute(sql)
                    operaciones = mycursor.fetchval()
                    operaciones = str(operaciones)

                    rand=random.randint(1,100000)
                    rand = str(rand)

                    mycursor.execute(f"SELECT  id_cuenta_banc FROM cuenta_bancaria WHERE id_usuario = {var.ID_display}")
                    id_cuenta_ban = mycursor.fetchval()
                    id_cuenta_ban = str(id_cuenta_ban)

                    mycursor.execute("INSERT INTO estado_cuenta values ('"+rand+"', '"+fecha_alt+"', '"+curr2+"', '"+id_cuenta_ban+"', '"+operaciones+"')")

                    mydb.commit()

            except ValueError:
                messagebox.showwarning('WARNING','Invadlid Input!')
                cash.set('')
        deposit_entry.bind('<Return>',deposit_cash)
        enter_button=tk.Button(self,text='Depositar',font=('Lucida Console',13),command=lambda:[deposit_cash(self)],relief='raised',borderwidth=3,width=23,height=3)
        enter_button.pack(pady=10)

        two_tone_label=tk.Label(self,bg='#1e1e2d')
        two_tone_label.pack(fill='both',expand=True)

        def exit():
            controller.show_frame('MenuPage')

        exit_button=tk.Button(self,text='REGRESAR AL MENU',font=('Lucida Console',13),command=exit,relief='raised',borderwidth=3,width=23,height=3)
        exit_button.pack(pady=10)

    def on_balance_changed(self, *args):
        self.balance_var.set('Saldo Actual: $'+str(self.controller.shared_data['Balance'].get()))
