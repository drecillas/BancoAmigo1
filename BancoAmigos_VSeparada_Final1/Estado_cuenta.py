
from tkinter import *
from tkinter import BOTH, END, LEFT
import tkinter as tk
from tkinter import ttk 
import pyodbc
from tkinter import scrolledtext as st
import var

class TablaPage(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='#1e1e2d')
        self.controller = controller
        self.controller.title('BANCO AMIGOS')
        self.controller.state('zoomed')
        heading=tk.Label(self,text='ESTADO DE CUENTA',font=('Lucida Console',45,'bold'),foreground='white',background='#1e1e2d')
        heading.pack(pady=25)
        upperframe=tk.Frame(self,bg='#1e1e2d')
        upperframe.pack(fill='both',expand='True')
        name_info =tk.Label(upperframe, text= f'{var.user_display_name} {var.apep_display_name} {var.apem_display_name}',font=('Lucida Console',20,'bold'),fg='yellow',bg='#1e1e2d').pack(pady=5)
        button_frame=tk.Frame(self,bg='#1e1e2d')
        button_frame.pack(fill='x',expand='True')
        
        estiloTabla = ttk.Style()
        estiloTabla.configure("Treeview", font = ("Lucida Console", 10, 'bold'), foreground = 'white', background = "#1e1e2d")
        estiloTabla.map('Treeview',background=[('selected', 'DarkOrchid1')], foreground=[('selected','black')] )
        estiloTabla.configure('Heading',background = 'white', foreground='navy', padding=(2,8), font= ('Lucida Console', 12, 'bold'))

        tabla=ttk.Treeview(upperframe,height=18,columns=("#1", "#2", "#3","#4"),selectmode="extended",show="headings")
        tabla.heading("#1",text="FOLIO",anchor=CENTER)
        tabla.heading("#2",text="FECHA",anchor=CENTER)
        tabla.heading("#3",text="SALDO",anchor=CENTER)
        tabla.heading("#4",text="OPERACION",anchor=CENTER)
        tabla.column("#4", minwidth=0, width=220)

        tabla.pack()
       
        def recuperar_todos():
            mydb=pyodbc.connect(driver='{SQL Server}', 
                                server='10.10.58.33', 
                                database='Gangrena', 
                                trusted_Connection='yes')
            mycursor=mydb.cursor()
            mycursor.execute("use Gangrena")
            mycursor.execute(f'select es.folio_est_cuenta as folio, es.fecha_est_cuenta as fecha, es.saldo_ope_total as saldo, nom_operaciones as operacion from estado_cuenta es INNER JOIN cuenta_bancaria cb on es.id_cuenta_banc = cb.id_cuenta_banc INNER JOIN usuario u on cb.id_usuario = u.id_usuario INNER JOIN cat_operaciones co on co.id_cat_operaciones = es.id_cat_operaciones where accit= {var.username1} Order by fecha desc;')
            return mycursor.fetchall()

        def listar():
            respuestas=recuperar_todos()
            for (folio,fecha,saldo,operacion) in respuestas:
                    tabla.insert('','end',values=(folio,fecha,'$'+(str(saldo)),operacion))
        listar()
        button_frame=tk.Label(self,bg='#1e1e2d')
        button_frame.pack(side='left',expand='True')
        
        def quit():
            controller.show_frame('MenuPage')
        def delete():
            for item in tabla.get_children():
                tabla.delete(item)
        actualizar_button=tk.Button(button_frame,text='Actualizar',command=lambda:[delete(),listar()],font=('Lucida Console',13),relief=RIDGE,borderwidth=3,width=20,height=2)
        actualizar_button.grid(row=5,column=0)
        exit_button=tk.Button(button_frame,text='Regresar al Menu',command=lambda:[quit(),delete()],font=('Lucida Console',13),relief=RIDGE,borderwidth=3,width=20,height=2)
        exit_button.grid(row=4,column=0)
