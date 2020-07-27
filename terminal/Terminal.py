
import tkinter as tk                # python 3
from tkinter import ttk
from tkinter import font  as tkfont # python 3
from ttkthemes import ThemedTk, ThemedStyle
from Messages.ConfigMessage import ConfigMessage
from core.clientSocket import ClientSocket, CLIENT_CONFIG_MESSAGE
from core.heart_beat import HeartBeat
from pages.HomePage import HomePage
from pages.ticketStatusMonitoring import ticketStatusMonitoring
from pages.Settings import Settings
from pages.TruckReception import TruckReception
from pages.ResultPage import ResultPage
from pages.FirstTrip import FirstTrip


class Terminal(tk.Tk):
    state = {}
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title_font = tkfont.Font(family='Amiri' ,size=20, slant="italic")
        #open socket with server
        try:
            self.client_socket = ClientSocket()
            #request config message from server
            config_message= ConfigMessage()
            config_message.set_type(CLIENT_CONFIG_MESSAGE)
            self.client_socket.send_msg(config_message.json())
            HeartBeat.set_socket_status(True)
        except:
            self.client_socket = ''
            HeartBeat.set_socket_status(False)
            print("An exception occurred")
        # TODO:run heartbeat agent

        #TODO:run hardware lestiners

        #regester screen
        self.register_screens()
        #how first scrrn
        self.show_frame("HomePage")

    # ---------------------------------------------------------------------------------- #
    # ------------ loop over register screens and show certain page -------------------- #
    # ---------------------------------------------------------------------------------- #
    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()
        for widget in frame.winfo_children():
            widget.destroy()
        frame.render(self)

    def set_app_state(self,page,result):
        if page == 'TruckReception':
            self.state['truck_reception']=result
        elif page == 'FirstTrip' :
            self.state['first_trip'] = result

    # --------------------------------------------------------------------- #
    # ------------ load screen from memory and show it -------------------- #
    # --------------------------------------------------------------------- #
    def register_screens(self):
        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.grid()
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        self.frames["HomePage"] = HomePage(parent=container, controller=self)
        self.frames["TruckReception"] = TruckReception(parent=container, controller=self)
        self.frames["Settings"] = Settings(parent=container, controller=self)
        self.frames["ResultPage"] = ResultPage(parent=container, controller=self)
        self.frames["FirstTrip"] = FirstTrip(parent=container, controller=self)
        self.frames["ticketStatusMonitoring"] = ticketStatusMonitoring(parent=container, controller=self)
        self.frames["HomePage"].grid(row=0, column=0, sticky="nsew")
        self.frames["TruckReception"].grid(row=0, column=0, sticky="nsew")
        self.frames["Settings"].grid(row=0, column=0, sticky="nsew")
        self.frames["ResultPage"].grid(row=0, column=0, sticky="nsew")
        self.frames["FirstTrip"].grid(row=0, column=0, sticky="nsew")
        self.frames["ticketStatusMonitoring"].grid(row=0,column=0,sticky="nsew")



if __name__ == "__main__":
    
    app = Terminal()
    app.geometry("1024x768")
    # app.attributes('-fullscreen', True)
    app.configure(bg='#fff')

    style = ThemedStyle(app)
    style.set_theme("radiance")
    app.mainloop()