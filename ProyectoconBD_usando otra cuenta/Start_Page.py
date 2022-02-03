from tkinter import *
from tkinter import messagebox
from tkinter import BOTH, END, LEFT
import time
import tkinter as tk
from tkinter import scrolledtext as st
import var
#from Main import main_screen


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='#1e1e2d')
        self.controller = controller
        self.controller.title('BANCO AMIGOS')
        self.controller.state('zoomed')
        self.controller.iconphoto(False,tk.PhotoImage(file='imagenes/abc.png'))
        space_label=tk.Label(self,height=6,bg='#1e1e2d').pack()
        heading=tk.Label(self,text='Banco Amigos',font=('Lucida Console',45,'bold'),foreground='white',background='#1e1e2d')
        heading.pack(pady=25)
        bien= tk.Label(self, text=f'BIENVENIDO',font=('Lucida Console',25),bg='#1e1e2d',fg='white').pack(pady=10)
        Name=tk.Label(self,text=f'{var.user_display_name} {var.apep_display_name} {var.apem_display_name}',font=('orbitron',20,'bold'),foreground='yellow',background='#1e1e2d').pack(pady=10)
        def next_page():
            controller.show_frame('MenuPage')

        entry_button = tk.Button(self,text='ACCEDER',fg='#663259', bg = "#c2d5e3", width = "24", height = "3",font=("Lucida Console", 12,'bold'),command=next_page,relief='raised').pack(pady=10)

        def Quit():
            self.controller.destroy()

        def popup():
            response=messagebox.askyesno('Salir','Seguro que deseas salir?')

            if response == 1:
                return Quit()
            else:
                return

        quit1 = tk.Button(self,text='SALIR',fg='white', bg = "#663259", width = "24", height = "3",font=("Lucida Console", 12,'bold'),command=popup,relief='raised').pack(pady=10)

        dualtone_label=tk.Label(self, text='',font=('Lucida Console',13),fg='white',bg='#1e1e2d',anchor='n')
        dualtone_label.pack(fill='both',expand='True')

        def changescreen():
            
            self.controller.destroy()
            import Main
            Main.main_screen()

        def popup2():
            response=messagebox.askyesno('Salir','Quieres usar otra cuenta?')

            if response == 1:
                return changescreen()
            else:
                return

        register_login_screen = tk.Button(dualtone_label,text='Usar otra cuenta',fg='white', bg = "#663259",font=("Lucida Console", 12,'bold'),command=popup2,relief='raised',borderwidth=3,width=23,height=3).pack(pady=10,padx=10,side='bottom',anchor='e')

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

        time_label=tk.Label(bottom_frame,font=('Lucida Console',12))
        time_label.pack(side='right')
        tick()

