from tkinter import ttk, PhotoImage
import tkinter as tk

from core.heart_beat import HeartBeat


class Header(ttk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        self.controller = controller
        self.render()

    def changeSocketStatus(self,value):
        print("changeSocketStatus")

    def render(self):
        myImage = PhotoImage(file='assets/header.png')
        label = tk.Label(self, image=myImage,width='950',bg='#fff')
        label.image = myImage  # keep a reference!
        label.grid(row=0,column=0,columnspan=3)
        socket_status=HeartBeat.get_socket_status()
        if socket_status:
            connect_btn_img = PhotoImage(file='assets/green_circle.png')
            connect_btn_img_label = tk.Label(self, image=connect_btn_img,bg="#fff")
            connect_btn_img_label.image = connect_btn_img
            connect_btn = tk.Button(self, image=connect_btn_img, borderwidth=0,bg="#fff",highlightthickness='0')
            connect_btn.bind("<1>", lambda event: self.changeSocketStatus("0"))
            connect_btn.grid(column=3, row=0)
        else:
            connect_btn_img = PhotoImage(file='assets/red_circle.png')
            connect_btn_img_label = tk.Label(self, image=connect_btn_img, bg="#fff")
            connect_btn_img_label.image = connect_btn_img
            connect_btn = tk.Button(self, image=connect_btn_img, borderwidth=0, bg="#fff", highlightthickness='0')
            connect_btn.bind("<1>", lambda event: self.changeSocketStatus("0"))
            connect_btn.grid(column=3, row=0)