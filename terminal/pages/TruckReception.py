
from tkinter import ttk, PhotoImage  # Normal Tkinter.* widgets are not themed!
from components.header import Header
from components.keyPad import Keypad
from core import session_core
from core.readings import Readings
from core.session_core import SessionCore
from util.dictionary import arabic
import tkinter as tk                # python 3
import time
import datetime

from datetime import datetime



class TruckReception(tk.Frame):
    # self: represents the current object. This is a common first parameter for any method of a class.
    # parent: represents a widget to act as the parent of the current object. All widgets in tkinter except the root
    # window require a parent (sometimes also called a master)
    # controller: represents some other object that is designed to act as a common point of interaction for several
    # pages of widgets. It is an attempt to decouple the pages. That is to say, each page doesn't need to know about
    # the other pages. If it wants to interact with another page, such as causing it to be visible, it can ask the
    # controller to make it visible
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg="#fff")
        self.controller = controller
        # self.render(parent)

    def set_text(self, value):
        self.input_target.insert(10, value)

    def clear_text(self):
        self.input_target.delete(0, 'end')

    def next_Entry(self):
        if self.tn_txt.get() == '':
            self.tn_txt.focus_set()
            self.handle_click(self.tn_txt)
        elif self.trn_txt.get()=='':
            self.trn_txt.focus_set()
            self.handle_click(self.trn_txt)
        elif self.nn_txt.get() =='':
            self.nn_txt.focus_set()
            self.handle_click(self.nn_txt)
        else:
            self.focus_out(self.nn_txt)
            self.show_result()

    def focus_out(self,value):
        if value.get() != '':
            current_time_ms = int(round(time.time() * 1000))
            current_time = current_time_ms - SessionCore.get_offset_time()
            currentSeconed = current_time / 1000
            location_time=time.localtime(currentSeconed)
            date_time = (f"{location_time.tm_year}-{location_time.tm_mon}-{location_time.tm_mday} {location_time.tm_hour}:{location_time.tm_min}:{location_time.tm_sec}")
            if value ==self.tn_txt:
                Readings.set_tn({'value':value.get(),'source':'manual','Accurace':'100','time_stamp':date_time})
            elif value == self.trn_txt:
                Readings.set_trn({'value':value.get(),'source':'manual','Accurace':'100','time_stamp':date_time})
            elif value == self.nn_txt:
                print('inside nn in focus')
                Readings.set_nn({'value':value.get(),'source':'manual','Accurace':'100','time_stamp':date_time})

    def handle_click(self,target):
        self.input_target = target

    def show_result(self):
        result = {}
        result["tn"] = self.tn_txt.get()
        result["trn"] = self.trn_txt.get()
        result["nn"] = self.nn_txt.get()
        self.controller.set_app_state('TruckReception',result)
        self.controller.show_frame("ResultPage")

    def render(self,controller):
        ####################################################################################
        Header.render(self)
        ####################################################################################
        tn_lbl = tk.Label(self,bg="#fff",width=10, text=arabic("رقم الشاحنة"),font=self.controller.title_font , justify="right")
        tn_lbl.grid(column=2, row=1,pady='20')
        tn_txt = ttk.Entry(self, width=20,font=("Amiri", 26), justify="right")
        tn_txt.grid(column=1, row=1,sticky='e')
        tn_txt.bind("<1>",lambda event: self.handle_click(tn_txt))
        tn_txt.bind('<FocusOut>', lambda event: self.focus_out(tn_txt))
        # ####################################################################################
        trn_lbl = tk.Label(self,bg="#fff",width=10, text=arabic("رقم المقطورة"),font=self.controller.title_font, justify="right")
        trn_lbl.grid(column=2, row=2,pady='10')
        trn_txt = ttk.Entry(self, width=20, font=("Amiri", 26), justify="right")
        trn_txt.grid(column=1, row=2,sticky='e')
        trn_txt.bind("<1>",lambda event: self.handle_click(trn_txt))
        trn_txt.bind('<FocusOut>', lambda event: self.focus_out(trn_txt))
        # #####################################################################################
        nn_lbl = tk.Label(self,bg="#fff",width=10, text=arabic("الرقم الوطني"), font=self.controller.title_font, justify="right")
        nn_lbl.grid(column=2, row=3,pady='20')
        nn_txt = ttk.Entry(self, width=20, font=("Amiri", 26), justify="right")
        nn_txt.grid(column=1, row=3,sticky='e')
        nn_txt.bind("<1>",lambda event: self.handle_click(nn_txt))
        # nn_txt.bind("<FocusOut>", lambda event: self.focus_out(nn_txt))
        #########################################################################################
        self.tn_txt = tn_txt
        self.trn_txt = trn_txt
        self.nn_txt = nn_txt
        # #####################################################################################
        print(len(Readings.get_tn()),'this is the length')
        if len(Readings.get_tn()) > 0 :
            self.tn_txt.insert(10, Readings.get_tn()[0]['value'])
            self.trn_txt.insert(10, Readings.get_trn()[0]['value'])
            self.nn_txt.insert(10, Readings.get_nn()[0]['value'])
        else:
            self.tn_txt.insert(10, Readings.get_tn())
            self.trn_txt.insert(10, Readings.get_trn())
            self.nn_txt.insert(10, Readings.get_nn())
        #########################################################################################
        self.tn_txt.focus_set()
        self.handle_click(self.tn_txt)
        ########################################################################################3
        keypad = Keypad(self)
        keypad.grid(row=5, rowspan=3, column=1, sticky="e")


