
from tkinter import *
from tkinter import messagebox
from tkinter import BOTH, END, LEFT
import tkinter as tk
import random
import pyodbc
from tkinter import scrolledtext as st
import var
from bd import conectar
class TransferPage(tk.Frame):
        def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent,bg='#1e1e2d')
            self.controller = controller
            self.controller.title('BANCO AMIGOS')
            self.controller.state('zoomed')
            global transferencia
            space_label=tk.Label(self,height=6,bg='#1e1e2d').pack()
            heading=tk.Label(self,text='TRANSFERENCIA BANCO AMIGOS',font=('Lucida Console',45,'bold'),foreground='white',background='#1e1e2d')
            heading.pack(pady=25)
            button_frame=tk.Frame(self,bg='#1e1e2d')
            button_frame.pack(fill='y',expand='False')
            space_label=tk.Label(button_frame,height=2,bg='#1e1e2d')
            space_label.grid(row=2,column=1)
            enter_amount_label=tk.Label(button_frame,text='INGRESA LA CANTIDAD A TRANSFERIR',font=('Lucida Console',13,'bold'),bg='#1e1e2d',fg='white')
            enter_amount_label.grid(pady=7)
            deposito=tk.StringVar()
            deposito_entry=tk.Entry(button_frame,textvariable=deposito,font=('Lucida Console',20,'bold'),width=22)
            deposito_entry.grid(pady=8)
            enter_amount_label1=tk.Label(button_frame,text='INGRESA LA CUENTA A TRANSFERIR',font=('Lucida Console',13,'bold'),bg='#1e1e2d',fg='white')
            enter_amount_label1.grid(pady=9)
            transferencia=tk.StringVar()
            transferencia_entry=tk.Entry(button_frame,textvariable=transferencia,font=('Lucida Console',20,'bold'),width=22)
            transferencia_entry.grid(pady=10)
            self.balance_var = tk.StringVar()
            controller.shared_data['Balance'].trace('w', self.on_balance_changed)
            upperframe=tk.Frame(self,bg='#1e1e2d')
            upperframe.pack(fill='both',expand='True')
            balance_label = tk.Label(self, textvariable=self.balance_var, font=('Lucida Console',15,'bold'),fg='yellow', bg='#1e1e2d')
            balance_label.place(x=530, y=193)
            
            def transfer(self):
                global current_balance
                try:
                    var.transferencia = transferencia.get()
                    var.dep= deposito.get()
                    val=int(var.dep)
                    saldocliente=var.current_balance
                    if int(var.dep)>var.current_balance:
                        messagebox.showwarning('ATENCIÓN','SALDO INSUFICIENTE!')
                        deposito_entry.delete(0,END)
                    elif int(var.dep)<0:
                        messagebox.showwarning('ATENCIÓN','INGRESA UNA CANTIDAD CORRECTA!')
                        deposito_entry.delete(0,END)
                    else:
                        responde =messagebox.askquestion('Confirmación','¿Estas seguro que deseas realizar la transferencia?')
                        if responde == "yes":
                            var.current_balance -= int(var.dep)
                            var.curr2=str(val)
                            controller.shared_data['Balance'].set(var.current_balance)
                        
                            transfer = conectar.transferencia_bd()
                            username2 = var.transferencia
                            messagebox.showinfo('TRANSFERENCIA','Transferencia exitosa!')                  
                            deposito_entry.delete(0,END)
                            transferencia_entry.delete(0,END)
                        else:
                            messagebox.showinfo('TRANSFERENCIA','Transferencia cancelada!')                  

                except ValueError:
                    messagebox.showwarning('WARNING','Invadlid Input!')
            transferencia_entry.bind('<Return>',transfer)    
            button_frame=tk.Label(self,bg='#1e1e2d')
            button_frame.pack(side='left',expand='True')
            pass            
            def exit():
                controller.show_frame('MenuPage')
            enter_button=tk.Button(self,text='Transferir',font=('Lucida Console',13),command=lambda:[transfer(self)],relief='raised',borderwidth=3,width=23,height=3)
            enter_button.place(x=550, y=445)
            exit_button=tk.Button(button_frame,text='Regresar al Menu',command=exit,font=('Lucida Console',13),width=18,height=2)
            exit_button.grid()

        def on_balance_changed(self, *args):
            self.balance_var.set('Saldo Actual: $'+str(self.controller.shared_data['Balance'].get()))
        
