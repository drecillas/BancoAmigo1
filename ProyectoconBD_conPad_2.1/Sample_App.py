
from tkinter import *
from tkinter import BOTH, END, LEFT
import tkinter as tk
from tkinter import scrolledtext as st
from Desarrolladores_info import About_Info
from Menu_Page import MenuPage
from Info_page import InfoPage
from Start_Page import StartPage
from Estado_cuenta import TablaPage
from Register_Screen import register
from Transfer_page import TransferPage
from Retiro_Page import WithdrawPage
from Deposite_Page import DepositPage
import var

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

        for F in (StartPage, MenuPage, TransferPage, TablaPage, WithdrawPage, DepositPage, InfoPage, About_Info):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()
