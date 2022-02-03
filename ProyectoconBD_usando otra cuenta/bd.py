import var
import pyodbc
import random
from tkinter import BOTH, END, LEFT
class conectar:
     global conexion
     conexion = pyodbc.connect(driver='{SQL Server}',server='10.10.58.33',database='Gangrena',trusted_connection='yes')
     cursor = conexion.cursor()
     def login_bd():
         cursor = conexion.cursor()
         cursor.execute("select accit from usuario")
         values=cursor.fetchall()
         var.user_acc=[]
         for i in values:
           var.user_acc.append(i[0])


     def login_contraBD():
         cursor = conexion.cursor()
         cursor.execute(f"SELECT pw FROM usuario WHERE accit={var.username1}")
         values = cursor.fetchall()
         user_pass=[]
         for i in values:
                  user_pass.append(i[0])
                  var.user_pass_1=str(user_pass[0])

     def login_comprobacionBD():
         cursor = conexion.cursor()
         cursor.execute(f"select nombre from usuario where accit={var.username1}")
         values=cursor.fetchall()
         user_name=[]
         for i in values:
            user_name.append(i[0])
            var.user_display_name=str(user_name[0])
         cursor.execute(f"select apellido_pa from usuario where accit={var.username1}")
         values=cursor.fetchall()
         apep_name=[]
         for i in values:
            apep_name.append(i[0])
            var.apep_display_name=str(apep_name[0])
         cursor.execute(f"select apellido_ma from usuario where accit={var.username1}")
         values=cursor.fetchall()
         apem_name=[]
         for i in values:
             apem_name.append(i[0])
             var.apem_display_name=str(apem_name[0])
         cursor.execute(f"select correo from usuario where accit={var.username1}")
         values=cursor.fetchall()
         mail_name=[]
         for i in values:
             mail_name.append(i[0])
             var.mail=str(mail_name[0])
         cursor.execute(f"select id_usuario from usuario where accit={var.username1}")
         values=cursor.fetchall()
         apem_name=[]
         for i in values:
             apem_name.append(i[0])
             var.ID_display=str(apem_name[0])
         cursor.execute(f"select telefono from usuario where accit={var.username1}")
         values=cursor.fetchall()
         telf_name=[]
         for i in values:
             telf_name.append(i[0])
             var.telf_display_name=str(telf_name[0])
         cursor.execute(f'select balance from usuario where accit={var.username1}')
         values=cursor.fetchall()
         user_balance=[]
         for i in values:
             user_balance.append(i[0])
             user_balance_1=float(user_balance[0])
             var.current_balance=user_balance_1


     def registro_bd():
         cursor = conexion.cursor()
         cursor.execute('select accit from usuario')
         values=cursor.fetchall()
         cursor.execute('select telefono from usuario')
         values_tel=cursor.fetchall()
         b=[]
         for i in values:
             b.append(i[0])
             var.b = b
         a=[]
         for j in values_tel:
             a.append(j[0])
             var.a = a


     def regis_bd_puesto():
         cursor = conexion.cursor()
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
         balance_inti = var.option_var.get()
         if balance_inti  =="Gerente":
            sql="select salario from cat_salario_puesto where id_cat_salario_puesto =1"
            cursor.execute(sql)
            balance_inti  = cursor.fetchval()
            balance_inti = str(balance_inti)
         elif balance_inti  =="Supervisor":
            sql="select salario from cat_salario_puesto where id_cat_salario_puesto =2"
            cursor.execute(sql)
            balance_inti  = cursor.fetchval()
            balance_inti = str(balance_inti)
         elif balance_inti  =="Cajero":
            sql="select salario from cat_salario_puesto where id_cat_salario_puesto =3"
            cursor.execute(sql)
            balance_inti  = cursor.fetchval()
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
         cursor.execute(sql)
         fecha_alt = cursor.fetchval()
         fecha_alt = str(fecha_alt)
         cursor.execute("insert into usuario values('"+name_info+"', '"+apellidoP_info+"', '"+apellidoM_info+"', '"+telf_info+"', '"+Correo_info+"', '"+password_info+"', '"+poss_info+"', '"+balance_inti+"','"+username_info+"')")
         sql = "SELECT TOP 1 id_usuario FROM usuario ORDER BY id_usuario DESC;"
         cursor.execute(sql)
         id_usuario1 = cursor.fetchval()
         id_usuario1 = str(id_usuario1)
         cursor.execute("insert into cuenta_bancaria values('"+username_info+"', '"+balance_inti+"', '"+fecha_alt+"', '"+id_usuario1+"', '"+id_cat_cuentas+"') ")
         conexion.commit()


     def retiro_user():
         cursor = conexion.cursor()
         curr2= var.curr2
         curr = str(var.current_balance)
         cursor.execute(f"update usuario set balance ={var.current_balance} where accit = {var.username1} ")
         sql = "select SYSDATETIME ()"
         cursor.execute(sql)
         fecha_alt = cursor.fetchval()
         fecha_alt = str(fecha_alt)
         sql="select id_cat_operaciones from cat_operaciones where id_cat_operaciones = 2"
         cursor.execute(sql)
         operaciones = cursor.fetchval()
         operaciones = str(operaciones)
         rand=random.randint(1,100000)
         rand = str(rand)
         cursor.execute(f"SELECT  id_cuenta_banc FROM cuenta_bancaria WHERE id_usuario = {var.ID_display}")
         id_cuenta_ban = cursor.fetchval()
         id_cuenta_ban = str(id_cuenta_ban)
         cursor.execute("INSERT INTO estado_cuenta values ('"+rand+"', '"+fecha_alt+"', '"+curr2+"', '"+id_cuenta_ban+"', '"+operaciones+"')")
         conexion.commit()


     def other_amount():
        cursor = conexion.cursor()
        curr2 = var.curr2
        curr = str(var.current_balance)
        cursor.execute(f"update usuario set balance ={var.current_balance} where accit = {var.username1} ")
        sql = "select SYSDATETIME ()"
        cursor.execute(sql)
        fecha_alt = cursor.fetchval()
        fecha_alt = str(fecha_alt)
        sql="select id_cat_operaciones from cat_operaciones where id_cat_operaciones = 2"
        cursor.execute(sql)
        operaciones = cursor.fetchval()
        operaciones = str(operaciones)
        rand=random.randint(1,100000)
        rand = str(rand)
        cursor.execute(f"SELECT  id_cuenta_banc FROM cuenta_bancaria WHERE id_usuario = {var.ID_display}")
        id_cuenta_ban = cursor.fetchval()
        id_cuenta_ban = str(id_cuenta_ban)
        cursor.execute("INSERT INTO estado_cuenta values ('"+rand+"', '"+fecha_alt+"', '"+curr2+"', '"+id_cuenta_ban+"', '"+operaciones+"')")
        conexion.commit()


     def deposito_bd():
         cursor = conexion.cursor()
         curr2 = var.curr2
         curr = str(var.current_balance)
         cursor.execute(f"update usuario set balance ={var.current_balance} where accit = {var.username1} ")
         sql = "select SYSDATETIME ()"
         cursor.execute(sql)
         fecha_alt = cursor.fetchval()
         fecha_alt = str(fecha_alt)
         sql="select id_cat_operaciones from cat_operaciones where id_cat_operaciones = 3"
         cursor.execute(sql)
         operaciones = cursor.fetchval()
         operaciones = str(operaciones)
         rand=random.randint(1,100000)
         rand = str(rand)
         cursor.execute(f"SELECT  id_cuenta_banc FROM cuenta_bancaria WHERE id_usuario = {var.ID_display}")
         id_cuenta_ban = cursor.fetchval()
         id_cuenta_ban = str(id_cuenta_ban)
         cursor.execute("INSERT INTO estado_cuenta values ('"+rand+"', '"+fecha_alt+"', '"+curr2+"', '"+id_cuenta_ban+"', '"+operaciones+"')")
         conexion.commit()


     def transferencia_bd():
        cursor = conexion.cursor()
        curr2 = var.curr2
        cursor.execute(f"update usuario set balance ={var.current_balance} where accit = {var.username1} ")             
        sql = "select SYSDATETIME ()"
        cursor.execute(sql)
        fecha_alt = cursor.fetchval()
        fecha_alt = str(fecha_alt)
        sql="select id_cat_operaciones from cat_operaciones where id_cat_operaciones = 1"
        cursor.execute(sql)
        operaciones = cursor.fetchval()
        operaciones = str(operaciones)
        sl="select id_cat_operaciones from cat_operaciones where id_cat_operaciones=4"
        cursor.execute(sl)
        concep=cursor.fetchval()
        concep = str(concep)
        rand=random.randint(1,100000)
        rand = str(rand)
        cursor.execute(f"SELECT  id_cuenta_banc FROM cuenta_bancaria WHERE id_usuario = {var.ID_display}")
        id_cuenta_ban = cursor.fetchval()
        id_cuenta_ban = str(id_cuenta_ban)
        username2 = var.transferencia
        cursor.execute(f"select id_usuario from usuario where accit = {username2}")
        con = cursor.fetchval()
        con = str(con)
        cursor.execute(f"SELECT  id_cuenta_banc FROM cuenta_bancaria WHERE id_usuario = {con}")
        concepto = cursor.fetchval()
        concepto = str(concepto)
        cursor.execute("INSERT INTO estado_cuenta values ('"+rand+"', '"+fecha_alt+"', '"+curr2+"', '"+id_cuenta_ban+"', '"+operaciones+"')")
        cursor.execute("INSERT INTO estado_cuenta values ('"+rand+"', '"+fecha_alt+"', '"+curr2+"', '"+concepto+"', '"+concep+"')")

        otrosaldo = var.current_balance
        cursor.execute(f'select balance from usuario where accit={username2}')
        values=cursor.fetchall()
        cursor.execute(f"update usuario set balance ={otrosaldo} where accit = {username2} ")
        conexion.commit()
     

     def estado_bd():
         cursor = conexion.cursor()
         cursor.execute(f'select es.folio_est_cuenta as folio, es.fecha_est_cuenta as fecha, es.saldo_ope_total as saldo, nom_operaciones as operacion from estado_cuenta es INNER JOIN cuenta_bancaria cb on es.id_cuenta_banc = cb.id_cuenta_banc INNER JOIN usuario u on cb.id_usuario = u.id_usuario INNER JOIN cat_operaciones co on co.id_cat_operaciones = es.id_cat_operaciones where accit= {var.username1} Order by fecha desc;')
         return cursor.fetchall()
         conexion.close()