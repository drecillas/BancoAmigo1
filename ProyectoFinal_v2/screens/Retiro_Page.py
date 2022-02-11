
from tkinter import *
from tkinter import messagebox
from tkinter import BOTH, END, LEFT
import tkinter as tk
import random
import pyodbc
from tkinter import scrolledtext as st
from screens import var
from BaseDatos.bd import conectar
                                
class WithdrawPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='#1e1e2d')
        self.controller = controller
        heading=tk.Label(self,text='CAJERO BANCO AMIGOS',font=('Lucida Console',45,'bold'),foreground='white',background='#1e1e2d')
        heading.pack(pady=25)
        controller.shared_data['Balance'].set(var.current_balance)
        choose_amount_label=tk.Label(self,text='ELIGE LA CANTIDAD A RETIRAR',font=('Lucida Console',17,'bold'),fg='white',bg='#1e1e2d')
        choose_amount_label.pack()
        button_frame=tk.Frame(self,bg='#1e1e2d')
        button_frame.pack(fill='both',expand='True')
        self.balance_var = tk.StringVar()
        controller.shared_data['Balance'].trace('w', self.on_balance_changed)
        upperframe=tk.Frame(self,bg='#1e1e2d')
        upperframe.pack(fill='both',expand='True')
        balance_label = tk.Label(self, textvariable=self.balance_var, font=('Lucida Console',15,'bold'),fg='yellow', bg='#1e1e2d')
        balance_label.place(x=530, y=193)
        
        global curr2
        def withdraw(amount):
            if amount>var.current_balance:
                messagebox.showwarning('WARNING','SALDO INSUFICIENTE!')
                other_amount_entry.delete(0,END)
            else:
                response= messagebox.askquestion('Confirmación','Estas seguro que deseas realizar el retiro?')
                if response == "yes":
                    var.current_balance -= amount
                    var.curr2=str(amount)
                    curr = str(var.current_balance)
                    
                    messagebox.showinfo('RETIRO','EXITOSO!')
                    other_amount_entry.delete(0,END)
                    controller.shared_data['Balance'].set(var.current_balance)
                    retiro = conectar.retiro_user()
                else:
                    messagebox.showinfo('RETIRO','CANCELADO!')
                    var.curr=0
        twenty_button=tk.Button(button_frame,text='$20',font=('Lucida Console',12),command=lambda:withdraw(20),relief='raised',borderwidth=3,width=30,height=4)
        twenty_button.grid(row=0,column=0,pady=5)
        fourty_button=tk.Button(button_frame,text='$40',font=('Lucida Console',12),command=lambda:withdraw(40),relief='raised',borderwidth=3,width=30,height=4)
        fourty_button.grid(row=1,column=0,pady=5)
        sixty_button=tk.Button(button_frame,text='$60',font=('Lucida Console',12),command=lambda:withdraw(60),relief='raised',borderwidth=3,width=30,height=4)
        sixty_button.grid(row=2,column=0,pady=5)
        eighty_button=tk.Button(button_frame,text='$80',font=('Lucida Console',12),command=lambda:withdraw(80),relief='raised',borderwidth=3,width=30,height=4)
        eighty_button.grid(row=3,column=0,pady=5)
        one_hundred_button=tk.Button(button_frame,text='$100',font=('Lucida Console',12),command=lambda:withdraw(100),relief='raised',borderwidth=3,width=30,height=4)
        one_hundred_button.grid(row=0,column=1,pady=5,padx=794)
        two_hundred_button=tk.Button(button_frame,text='$200',font=('Lucida Console',12),command=lambda:withdraw(200),relief='raised',borderwidth=3,width=30,height=4)
        two_hundred_button.grid(row=1,column=1,pady=5)
        three_hundred_button=tk.Button(button_frame,text='$300',font=('Lucida Console',12),command=lambda:withdraw(300),relief='raised',borderwidth=3,width=30,height=4)
        three_hundred_button.grid(row=2,column=1,pady=5)
        cash=tk.StringVar()
        other_amount_entry=tk.Entry(button_frame,font=('Lucida Console',12),textvariable=cash,width=25,justify='center')
        other_amount_entry.place(x=1110, y=340, height=40)
        peso=tk.Label(self,text='$',font=('Lucida Console',20,'bold'),foreground='white',background='#1e1e2d')
        peso.place(x=1085, y=485, height=40)
        other_amount_heading=tk.Button(button_frame,text='OTRA CANTIDAD',font=('Lucida Console',15,'bold'),borderwidth=0,relief='sunken',activeforeground='white',activebackground='#33334d',bg='#1e1e2d',fg='white')
        other_amount_heading.place(x=1140, y=275, height=40)
        
        def other_amount(self):
            global current_balance
            try:
                var.val=int(cash.get())
                if int(cash.get())>var.current_balance:
                    messagebox.showwarning('ATENCIÓN','SALDO INSUFICIENTE!')
                    other_amount_entry.delete(0,END)
                elif int(cash.get())<0:
                    messagebox.showwarning('ANTENCIÓN','INGRESA UNA CANTIDAD CORRECTA!')
                    other_amount_entry.delete(0,END)
                else:
                    
                    r=messagebox.askquestion('Confirmación','Estas seguro que deseas realizar el retiro?')
                    if r=='yes':
                        var.current_balance -= int(cash.get())
                        var.curr2=str(var.val)
                        messagebox.showinfo('RETIRO','EXITOSO!')
                        controller.shared_data['Balance'].set(var.current_balance)
                        cash.set('')
                        otra_cantidad = conectar.other_amount()
                    else:
                        cash.set("")
                        var.curr=0
            except ValueError:
                messagebox.showwarning('WARNING','Invadlid Input!')
                cash.set('')
        other_amount_entry.bind('<Return>',other_amount)
        
        def exit():
            controller.show_frame('MenuPage')
            
        exit_button=tk.Button(button_frame,text='Regresar al Menu',command=exit,font=('Lucida Console',13),relief=RIDGE,borderwidth=3,width=23,height=4)
        exit_button.place(x=30, y=365)
        enter_button=tk.Button(self,text='Retirar',font=('Lucida Console',13),command=lambda:[other_amount(self)],width=23,height=3)
        enter_button.place(x=1120, y= 540)
        
    def on_balance_changed(self, *args):
        self.balance_var.set('Saldo Actual: $'+str(self.controller.shared_data['Balance'].get()))