from tkinter import ttk # Normal Tkinter.* widgets are not themed!
from Messages.message_types import SESSION_DATA
from components.header import Header
import tkinter as tk
from core.readings import Readings
from Messages.Session import Session
from util.dictionary import arabic
from core.session_core import SessionCore
from tkinter import messagebox


class ResultPage(tk.Frame):
    def __init__(self,parent, controller):
        tk.Frame.__init__(self, parent,bg="#fff")
        self.controller = controller
        self.client_socket = controller.client_socket

    def handle_txt(self,value):
        if value =='import':
            return arabic("استيراد")
        elif value == 'export':
            return arabic("تصدير")
        elif value == 'import_export':
            return arabic("استيراد/تصدير")
        elif value == 'south_port':
            return arabic("الميناء الجنوبي")
        elif value == 'main_port':
            return arabic('الميناء الرئيسي')
        elif value == 'camera':
            return arabic('كاميرا')

    def send_session(self):
        session_data = Session()
        session_data.set_type(SESSION_DATA)
        session_data.set_session_data(SessionCore.get_session())
        self.client_socket.send_msg(session_data.json())
        self.controller.show_frame("ticketStatusMonitoring")
        # messagebox.showinfo("information", "Information")

    def render(self,controller):
        Header.render(self)
        tn_lbl = tk.Label(self, text=arabic("رقم الشاحنة"),font=self.controller.title_font,bg="#fff")
        tn_lbl.grid(column=2, row=1)
        tn_txt= tk.Label(self, text=SessionCore.get_tn()[0]['value'], font=self.controller.title_font, justify="right",bg="#fff")
        tn_txt.grid(column=1, row=1,sticky='e')
        ##################################################################################################
        trn_lbl = tk.Label(self, text=arabic("رقم المقطورة"),font=self.controller.title_font, justify="right",bg="#fff")
        trn_lbl.grid(column=2, row=2)
        trn_txt=tk.Label(self, text=SessionCore.get_trn()[0]['value'], font=self.controller.title_font, justify="right",bg="#fff")
        trn_txt.grid(column=1,row=2,sticky='e')
        ###################################################################################################
        nn_lbl = tk.Label(self, text=arabic("الرقم الوطني"), font=self.controller.title_font, justify="right",bg="#fff")
        nn_lbl.grid(column=2, row=3)
        nn_txt=tk.Label(self, text=SessionCore.get_nn()[0]['value'], font=self.controller.title_font, justify="right",bg="#fff")
        nn_txt.grid(column=1,row=3,sticky='e')
        ##########
        button = ttk.Button(self,width=10 ,text=arabic("تقديم"),command=self.send_session)
        button.grid(column=0, row=7,columnspan=2)
        button = ttk.Button(self,width=10, text=arabic("رجوع"), command=lambda: self.controller.show_frame("TruckReception"))
        button.grid(column=1, row=7)
        #######################################################


