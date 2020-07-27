
from tkinter import ttk, PhotoImage  # Normal Tkinter.* widgets are not themed!
from tkinter import Frame
import tkinter as tk

class Keypad(tk.Frame):

    def  __init__(self, parent):
        tk.Frame.__init__(self, parent,bg="#fff")
        frame1 = Frame(self,bg="#fff")

        def keyPad_clicked_handler(value):
            parent.set_text(value)
        frame1.grid(row=5, rowspan=3, column=1)
        number7_btn = PhotoImage(file='assets/number7.png')
        number7_img_label = tk.Label(self, image=number7_btn,bg="#fff")
        number7_img_label.image = number7_btn
        btn7 = tk.Button(self, image=number7_btn, borderwidth=0,bg='#fff',highlightthickness='0')
        btn7.bind("<1>", lambda event: keyPad_clicked_handler("7"))
        btn7.grid(column=0, row=0, sticky='e',padx='10')
        ############################################################################
        number8_btn = PhotoImage(file='assets/number8.png')
        number8_img_label = tk.Label(self, image=number8_btn,bg="#fff")
        number8_img_label.image = number8_btn
        btn8 = tk.Button(self, image=number8_btn, borderwidth=0,bg="#fff",highlightthickness='0')
        btn8.bind("<1>", lambda event: keyPad_clicked_handler("8"))
        btn8.grid(column=1, row=0, sticky='e',padx='10')
        ############################################################################
        number9_btn = PhotoImage(file='assets/number9.png')
        number9_img_label = tk.Label(self, image=number7_btn,bg="#fff")
        number9_img_label.image = number9_btn
        btn9 = tk.Button(self, image=number9_btn, borderwidth=0,bg="#fff",highlightthickness='0')
        btn9.bind("<1>", lambda event: keyPad_clicked_handler("9"))
        btn9.grid(column=2, row=0, sticky='e',padx='5')
        ############################################################################
        number4_btn = PhotoImage(file='assets/number4.png')
        number4_img_label = tk.Label(self, image=number4_btn,bg="#fff")
        number4_img_label.image = number4_btn
        btn4 = tk.Button(self, image=number4_btn, borderwidth=0,bg="#fff",highlightthickness='0')
        btn4.bind("<1>", lambda event: keyPad_clicked_handler("4"))
        btn4.grid(column=0, row=1, sticky='e',padx='10',pady='3')
        ############################################################################
        number5_btn = PhotoImage(file='assets/number5.png')
        number5_img_label = tk.Label(self, image=number5_btn,bg="#fff")
        number5_img_label.image = number5_btn
        btn5 = tk.Button(self, image=number5_btn, borderwidth=0,bg="#fff",highlightthickness='0')
        btn5.bind("<1>", lambda event: keyPad_clicked_handler("5"))
        btn5.grid(column=1, row=1, sticky='e',padx='10',pady='3')
        ############################################################################
        number6_btn = PhotoImage(file='assets/number6.png')
        number6_img_label = tk.Label(self, image=number6_btn,bg="#fff")
        number6_img_label.image = number6_btn
        btn6 = tk.Button(self, image=number6_btn, borderwidth=0,bg="#fff",highlightthickness='0')
        btn6.bind("<1>", lambda event: keyPad_clicked_handler("6"))
        btn6.grid(column=2, row=1, sticky='e',padx='5',pady='3')
        #############################################################################
        number1_btn = PhotoImage(file='assets/number1.png')
        number1_img_label = tk.Label(self, image=number1_btn,bg="#fff")
        number1_img_label.image = number1_btn
        btn1 = tk.Button(self, image=number1_btn, borderwidth=0,bg="#fff",highlightthickness='0')
        btn1.bind("<1>", lambda event: keyPad_clicked_handler("1"))
        btn1.grid(column=0, row=2, sticky='e',padx='10',pady='3')
        #############################################################################
        number2_btn = PhotoImage(file='assets/number2.png')
        number2_img_label = tk.Label(self, image=number2_btn,bg="#fff")
        number2_img_label.image = number2_btn
        btn2 = tk.Button(self, image=number2_btn, borderwidth=0,bg="#fff",highlightthickness='0')
        btn2.bind("<1>", lambda event: keyPad_clicked_handler("2"))
        btn2.grid(column=1, row=2, sticky='e',padx='10',pady='3')
        ############################################################################
        number3_btn = PhotoImage(file='assets/number3.png')
        number3_img_label = tk.Label(self, image=number3_btn,bg="#fff")
        number3_img_label.image = number3_btn
        btn3 = tk.Button(self, image=number3_btn, borderwidth=0,bg="#fff",highlightthickness='0')
        btn3.bind("<1>", lambda event: keyPad_clicked_handler("3"))
        btn3.grid(column=2, row=2, sticky='e',padx='5',pady='3')
        ###########################################################################
        number0_btn = PhotoImage(file='assets/number0.png')
        number0_img_label = tk.Label(self, image=number0_btn,bg="#fff")
        number0_img_label.image = number0_btn
        btn0 = tk.Button(self, image=number0_btn, borderwidth=0,bg="#fff",highlightthickness='0')
        btn0.bind("<1>", lambda event: keyPad_clicked_handler("0"))
        btn0.grid(column=1, row=3, sticky='e',padx='10')
        ############################################################################
        clear_btn = PhotoImage(file='assets/clear.png')
        clear_img_label = tk.Label(self, image=clear_btn,bg="#fff")
        clear_img_label.image = clear_btn
        lbl_clr = tk.Button(self,  image=clear_btn , command=lambda: parent.clear_text(),bg="#fff",highlightthickness='0')
        lbl_clr.grid(row=0, column=4, sticky='e',rowspan='2')
        ############################################################################
        apply_btn = PhotoImage(file='assets/apply.png')
        apply_img_label = tk.Label(self, image=apply_btn,bg="#fff")
        apply_img_label.image = apply_btn
        lbl_apply = tk.Button(self,  image=apply_btn , command=lambda: parent.next_Entry(),bg="#fff",highlightthickness='0')
        lbl_apply.grid(row=2, column=4, sticky='e',rowspan='2')
        ############################################################################
        self.frame = frame1

    def get(self):
        return self.frame.get()