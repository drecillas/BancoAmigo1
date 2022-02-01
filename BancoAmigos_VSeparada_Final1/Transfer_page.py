
from tkinter import *
from tkinter import messagebox
from tkinter import BOTH, END, LEFT
import tkinter as tk
import random
import pyodbc
from tkinter import scrolledtext as st
import var

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
                    val=int(deposito.get())
                    saldocliente=var.current_balance
                    if int(deposito.get())>var.current_balance:
                        messagebox.showwarning('ATENCIÓN','SALDO INSUFICIENTE!')
                        deposito_entry.delete(0,END)
                    elif int(deposito.get())<0:
                        messagebox.showwarning('ATENCIÓN','INGRESA UNA CANTIDAD CORRECTA!')
                        deposito_entry.delete(0,END)
                    else:
                        var.current_balance -= int(deposito.get())
                        curr2=str(val)
                        controller.shared_data['Balance'].set(var.current_balance)
                        messagebox.askquestion('Confirmación','¿Estas seguro que deseas realizar la transferencia?')
                        mydb=pyodbc.connect(driver='{SQL Server}', server='10.10.58.33', database='Gangrena', trusted_Connection='yes')
                        mycursor=mydb.cursor()
                        mycursor.execute("use Gangrena")
                        mycursor.execute(f"update usuario set balance ={var.current_balance} where accit = {var.username1} ")
                        
                        sql = "select SYSDATETIME ()"
                        mycursor.execute(sql)
                        fecha_alt = mycursor.fetchval()
                        fecha_alt = str(fecha_alt)
        
                        sql="select id_cat_operaciones from cat_operaciones where id_cat_operaciones = 1"
                        mycursor.execute(sql)
                        operaciones = mycursor.fetchval()
                        operaciones = str(operaciones)
                        sl="select id_cat_operaciones from cat_operaciones where id_cat_operaciones=4"
                        mycursor.execute(sl)
                        concep=mycursor.fetchval()
                        concep = str(concep)
                        rand=random.randint(1,100000)
                        rand = str(rand)
                        mycursor.execute(f"SELECT  id_cuenta_banc FROM cuenta_bancaria WHERE id_usuario = {var.ID_display}")
                        id_cuenta_ban = mycursor.fetchval()
                        id_cuenta_ban = str(id_cuenta_ban)
                        username2 = transferencia.get()

                        mycursor.execute(f"select id_usuario from usuario where accit = {username2}")
                        con = mycursor.fetchval()
                        con = str(con)
                        mycursor.execute(f"SELECT  id_cuenta_banc FROM cuenta_bancaria WHERE id_usuario = {con}")
                        concepto = mycursor.fetchval()
                        concepto = str(concepto)

                        mycursor.execute("INSERT INTO estado_cuenta values ('"+rand+"', '"+fecha_alt+"', '"+curr2+"', '"+id_cuenta_ban+"', '"+operaciones+"')")
                        mycursor.execute("INSERT INTO estado_cuenta values ('"+rand+"', '"+fecha_alt+"', '"+curr2+"', '"+concepto+"', '"+concep+"')")
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
                    otrosaldo=float(new_balance[0])
                
                    otrosaldo += int(deposito.get())
                    messagebox.showinfo('TRANSFERENCIA','Transferencia exitosa!')
                    username2 = transferencia.get()
                    mydb=pyodbc.connect(driver='{SQL Server}', server='10.10.58.33', database='Gangrena', trusted_Connection='yes')
                    mycursor=mydb.cursor()
                    mycursor.execute("use Gangrena")
                    mycursor.execute(f"update usuario set balance ={otrosaldo} where accit = {username2} ")
                    mydb.commit()
                    deposito_entry.delete(0,END)
                    transferencia_entry.delete(0,END)
                    
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
        
