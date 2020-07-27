
from components.header import Header
import tkinter as tk
from tkinter import ttk, PhotoImage  # Normal Tkinter.* widgets are not themed!
from core.session_core import SessionCore


class ticketStatusMonitoring(ttk.Frame):

    self =None
    def __init__(self, parent,controller):
        self.controller = controller
        tk.Frame.__init__(self, parent, bg="#fff")
        ticketStatusMonitoring.self = self
    def render(self,controller):
            Header.render(self)
            if SessionCore.get_session()['ticket_id'] and SessionCore.get_session()['ticket_id'] != '' and SessionCore.get_session()['ticket_id'] != None:
                loadingImg = PhotoImage(file='assets/loading.png')
                loading_img_label = tk.Label(self, image=loadingImg, bg="#fff")
                loading_img_label.image = loadingImg
                loading_img_label.grid(column=1, row=3, sticky='e', padx='10')

    @staticmethod
    def refresh():
        ticketStatusMonitoring.render(ticketStatusMonitoring.self,None)

