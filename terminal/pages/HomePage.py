from tkinter import ttk, PhotoImage  # Normal Tkinter.* widgets are not themed!

from Messages.ConfigMessage import ConfigMessage
from Messages.Session import Session
from Messages.message_types import SESSION_REQUEST
from components.header import Header
import tkinter as tk

class HomePage(tk.Frame):
    def __init__(self ,parent, controller):
        tk.Frame.__init__(self, parent,bg='#fff')
        self.controller = controller
        self.client_socket = controller.client_socket
        # self.render()

    def page_redirection(self,event=None):
        request_message = Session()
        request_message.set_type(SESSION_REQUEST)
        self.client_socket.send_msg(request_message.json())
        self.controller.show_frame("TruckReception")

    def render(self,controller):
        Header.render(self)
        login_btn = PhotoImage(file='assets/truck_reciption.png')
        img_label = tk.Label(self, image=login_btn)
        img_label.image = login_btn
        my_button = tk.Button(self, image=login_btn, command=self.page_redirection, borderwidth=0)
        my_button.grid(column=2, row=4, sticky='e')

