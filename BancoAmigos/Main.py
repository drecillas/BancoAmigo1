################## IMPORTAMOS MODULOS #################################
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
############################################################ CLASES DEL BANCO ############################################################

################## Nuestro Saldo  #################################
current_balance=0.00

class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.shared_data={'Balance':tk.IntVar()}

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}
        ################## INITIALIZING PAGES IN CONTAINER #################################
        for F in (StartPage, MenuPage, TransferPage, WithdrawPage,DepositPage,BalancePage,InfoPage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

################## PAGINA DE INICIO(STARPAGE) #################################
class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='#1e1e2d')
        self.controller = controller
        self.controller.title('BANCO AMIGOS')
        self.controller.state('zoomed')
        self.controller.iconphoto(False,tk.PhotoImage(file='imagenes/abc.png'))
        space_label=tk.Label(self,height=6,bg='#1e1e2d').pack()
        heading=tk.Label(self,text='Banco Amigos',font=('orbitron',45,'bold'),foreground='white',background='#1e1e2d')
        heading.pack(pady=25)
        bien= tk.Label(self, text=f'BIENVENIDO',font=('BatmanForeverAlternate',25),bg='#1e1e2d',fg='white').pack(pady=10)
        Name=tk.Label(self,text=f'{user_display_name} {apep_display_name} {apem_display_name}',font=('orbitron',20,'bold'),foreground='yellow',background='#1e1e2d').pack(pady=10)
        def next_page():
            controller.show_frame('MenuPage')

        entry_button = tk.Button(self,text='ACCEDER',fg='#663259', bg = "#c2d5e3", width = "24", height = "3",font=("orbitron", 12,'bold'),command=next_page,relief='raised').pack(pady=10)

        def Quit():
            self.controller.destroy()

        def popup():
            response=messagebox.askyesno('Salir','Seguro que deseas salir?')

            if response == 1:
                return Quit()
            else:
                return

        quit1 = tk.Button(self,text='SALIR',fg='white', bg = "#663259", width = "24", height = "3",font=("orbitron", 12,'bold'),command=popup,relief='raised').pack(pady=10)


        dualtone_label=tk.Label(self, text='',font=('orbitron',13),fg='white',bg='#1e1e2d',anchor='n')
        dualtone_label.pack(fill='both',expand='True')

        def changescreen():
            self.controller.destroy()
            main_screen()

        def popup2():
            response=messagebox.askyesno('Salir','Quieres usar otra cuenta?')

            if response == 1:
                return changescreen()
            else:
                return

        register_login_screen = tk.Button(dualtone_label,text='Usar otra cuenta',fg='white', bg = "#663259",font=("orbitron", 12,'bold'),command=popup2,relief='raised',borderwidth=3,width=23,height=3).pack(pady=10,padx=10,side='bottom',anchor='e')

        ################## BOTTOM FRAME #################################
        bottom_frame=tk.Frame(self,relief='raised',borderwidth=3).pack(fill='x',side='bottom')

        visa_photo= tk.PhotoImage(file='imagenes/visa.png')
        visa_label=tk.Label(bottom_frame,image=visa_photo)
        visa_label.pack(side='left')
        visa_label.image=visa_photo

        mastercard_photo= tk.PhotoImage(file='imagenes/mastercard.png')
        mastercard_label=tk.Label(bottom_frame,image=mastercard_photo)
        mastercard_label.pack(side='left')
        mastercard_label.image=mastercard_photo

        american_express_photo= tk.PhotoImage(file='imagenes/american_express.png')
        american_express_label=tk.Label(bottom_frame,image=american_express_photo)
        american_express_label.pack(side='left')
        american_express_label.image=american_express_photo

        def tick():
            current_time=time.strftime('%I:%M %p')
            time_label.config(text=current_time)
            time_label.after(200,tick)


        time_label=tk.Label(bottom_frame,font=('orbitron',12))
        time_label.pack(side='right')
        tick()

################## PAGINA MENU(MENUPAGE) #################################
class MenuPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='#1e1e2d')
        self.controller = controller

        heading=tk.Label(self,text='CAJERO BANCO AMIGOS',font=('orbitron',45,'bold'),foreground='white',bg = "#1e1e2d")
        heading.pack(pady=25)
        slection_label=tk.Label(self,text='Selecciona una opción',font=('orbitron',25,'bold'),fg='white',bg='#1e1e2d')
        slection_label.pack(fill='x',pady=5)

        button_frame=tk.Frame(self,bg='#1e1e2d')
        button_frame.pack(fill='both',expand='True')

        def withdraw():
            controller.show_frame('WithdrawPage')

        withdraw_button=tk.Button(button_frame,text='RETIRO',font=('orbitron',13),command=withdraw,relief='raised',borderwidth=3,width=30,height=4)
        withdraw_button.grid(row=0,column=0,pady=7)

        def deposit():
            controller.show_frame('DepositPage')

        deposit_button=tk.Button(button_frame,text='DEPOSITO',font=('orbitron',13),command=deposit,relief='raised',borderwidth=3,width=30,height=4)
        deposit_button.grid(row=1,column=0,pady=5)
        def balance():
            controller.show_frame('BalancePage')

        balance_button=tk.Button(button_frame,text='SALDO',font=('orbitron',13),command=balance,relief='raised',borderwidth=3,width=30,height=4)
        balance_button.grid(row=0,column=1,pady=7,padx=794)

        def info():
            controller.show_frame('InfoPage')

        info_button=tk.Button(button_frame,text='INFO DE USUARIO',font=('orbitron',13),command=info,relief='raised',borderwidth=3,width=30,height=4)
        info_button.grid(row=1,column=1,pady=5)

        def transfer():
            controller.show_frame('TransferPage')

        trasf_button=tk.Button(button_frame,text='TRANSFERENCIA',font=('orbitron',13),command=transfer,relief='raised',borderwidth=3,width=30,height=4)
        trasf_button.grid(row=2,column=0,pady=5)

        def exit():
            controller.show_frame('StartPage')


        exit_button=tk.Button(button_frame,text='SALIR',font=('orbitron',13),command=exit,relief='raised',borderwidth=3,width=30,height=4)
        exit_button.grid(row=2,column=1,pady=5)

class TransferPage(tk.Frame):
    
    def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent,bg='#1e1e2d')
            self.controller = controller
            self.controller.title('BANCO AMIGOS')
            self.controller.state('zoomed')
            space_label=tk.Label(self,height=6,bg='#1e1e2d').pack()
            heading=tk.Label(self,text='TRANSFERENCIA BANCO AMIGOS',font=('orbitron',45,'bold'),foreground='white',background='#1e1e2d')
            heading.pack(pady=25)
            button_frame=tk.Frame(self,bg='#1e1e2d')
            button_frame.pack(fill='y',expand='False')
            space_label=tk.Label(button_frame,height=2,bg='#1e1e2d')
            space_label.grid(row=2,column=1)

            enter_amount_label=tk.Label(button_frame,text='INGRESA LA CANTIDAD A TRANSFERIR',font=('orbitron',13,'bold'),bg='#1e1e2d',fg='white')
            enter_amount_label.grid(pady=7)

            deposito=tk.StringVar()
            deposito_entry=tk.Entry(button_frame,textvariable=deposito,font=('orbitron',20,'bold'),width=22)
            deposito_entry.grid(pady=8)

            enter_amount_label1=tk.Label(button_frame,text='INGRESA LA CUENTA A TRANSFERIR',font=('orbitron',13,'bold'),bg='#1e1e2d',fg='white')
            enter_amount_label1.grid(pady=9)
            
            transferencia=tk.StringVar()
            transferencia_entry=tk.Entry(button_frame,textvariable=transferencia,font=('orbitron',20,'bold'),width=22)
            transferencia_entry.grid(pady=10)
            def transfer(_):
                global current_balance
                try:
                    val=int(deposito.get())
                    if int(deposito.get())>current_balance:
                        messagebox.showwarning('ATENCIÓN','SALDO INSUFICIENTE!')
                        deposito_entry.delete(0,END)
                    elif int(deposito.get())<0:
                        messagebox.showwarning('ATENCIÓN','INGRESA UNA CANTIDAD CORRECTA!')
                        deposito_entry.delete(0,END)
                    else:
                        current_balance -= int(deposito.get())
                        controller.shared_data['Balance'].set(current_balance)
                        messagebox.askquestion('Confirmación','Estas seguro que deseas realizar la transferencia?')
                        mydb=pyodbc.connect(driver='{SQL Server}', server='10.10.58.33', database='Gangrena', trusted_Connection='yes')
                        mycursor=mydb.cursor()
                        mycursor.execute("use Gangrena")
                        mycursor.execute(f"update usuario set balance ={current_balance} where accit = {username1} ")
                        mydb.commit()
                
                    username2 = transferencia.get()
                    mydb=pyodbc.connect(driver='{SQL Server}', server='10.10.58.33', database='Gangrena', trusted_Connection='yes')
                    mycursor=mydb.cursor()
                    mycursor.execute("use Gangrena")
                    mycursor.execute(f'select balance from usuario where accit={username2}')
                    values=mycursor.fetchall()
                    new_balance=[]
                    for i in values:
                        new_balance.append(i[0])
                    new_balance_1=float(new_balance[0])
                    new_balance=new_balance_1
                
                    new_balance += int(deposito.get())
                    messagebox.showinfo('TRANSFERENCIA','Transferencia exitosa!')
                    controller.shared_data['Balance'].set(new_balance)
                    username2 = transferencia.get()
                    mydb=pyodbc.connect(driver='{SQL Server}', server='10.10.58.33', database='Gangrena', trusted_Connection='yes')
                    mycursor=mydb.cursor()
                    mycursor.execute("use Gangrena")
                    mycursor.execute(f"update usuario set balance ={new_balance} where accit = {username2} ")
                    mydb.commit()


                except ValueError:
                    messagebox.showwarning('WARNING','Invadlid Input!')
            transferencia_entry.bind('<Return>',transfer)

        
            button_frame=tk.Label(self,bg='#1e1e2d')
            button_frame.pack(side='left',expand='True')
            def exit():
                controller.show_frame('MenuPage')

            enter_button=tk.Button(button_frame,text='Transferir',font=('orbitron',13),relief=RIDGE,borderwidth=3,width=23,height=4,command=transfer)

            exit_button=tk.Button(button_frame,text='Regresar al Menu',command=exit,font=('orbitron',13),relief=RIDGE,borderwidth=3,width=23,height=4)
            exit_button.grid()

################## PAGINA DE RETIRO(WITGDRAWPAGE) #################################
class WithdrawPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='#1e1e2d')
        self.controller = controller

        heading=tk.Label(self,text='CAJERO BANCO AMIGOS',font=('orbitron',45,'bold'),foreground='white',background='#1e1e2d')
        heading.pack(pady=25)
        choose_amount_label=tk.Label(self,text='ELIGE LA CANTIDAD A RETIRAR',font=('orbitron',17,'bold'),fg='white',bg='#1e1e2d')
        choose_amount_label.pack()
        button_frame=tk.Frame(self,bg='#1e1e2d')
        button_frame.pack(fill='both',expand='True')

        def withdraw(amount):
            global current_balance
            if amount>current_balance:
                messagebox.showwarning('WARNING','SALDO INSUFICIENTE!')
                other_amount_entry.delete(0,END)
            else:

                current_balance -= amount
                curr = str(current_balance)
                messagebox.askquestion('Confirmación','Estas seguro que deseas realizar la transferencia?')
                messagebox.showinfo('RETIRO','EXITOSO!')
                other_amount_entry.delete(0,END)
                controller.shared_data['Balance'].set(current_balance)
                mydb=pyodbc.connect(driver='{SQL Server}', server='10.10.58.33', database='Gangrena', trusted_Connection='yes')
                mycursor=mydb.cursor()
                mycursor.execute("use Gangrena")
                mycursor.execute(f"update usuario set balance ={current_balance} where accit = {username1} ")

                sql = "select SYSDATETIME ()"
                mycursor.execute(sql)
                fecha_alt = mycursor.fetchval()
                fecha_alt = str(fecha_alt)
        
                sql="select id_cat_operaciones from cat_operaciones where id_cat_operaciones = 2"
                mycursor.execute(sql)
                operaciones = mycursor.fetchval()
                operaciones = str(operaciones)

                rand=random.randint(1,100000)
                rand = str(rand)

                mycursor.execute(f"SELECT  id_cuenta_banc FROM cuenta_bancaria WHERE id_usuario = {ID_display}")
                id_cuenta_ban = mycursor.fetchval()
                id_cuenta_ban = str(id_cuenta_ban)

                mycursor.execute("INSERT INTO estado_cuenta values ('"+rand+"', '"+fecha_alt+"', '"+curr+"', '"+id_cuenta_ban+"', '"+operaciones+"')")

                mydb.commit()

                controller.show_frame('MenuPage')



        twenty_button=tk.Button(button_frame,text='$20',font=('orbitron',12),command=lambda:withdraw(20),relief='raised',borderwidth=3,width=30,height=4)
        twenty_button.grid(row=0,column=0,pady=5)

        fourty_button=tk.Button(button_frame,text='$40',font=('orbitron',12),command=lambda:withdraw(40),relief='raised',borderwidth=3,width=30,height=4)
        fourty_button.grid(row=1,column=0,pady=5)

        sixty_button=tk.Button(button_frame,text='$60',font=('orbitron',12),command=lambda:withdraw(60),relief='raised',borderwidth=3,width=30,height=4)
        sixty_button.grid(row=2,column=0,pady=5)

        eighty_button=tk.Button(button_frame,text='$80',font=('orbitron',12),command=lambda:withdraw(80),relief='raised',borderwidth=3,width=30,height=4)
        eighty_button.grid(row=3,column=0,pady=5)

        one_hundred_button=tk.Button(button_frame,text='$100',font=('orbitron',12),command=lambda:withdraw(100),relief='raised',borderwidth=3,width=30,height=4)
        one_hundred_button.grid(row=0,column=1,pady=5,padx=794)

        two_hundred_button=tk.Button(button_frame,text='$200',font=('orbitron',12),command=lambda:withdraw(200),relief='raised',borderwidth=3,width=30,height=4)
        two_hundred_button.grid(row=1,column=1,pady=5)

        three_hundred_button=tk.Button(button_frame,text='$300',font=('orbitron',12),command=lambda:withdraw(300),relief='raised',borderwidth=3,width=30,height=4)
        three_hundred_button.grid(row=2,column=1,pady=5)

        cash=tk.StringVar()
        other_amount_entry=tk.Entry(button_frame,font=('orbitron',12),textvariable=cash,width=28,justify='right')
        other_amount_entry.grid(row=3,column=1,pady=4,ipady=30)

        other_amount_heading=tk.Button(button_frame,text='OTRA CANTIDAD',font=('orbitron',15,'bold'),borderwidth=0,relief='sunken',activeforeground='white',activebackground='#33334d',bg='#1e1e2d',fg='white')
        other_amount_heading.grid(row=4,column=1)

        def other_amount(_):
            global current_balance
            try:
                val=int(cash.get())

                if int(cash.get())>current_balance:
                    messagebox.showwarning('ATENCIÓN','SALDO INSUFICIENTE!')
                    other_amount_entry.delete(0,END)
                elif int(cash.get())<0:
                    messagebox.showwarning('ANTENCIÓN','INGRESA UNA CANTIDAD CORRECTA!')
                    other_amount_entry.delete(0,END)
                else:

                    current_balance -= int(cash.get())
                    curr = str(current_balance)
                    controller.shared_data['Balance'].set(current_balance)
                    cash.set('')
                    messagebox.askquestion('Confirmación','Estas seguro que deseas realizar la transferencia?')
                    messagebox.showinfo('RETIRO','EXITOSO!')
                    controller.show_frame('MenuPage')
                    mydb=pyodbc.connect(driver='{SQL Server}', server='10.10.58.33', database='Gangrena', trusted_Connection='yes')
                    mycursor=mydb.cursor()
                    mycursor.execute("use Gangrena")
                    mycursor.execute(f"update usuario set balance ={current_balance} where accit = {username1} ")

                    sql = "select SYSDATETIME ()"
                    mycursor.execute(sql)
                    fecha_alt = mycursor.fetchval()
                    fecha_alt = str(fecha_alt)
        
                    sql="select id_cat_operaciones from cat_operaciones where id_cat_operaciones = 2"
                    mycursor.execute(sql)
                    operaciones = mycursor.fetchval()
                    operaciones = str(operaciones)

                    rand=random.randint(1,100000)
                    rand = str(rand)

                    mycursor.execute(f"SELECT  id_cuenta_banc FROM cuenta_bancaria WHERE id_usuario = {ID_display}")
                    id_cuenta_ban = mycursor.fetchval()
                    id_cuenta_ban = str(id_cuenta_ban)

                    mycursor.execute("INSERT INTO estado_cuenta values ('"+rand+"', '"+fecha_alt+"', '"+curr+"', '"+id_cuenta_ban+"', '"+operaciones+"')")


                    mydb.commit()
            except ValueError:
                messagebox.showwarning('WARNING','Invadlid Input!')
                cash.set('')

        other_amount_entry.bind('<Return>',other_amount)

        def exit():
            controller.show_frame('MenuPage')

        exit_button=tk.Button(button_frame,text='Menu',command=exit,font=('orbitron',13),relief=RIDGE,borderwidth=3,width=23,height=4)
        exit_button.grid(row=4,column=0)
################## PAGINA DE DEPOSITO(DEPOSITPAGE) #################################
class DepositPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='#1e1e2d')
        self.controller = controller

        heading=tk.Label(self,text='Cajero Banco Amigos',font=('orbitron',45,'bold'),foreground='white',background='#1e1e2d')
        heading.pack(pady=25)

        space_label=tk.Label(self,height=4,bg='#1e1e2d').pack()

        enter_amount_label=tk.Label(self,text='INGRESA LA CANTIDAD A DEPOSITAR',font=('orbitron',13,'bold'),bg='#1e1e2d',fg='white').pack(pady=10)

        cash=tk.StringVar()
        deposit_entry=tk.Entry(self,textvariable=cash,font=('orbitron',20,'bold'),width=22)
        deposit_entry.pack(ipady=7)

        def deposit_cash():
            global current_balance
            try:
                val=int(cash.get())
                if int(val)<0:
                    messagebox.showwarning('Alerta','Ingresa una cantidad correcta!')
                    cash.set('')
                else:
                    current_balance += int(val)
                    curr = str(current_balance)
                    messagebox.askquestion('Confirmación','Estas seguro que deseas realizar la transferencia?')
                    messagebox.showinfo('DEPOSITO','Deposito exitoso!')
                    controller.shared_data['Balance'].set(current_balance)
                    controller.show_frame('MenuPage')
                    cash.set('')
                    mydb=pyodbc.connect(driver='{SQL Server}', server='10.10.58.33', database='Gangrena', trusted_Connection='yes')
                    mycursor=mydb.cursor()
                    mycursor.execute("use Gangrena")
                    mycursor.execute(f"update usuario set balance ={current_balance} where accit = {username1} ")

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

                    mycursor.execute(f"SELECT  id_cuenta_banc FROM cuenta_bancaria WHERE id_usuario = {ID_display}")
                    id_cuenta_ban = mycursor.fetchval()
                    id_cuenta_ban = str(id_cuenta_ban)

                    mycursor.execute("INSERT INTO estado_cuenta values ('"+rand+"', '"+fecha_alt+"', '"+curr+"', '"+id_cuenta_ban+"', '"+operaciones+"')")

                    mydb.commit()

            except ValueError:
                messagebox.showwarning('WARNING','Invadlid Input!')
                cash.set('')


        enter_button=tk.Button(self,text='Enter',font=('orbitron',13),command=deposit_cash,relief='raised',borderwidth=3,width=23,height=3)
        enter_button.pack(pady=10)

        two_tone_label=tk.Label(self,bg='#1e1e2d')
        two_tone_label.pack(fill='both',expand=True)

        def exit():
            controller.show_frame('MenuPage')

        exit_button=tk.Button(self,text='REGRESAR AL MENU',font=('orbitron',13),command=exit,relief='raised',borderwidth=3,width=23,height=3)
        exit_button.pack(pady=10)
        
################## PAGINA DE NUESTRO SALDO(BALANCEPAGE) #################################
class BalancePage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='#1e1e2d')
        self.controller = controller
        balance_label = tk.Label(self, text='', font=('orbitron',30,'bold'),fg='white', bg='#1e1e2d', anchor='w')
        balance_label.pack()
        heading=tk.Label(self,text='Cajero Banco Amigos',font=('orbitron',45,'bold'),foreground='white',background='#1e1e2d')
        heading.pack(pady=25)

        self.balance_var = tk.StringVar()
        controller.shared_data['Balance'].trace('w', self.on_balance_changed)
        controller.shared_data['Balance'].set(current_balance)
        upperframe=tk.Frame(self,bg='#1e1e2d')
        upperframe.pack(fill='both',expand='True')

        balance_label = tk.Label(upperframe, textvariable=self.balance_var, font=('orbitron',30,'bold'),fg='white', bg='#1e1e2d', anchor='w')
        balance_label.pack(pady=7)

        button_frame=tk.Label(self,bg='#1e1e2d')
        button_frame.pack(side='left',expand='True')

        def menu():
            controller.show_frame('MenuPage')

        menu_button=tk.Button(button_frame,command=menu,text='Menu',font=('orbitron',13),relief='raised',borderwidth=3,width=23,height=4)
        menu_button.pack(pady=6)

        def exit():
            controller.show_frame('StartPage')

        exit_button=tk.Button(button_frame,text='Salir',command=exit,font=('orbitron',13),relief='raised',borderwidth=3,width=23,height=4)
        exit_button.pack(pady=7)

    def on_balance_changed(self, *args):
        self.balance_var.set('Saldo Actual: $'+str(self.controller.shared_data['Balance'].get()))

class InfoPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='#1e1e2d')
        self.controller = controller

        heading=tk.Label(self,text='CAJERO BANCO AMIGOS',font=('orbitron',45,'bold'),foreground='white',background='#1e1e2d')
        heading.pack(pady=25)
        main_menu_label=tk.Label(self,text='Informacion personal',font=('orbitron',20,'bold'),fg='white',bg='#1e1e2d')
        main_menu_label.pack(pady=5)

        upperframe=tk.Frame(self,bg='#1e1e2d')
        upperframe.pack(fill='both',expand='True')

        button_frame=tk.Frame(self,bg='#1e1e2d')
        button_frame.pack(fill='both')

        mydb=pyodbc.connect(driver='{SQL Server}', server='10.10.58.33', database='Gangrena', trusted_Connection='yes')
        mycursor=mydb.cursor()
        mycursor.execute("use Gangrena")
        mycursor.execute(f"select pw from usuario where accit = {username1} ")
        pass_code=mycursor.fetchone()
        pass_code_read=''
        for i in pass_code:
            pass_code_read+=i

        name=tk.Label(upperframe, text=f'NOMBRE: ', font=('orbitron',16),fg='white', bg='#1e1e2d').pack(pady=5)
        name_info =tk.Label(upperframe, text= f'{user_display_name} {apep_display_name} {apem_display_name}',font=('orbitron',16,'bold'),fg='yellow',bg='#1e1e2d').pack(pady=5)

        tel= tk.Label(upperframe, text=f'NUMERO DE TELEFONO:', font=('orbitron',16),fg='white', bg='#1e1e2d').pack(pady=5)
        telf_info =tk.Label(upperframe, text=f'{telf_display_name}',font=('orbitron',16,'bold'),fg='yellow',bg='#1e1e2d').pack(pady=5)

        ac=tk.Label(upperframe, text=f'NUMERO DE CUENTA:', font=('orbitron',16),fg='white', bg='#1e1e2d').pack(pady=5)
        accid_info = tk.Label(upperframe, text=f'{username1}',font=('orbitron',16,'bold'),fg='yellow',bg='#1e1e2d').pack(pady=5)
        
        cor= tk.Label(upperframe, text=f'CORREO:', font=('orbitron',16),fg='white', bg='#1e1e2d').pack(pady=5)
        correo= tk.Label(upperframe, text=f'{mail}',font=('orbitron',16,'bold'),fg='yellow',bg='#1e1e2d').pack(pady=5)
        def exit():
            controller.show_frame('MenuPage')

        exit_button=tk.Button(button_frame,text='Menu',command=exit,font=('orbitron',13),relief='raised',borderwidth=3,width=23,height=4)
        exit_button.pack(pady=20,padx=10)

################## CLASS  DEFINE FUNCTION #################################
def abcd():

        app = SampleApp()
        app.mainloop()

############################################################ REGISTER/LOGIN ############################################################
def password_not_recognised():
  messagebox.showwarning('Atención',('Contraseña invalida!'))

################## ABOUT SCREEN #################################
def about():
  global screen3
  screen3 = Toplevel(screen)
  screen3.title("About")
  screen3.geometry("380x90+750+230")
  screen3.configure(bg='lightblue')
  screen3.iconphoto(False,tk.PhotoImage(file='imagenes/abc.png'))
  
################## WARNING_SCREEN #################################
def user_not_found():
  messagebox.showwarning('Alerta',('Usuario no encontrado !'))

################## REGISTER USER SCREEN #################################
def register_user():
  global username_info
  username_info = str(rand)
  password_info = password.get()
  name_info     = name.get().upper()
  telf_info     = telf.get()
  apellidoP_info= apellidoP.get().upper()
  apellidoM_info= apellidoM.get().upper()
  Correo_info  = Correo_info= (name.get()[0]+apellidoP.get()[0:3]+apellidoM.get()+"@hola.com").lower()
  option_var.get()
  poss_info     = option_var.get()
  if poss_info  =="Gerente":
     poss_info  = "1"
  elif poss_info  =="Supervisor":
        poss_info  = "2"
  elif poss_info  =="Cajero":
        poss_info = "3"
  else:
            print("Incorrecto")
  

  ################## SQL DATABASE ##################
  global mycursor
  mydb=pyodbc.connect(driver='{SQL Server}', server='10.10.58.33', database='Gangrena', trusted_Connection='yes')
  mycursor=mydb.cursor()
  mycursor.execute("use Gangrena")
  mydb.commit()

  mycursor.execute('select accit from usuario')
  values=mycursor.fetchall()

  b=[]
  for i in values:
      b.append(i[0])
  if username_info in b:
    messagebox.showwarning('Alerta',('El usuario ya existe!'))

    password_entry.delete(0,END)
    name_entry.delete(0,END)
    apellM_entry.delete(0,END)
    apellP_entry.delete(0, END)
    correo_entry.delete(0, END)
    tel_entry.delete(0, END)


  elif name_info=='' :
        messagebox.showwarning('WARNING',('Ingresa un nombre!'))
        password_entry.delete(0,END)
  elif password_info=='' or len(password_info)<=8 :
        messagebox.showwarning('WARNING',('Ingresa una contraseña valida!'))
        
  elif re.search('[0-9]',password_info) is None:
        messagebox.showwarning('Alerta',('ASEGURATE DE QUE TU CONTRASEÑA CONTENGA POR LO MENOS UN NUMERO'))
        password_entry.delete(0,END)
  elif re.search('[A-Z]',password_info) is None: 
        messagebox.showwarning('Alerta',('ASEGURATE DE QUE TU CONTRASEÑA CONTENGA POR LO MENOS UNA LETRA MAYUSCULA'))
        password_entry.delete(0,END)

  elif telf_info=='' or len(telf_info) != 10 :
        messagebox.showwarning('WARNING',('Ingresa un telefono valido!'))
        password_entry.delete(0,END)
  elif apellidoP_info=='' :
        messagebox.showwarning('WARNING',('Ingresa apellido paterno!'))
  elif apellidoM_info=='' :
        messagebox.showwarning('WARNING',('Ingresa apellido materno!'))
        password_entry.delete(0,END)
  elif Correo_info=='' :
        messagebox.showwarning('WARNING',('Ingresa un correo!'))
  else:
       
        balance_inti = option_var.get()
        if balance_inti  =="Gerente":
            sql="select salario from cat_salario_puesto where id_cat_salario_puesto =1"
            mycursor.execute(sql)
            balance_inti  = mycursor.fetchval()
            balance_inti = str(balance_inti)
        elif balance_inti  =="Supervisor":
            sql="select salario from cat_salario_puesto where id_cat_salario_puesto =2"
            mycursor.execute(sql)
            balance_inti  = mycursor.fetchval()
            balance_inti = str(balance_inti)
        elif balance_inti  =="Cajero":
            sql="select salario from cat_salario_puesto where id_cat_salario_puesto =3"
            mycursor.execute(sql)
            balance_inti  = mycursor.fetchval()
            balance_inti = str(balance_inti)
        else:
            print("Incorrecto")
        password_entry.delete(0, END)
        name_entry.delete(0, END)
        apellM_entry.delete(0,END)
        apellP_entry.delete(0, END)
        tel_entry.delete(0, END) 
        id_usuario=str(1)
        id_cat_cuentas=str(1)
        sql = "select SYSDATETIME ()"
        mycursor.execute(sql)
        fecha_alt = mycursor.fetchval()
        fecha_alt = str(fecha_alt)


        mycursor.execute("insert into usuario values('"+name_info+"', '"+apellidoP_info+"', '"+apellidoM_info+"', '"+telf_info+"', '"+Correo_info+"', '"+password_info+"', '"+poss_info+"', '"+balance_inti+"','"+username_info+"')")
        

        sql = "SELECT TOP 1 id_usuario FROM usuario ORDER BY id_usuario DESC;"
        mycursor.execute(sql)
        id_usuario1 = mycursor.fetchval()
        id_usuario1 = str(id_usuario1)

        mycursor.execute("insert into cuenta_bancaria values('"+username_info+"', '"+balance_inti+"', '"+fecha_alt+"', '"+id_usuario1+"', '"+id_cat_cuentas+"') ")

        mydb.commit()
        screen1.destroy()
        messagebox.showinfo('Registro',('Exitoso!'))

################## LOGIN VERIFY SCREEN #################################
def login_verify():
  global current_balance
  global username1
  global name_display
  global user_display_name
  global apep_display_name
  global apem_display_name
  global telf_display_name
  global ID_display
  global password1
  global mail

  username1 = username_verify.get()
  password1 = password_verify.get()
  username_entry1.delete(0, END)
  password_entry1.delete(0, END)

  mydb=pyodbc.connect(driver='{SQL Server}', server='10.10.58.33', database='Gangrena', trusted_Connection='yes')
  mycursor=mydb.cursor()
  mycursor.execute("use Gangrena")
  mycursor.execute("select accit from usuario")
  values=mycursor.fetchall()
  user_acc=[]
  for i in values:
    user_acc.append(i[0])

  if username1.isalpha():
        messagebox.showwarning('Atención',('Ingrese un numero de cuenta valido!'))
        username_entry1.delete(0, END)
        password_entry1.delete(0,END)

  if str(username1)=='':
        messagebox.showwarning('Atención',('Ingrese un numero de usuario!'))
        password_entry1.delete(0,END)
  elif str(username1).isspace():
        messagebox.showwarning('Antención',('Ingrese un numero de usuario!'))
        username_entry1.delete(0, END)
        password_entry1.delete(0,END)
  elif username1.isalnum():
      if username1.isdigit():

          if int(username1) in user_acc:

              mycursor.execute(f"SELECT pw FROM usuario WHERE accit={username1}")
              values=mycursor.fetchall()
              mydb.commit()
              user_pass=[]
              for i in values:
                  user_pass.append(i[0])

              user_pass_1=str(user_pass[0])

              if password1=='':
                  messagebox.showwarning('Alerta',('Ingrese una contraseña!'))
                  username_entry1.delete(0, END)
                  password_entry1.delete(0,END)
              elif password1 == str(user_pass_1) :
                  mycursor.execute(f"select nombre from usuario where accit={username1}")
                  values=mycursor.fetchall()
                  user_name=[]
                  for i in values:
                    user_name.append(i[0])
                  user_display_name=str(user_name[0])

                  mycursor.execute(f"select apellido_pa from usuario where accit={username1}")
                  values=mycursor.fetchall()
                  apep_name=[]
                  for i in values:
                    apep_name.append(i[0])
                  apep_display_name=str(apep_name[0])

                  mycursor.execute(f"select apellido_ma from usuario where accit={username1}")
                  values=mycursor.fetchall()
                  apem_name=[]
                  for i in values:
                    apem_name.append(i[0])
                  apem_display_name=str(apem_name[0])

                  mycursor.execute(f"select correo from usuario where accit={username1}")
                  values=mycursor.fetchall()
                  mail_name=[]
                  for i in values:
                    mail_name.append(i[0])
                  mail=str(mail_name[0])

                  mycursor.execute(f"select id_usuario from usuario where accit={username1}")
                  values=mycursor.fetchall()
                  apem_name=[]
                  for i in values:
                    apem_name.append(i[0])
                  ID_display=str(apem_name[0])


                  mycursor.execute(f"select telefono from usuario where accit={username1}")
                  values=mycursor.fetchall()
                  telf_name=[]
                  for i in values:
                    telf_name.append(i[0])
                  telf_display_name=str(telf_name[0])
                  mydb=pyodbc.connect(driver='{SQL Server}', server='10.10.58.33', database='Gangrena', trusted_Connection='yes')
                  mycursor=mydb.cursor()
                  mycursor.execute("use Gangrena")

                  mycursor.execute(f'select balance from usuario where accit={username1}')
                  values=mycursor.fetchall()
                  user_balance=[]
                  for i in values:
                    user_balance.append(i[0])
                  user_balance_1=float(user_balance[0])
                  current_balance=user_balance_1

                  screen2.destroy()
                  screen.destroy()
                  abcd()
              elif password1!= str(user_pass_1):
                  password_not_recognised()
          else:
              user_not_found()
      else:
          user_not_found()

  else:
        user_not_found()

################## REGISTER DISPLAY SCREEN #################################
def register():
  global screen1
  global password_entry
  global username_entry
  global tel_entry
  global apellP_entry
  global apellM_entry
  global correo_entry
  global rand
  screen1 = Toplevel(screen)
  screen1.title("Register")
  screen1.state('zoomed')
  screen1.configure(bg='#1e1e2d')
  screen1.iconphoto(False,tk.PhotoImage(file='imagenes/abc.png'))
  photo = PhotoImage(file="imagenes/login_person.png")
  img = photo.zoom(3)
  img = photo.subsample(2)
  label = Label(screen1,image=img,bg='#1e1e2d')
  label.image = img
  label.pack(pady=2)

  global username
  global password
  global name
  global telf
  global apellidoM
  global apellidoP
  global Correo
  global option_var

  global username_entry1
  global password_entry1
  global name_entry

  username = StringVar()
  password = StringVar()
  name     = StringVar()
  telf     = StringVar()
  apellidoP = StringVar()
  apellidoM = StringVar()
  Correo_info = StringVar()
  option_var = StringVar()

  Label(screen1, text = "Ingresa tu Nombre:",font = ("orbitron", 15),bg='#1e1e2d',fg='white').pack()
  name_entry = Entry(screen1,font = ("orbitron",18), textvariable = name,bg='white')
  name_entry.pack()

  Label(screen1, text = "Tu numero de cuenta es:",font = ("orbitron", 15),bg='#1e1e2d',fg='white').pack()
  rand=random.randint(1,100000)
  username=Label(screen1, text = rand,font = ("orbitron", 15),bg='yellow').pack()

  Label(screen1, text = "ingresa tu Apellido Paterno",font = ("orbitron", 15),bg='#1e1e2d',fg='white').pack()
  apellP_entry =  Entry(screen1,font = ("orbitron",18), textvariable = apellidoP,bg='white')
  apellP_entry.config(fg='black')
  apellP_entry.pack()

  Label(screen1, text = "Ingresa tu Apellido Materno",font = ("orbitron", 15),bg='#1e1e2d',fg='white').pack()
  apellM_entry =  Entry(screen1,font = ("orbitron",18), textvariable = apellidoM,bg='white')
  apellM_entry.config(fg='black')
  apellM_entry.pack()
  Label(screen1, text = "",bg='#1e1e2d').pack()
  def generar():
        button1['state'] = tk.DISABLED
        Label(screen1, text = "Tu correo es:",bg='lightblue',font = ("orbitron", 10)).pack()
        Correo_info= (name.get()[0]+apellidoP.get()[0:3]+apellidoM.get()+"@hola.com").lower()
        Label(screen1, text = Correo_info,bg='#1e1e2d',fg='white',font = ("orbitron", 10)).pack()
  
  button1= tk.Button(screen1,text = "Generar correo",fg='#663259', bg = "#c2d5e3", width = "21", height = "2", font = ("orbitron", 12,'bold'),command=generar)
  button1.pack()

  Label(screen1, text = "Ingresa tu Telefono",font = ("orbitron", 15),bg='#1e1e2d',fg='white').pack()
  tel_entry =  Entry(screen1,font = ("orbitron",18), textvariable = telf,bg='white')
  tel_entry.config(fg='black')
  tel_entry.pack()

  Label(screen1, text = "Ingresa tu Contraseña",font = ("orbitron", 15),bg='#1e1e2d',fg='white').pack()
  password_entry =  Entry(screen1,font = ("orbitron",18), textvariable = password,bg='white')
  password_entry.config(fg='black',show='●')
  password_entry.pack()

  languages = ('Gerente', 'Supervisor', 'Cajero')
  label = Label(screen1,  text='Seleciona tu Posición', font= ("orbitron", 15), bg='#1e1e2d',fg='white').pack()

    # option menu
  option_menu = ttk.OptionMenu(screen1, option_var,languages[0],*languages).pack()
  Button(screen1,text = "REGISTRARSE",fg='white', bg = "#663259", width = "21", height = "2", font = ("orbitron", 12,'bold'),command=register_user).pack(pady=5)
  if option_var =="Gerente":
     option_var = int("1")
  elif option_var =="Supervisor":
        option_var = int("2")
  elif option_var =="Cajero":
        option_var = int("3")
  else:
            print("Incorrecto")
################## LOGIN DISPLAY SCREEN #################################
def login():
  global screen2
  screen2 = Toplevel(screen)
  screen2.title("Login")
  screen2.state('zoomed')
  screen2.configure(bg='#1e1e2d')
  screen2.iconphoto(False,tk.PhotoImage(file='imagenes/abc.png'))

  photo = PhotoImage(file="imagenes/login_person.png")
  label = Label(screen2,image=photo,bg='#1e1e2d')
  label.image = photo
  label.pack(pady=5)

  Label(screen2, text = "Por favor ingresa tus datos para iniciar sesión",bg='#1e1e2d',fg='white',font = ("orbitron", 25,'bold')).pack()
  Label(screen2, text = "",bg='#1e1e2d').pack()

  global username_verify
  global password_verify
  username_verify = StringVar()
  password_verify = StringVar()
  global username_entry1
  global password_entry1

  Label(screen2, text = "Numero de cuenta",fg='white',bg='#1e1e2d',font = ("orbitron", 15)).pack()
  Label(screen2, text = "",bg='#1e1e2d').pack()
  username_entry1 = Entry(screen2,font = ("orbitron",15) ,textvariable = username_verify,bg='#392f28',fg='white')
  username_entry1.pack()

  Label(screen2, text = "",bg='#1e1e2d').pack()
  Label(screen2, text = "Contraseña",fg='white',bg='#1e1e2d',font = ("orbitron", 15)).pack()
  Label(screen2, text = "",bg='#1e1e2d').pack()
  password_entry1 = Entry(screen2,font = ("orbitron",15), textvariable = password_verify,bg='#392f28')
  password_entry1.config(fg='black',show='●')
  password_entry1.pack()
  Label(screen2, text = "",bg='#1e1e2d').pack()
  Button(screen2,text = "INICIAR SESIÓN",fg='white', bg = "#663259", width = "22", height = "2", font = ("orbitron", 12,'bold'),command=login_verify).pack(pady=5)

  def transfer_verify():
    global new_balance
    username2 = transferencia.get()
    mydb=pyodbc.connect(driver='{SQL Server}', server='10.10.58.33', database='Gangrena', trusted_Connection='yes')
    mycursor=mydb.cursor()
    mycursor.execute("use Gangrena")
    mycursor.execute(f'select balance from usuario where accit={username2}')
    values=mycursor.fetchall()
    new_balance=[]
    for i in values:
        new_balance.append(i[0])
    new_balance_1=float(new_balance[0])
    new_balance=new_balance_1

################## REGISTER/LOGIN SCREEN #################################
def main_screen():
  global screen
  screen = Tk()
  screen.state('zoomed')
  screen.title("BANCO AMIGOS")
  screen.configure(bg='#1e1e2d')
  screen.iconphoto(False,tk.PhotoImage(file="imagenes/abc.png"))
  Label(text = "", width = "300",bg='#1e1e2d').pack()
  img = ImageTk.PhotoImage(Image.open("imagenes/bancoamigos.png"))
  panel = Label(screen, image = img,bg='#1e1e2d',width = "550", height = "350")
  panel.pack()
  Label(text = "",bg='#1e1e2d').pack()
  Button(text = "INGRESAR",fg='#663259', bg = "#c2d5e3", width = "21", height = "2", font = ("orbitron", 12,'bold'),command=login).pack(pady=5)
  Label(text = "",bg='#1e1e2d').pack()
  Button(text = "REGISTRARSE",fg='white', bg = "#663259", width = "21", height = "2", font = ("orbitron", 12,'bold'),command=register).pack(pady=5)
  Label(text = "",bg='#1e1e2d').pack()
  screen.mainloop()
main_screen()