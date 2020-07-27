
from tkinter import ttk
from tkinter import font  as tkfont # python 3

class Settings(ttk.Frame):

    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        self.controller = controller
        label = ttk.Label(self, text="Settings Page", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = ttk.Button(self, text="Go to the start page",
                            command=lambda: controller.show_frame("HomePage"))
        button.pack()
