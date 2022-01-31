
from tkinter import *
from tkinter import messagebox
from tkinter import BOTH, END, LEFT
import random
import pyodbc
from tkinter import scrolledtext as st
import var

def register_user():
    
  global username_info
  rand=random.randint(1,100000)
  rand = str(rand)
  username_info = str(rand)
  password_info = var.password.get()
  name_info     = var.name.get().upper()
  telf_info     = var.telf.get()
  apellidoP_info= var.apellidoP.get().upper()
  apellidoM_info= var.apellidoM.get().upper()
  Correo_info  = Correo_info= (var.name.get()[0]+var.apellidoP.get()[0:3]+var.apellidoM.get()+"@hola.com").lower()
  var.option_var.get()
  poss_info     = var.option_var.get()
  if poss_info  =="Gerente":
     poss_info  = "1"
  elif poss_info  =="Supervisor":
        poss_info  = "2"
  elif poss_info  =="Cajero":   
        poss_info = "3"
  else:
            print("Incorrecto")
  
  ################## SQL DATABASE ##################
  global label_may
  global label_con
  global mycursor
  mydb=pyodbc.connect(driver='{SQL Server}', server='10.10.58.33', database='Gangrena', trusted_Connection='yes')
  mycursor=mydb.cursor()
  mycursor.execute("use Gangrena")
  mydb.commit()

  mycursor.execute('select accit from usuario')
  values=mycursor.fetchall()

  mycursor.execute('select telefono from usuario')
  values_tel=mycursor.fetchall()

  b=[]
  for i in values:
      b.append(i[0])

  a=[]
  for j in values_tel:
      a.append(j[0])

  if username_info in b:
    label = Label(var.screen1, text = "El Usuario ingresado ya existe  ",bg='#1e1e2d', fg='orange',font = ("Lucida Console", 11,'bold'))
    label.place(x= 720, y=520)
    var.name_entry.delete(0,END)

  elif telf_info in a:
    label = Label(var.screen1, text = "El telefono ingresado ya existe",bg='#1e1e2d', fg='orange',font = ("Lucida Console", 11,'bold'))
    label.place(x= 720, y=520)
    var.tel_entry.delete(0,END)

  elif name_info=='' :
        label = Label(var.screen1, text = "Ingresa un nombre",bg='#1e1e2d', fg='orange',font = ("Lucida Console", 11,'bold'))
        label.place(x= 720, y=520)
        var.password_entry.delete(0,END)

  elif password_info=='' or len(password_info)<=8 :
        label_con = Label(var.screen1, text = "Ingresa una Contraseña valida            ",bg='#1e1e2d', fg='orange',font = ("Lucida Console", 11,'bold'))
        label_con.place(x= 720, y=520)
        var.password_entry.delete(0,END)

  elif re.search('[0-9]',password_info) is None:
        label_num = Label(var.screen1, text = "Contraseña con por lo menos un numero    ",bg='#1e1e2d', fg='orange',font = ("Lucida Console", 11,'bold'))
        label_num.place(x= 720, y=520)
        var.password_entry.delete(0,END)

  elif re.search('[A-Z]',password_info) is None:
 
        label_may = Label(var.screen1, text = "Contraseña con minimo una letra mayuscula",bg='#1e1e2d', fg='orange',font = ("Lucida Console", 11,'bold'))
        label_may.place(x= 720, y=520)
        var.password_entry.delete(0,END)

  elif telf_info=='' or len(telf_info) != 10 :
        label = Label(var.screen1, text = "Numero de telefono invalido       ",bg='#1e1e2d', fg='orange',font = ("Lucida Console", 11,'bold'))
        label.place(x= 720, y=520)
        var.password_entry.delete(0,END)
        var.tel_entry.delete(0,END)

  elif apellidoP_info=='' :
        label = Label(var.screen1, text = "Ingresa apellido paterno          ",bg='#1e1e2d', fg='orange',font = ("Lucida Console", 11,'bold'))
        label.place(x= 720, y=520)
        var.password_entry.delete(0,END)

  elif apellidoM_info=='' :
        label = Label(var.screen1, text = "Ingresa apellido materno          ",bg='#1e1e2d', fg='orange',font = ("Lucida Console", 11,'bold'))
        label.place(x= 720, y=520)
        var.password_entry.delete(0,END)

  else:       
        balance_inti = var.option_var.get()
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
        var.password_entry.delete(0, END)
        var.name_entry.delete(0, END)
        var.apellM_entry.delete(0,END)
        var.apellP_entry.delete(0, END)
        var.tel_entry.delete(0, END) 
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
        messagebox.showinfo('Registro',('Exitoso!'))
