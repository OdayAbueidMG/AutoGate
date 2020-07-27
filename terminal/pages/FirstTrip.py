from components.header import Header
import tkinter as tk
from tkinter import ttk, PhotoImage
import datetime
from core.readings import Readings
from util.dictionary import arabic

class FirstTrip(tk.Frame):
    def __init__(self,parent, controller):
        tk.Frame.__init__(self, parent,bg="#fff")
        self.controller = controller

    def clickedHandler(self,value):
        current_date_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if value == 'import' or value == 'export' or value == 'import_export':
            self.operation_type = value
            Readings.set_operation_type({'value':value,'source':'manual','Accurace':'100','time_stamp':current_date_time})
            if value == 'import':
                self.btn_import.configure(highlightbackground="#3995d2",highlightthickness=1,bg="#3995d2")
                self.btn_export.configure(highlightbackground='#fff', highlightthickness=0, bg="#fff")
                self.imp_exp.configure(highlightbackground='#fff', highlightthickness=0, bg="#fff")
            elif value == 'export':
                self.btn_export.configure(highlightbackground='#3995d2', highlightthickness=0, bg="#3995d2")
                self.btn_import.configure(highlightbackground="#fff",highlightthickness=1,bg="#fff")
                self.imp_exp.configure(highlightbackground='#fff', highlightthickness=0, bg="#fff")
            elif value == 'import_export':
                self.imp_exp.configure(highlightbackground='#3995d2', highlightthickness=0, bg="#3995d2")
                self.btn_import.configure(highlightbackground="#fff",highlightthickness=1,bg="#fff")
                self.btn_export.configure(highlightbackground='#fff', highlightthickness=0, bg="#fff")
        elif value == 'south_port' or value == 'main_port':
            self.discharge_location = value
            Readings.set_discharge_location({'value':value,'source':'manual','Accurace':'100','time_stamp':current_date_time})
            if value == 'south_port':
                self.south_port.configure(highlightbackground='#3995d2', highlightthickness=0, bg="#3995d2")
                self.main_port.configure(highlightbackground="#fff",highlightthickness=1,bg="#fff")
            elif value == 'main_port':
                self.main_port.configure(highlightbackground='#3995d2', highlightthickness=0, bg="#3995d2")
                self.south_port.configure(highlightbackground='#fff', highlightthickness=0, bg="#fff")
        elif value == 'camera':
            self.truck_route = value
            Readings.set_truck_route({'value':value,'source':'manual','Accurace':'100','time_stamp':current_date_time})
            if value == 'camera':
                self.camera_dest.configure(highlightbackground='#3995d2', highlightthickness=0, bg="#3995d2")


    def showResult(self):
        if Readings.get_operation_type() == '':
            return self.operation_type_warning.config(text=arabic("يجب اختيار نوع العملية قبل المتابعة"))
        else:
            self.operation_type_warning.config(text=arabic(""))
        if Readings.get_discharge_location() == '':
            return self.discharge_location_warning.config(text=arabic("يجب اختيار موقع التفريغ قبل المتابعة"))
        else:
             self.discharge_location_warning.config(text=arabic(""))
        if Readings.get_truck_route() == '':
            return self.destination_warning.config(text=arabic("يجب اختيار الوجهة قبل المتابعة"))
        else:
            self.destination_warning.config(text=arabic(""))

        self.controller.show_frame("ResultPage")

    def render(self,controller):

        Header.render(self)
        ###############################################################
        operation_type_lbl = tk.Label(self,bg="#fff",width=10, text=arabic("نوع العملية"),font=self.controller.title_font , justify="right")
        operation_type_lbl.grid(column=2, row=1,pady='10',sticky='e')
        operation_type_warning = tk.Label(self, text="", justify="right", fg="red",bg='#fff')
        operation_type_warning.grid(column=0, row=1)

        ###############################################################
        import_btn = PhotoImage(file='assets/import.png')
        import_img_label = tk.Label(self, image=import_btn, bg="#fff", highlightbackground="#f00",
                                    highlightthickness='0')
        import_img_label.image = import_btn
        btn_import = tk.Button(self, image=import_btn, borderwidth=0, bg="#fff")
        btn_import.bind("<1>", lambda event: self.clickedHandler("import"))
        btn_import.grid(column=2, row=2)
        ##############################################################3
        export_btn = PhotoImage(file='assets/export.png')
        export_img_label = tk.Label(self, image=export_btn,bg="#fff",highlightbackground="#f00",highlightthickness='0')
        export_img_label.image = export_btn
        btn_export = tk.Button(self, image=export_btn, borderwidth=0,bg="#fff")
        btn_export.bind("<1>", lambda event: self.clickedHandler("export"))
        btn_export.grid(column=1, row=2)
        ################################################################
        imp_exp_btn = PhotoImage(file='assets/import-export.png')
        imp_exp_img_label = tk.Label(self, image=imp_exp_btn,bg="#fff",highlightbackground="#f00",highlightthickness='0')
        imp_exp_img_label.image = imp_exp_btn
        imp_exp = tk.Button(self, image=imp_exp_btn, borderwidth=0,bg="#fff")
        imp_exp.bind("<1>", lambda event: self.clickedHandler("import_export"))
        imp_exp.grid(column=0, row=2)
        ################################################################
        discharge_location_lbl = tk.Label(self, bg="#fff", width=10, text=arabic("موقع التفريغ"), font=self.controller.title_font,justify="right")
        discharge_location_lbl.grid(column=2, row=3, pady='10', sticky='e')
        discharge_location_warning = tk.Label(self, text="", justify="right", fg="red",bg='#fff')
        discharge_location_warning.grid(column=0, row=3)
        ################################################################
        south_port_btn = PhotoImage(file='assets/south-port.png')
        south_port_label = tk.Label(self, image=south_port_btn, bg="#fff", highlightbackground="#f00",highlightthickness='0')
        south_port_label.image = south_port_btn
        south_port = tk.Button(self, image=south_port_btn, borderwidth=0, bg="#fff")
        south_port.bind("<1>", lambda event: self.clickedHandler("south_port"))
        south_port.grid(column=2, row=4)
        #################################################################
        main_port_btn = PhotoImage(file='assets/main-port.png')
        main_port_label = tk.Label(self, image=main_port_btn, bg="#fff", highlightbackground="#f00",
                                    highlightthickness='0')
        main_port_label.image = main_port_btn
        main_port = tk.Button(self, image=main_port_btn, borderwidth=0, bg="#fff")
        main_port.bind("<1>", lambda event: self.clickedHandler("main_port"))
        main_port.grid(column=1, row=4)
        ##################################################################
        destination_lbl = tk.Label(self, bg="#fff", width=10, text=arabic("الوجهة"),
                                          font=self.controller.title_font, justify="right")
        destination_lbl.grid(column=2, row=5, pady='10', sticky='e')
        destination_warning = tk.Label(self, text="", justify="right", fg="red", bg='#fff')
        destination_warning.grid(column=0, row=5)
        ##################################################################
        camera_dest_btn = PhotoImage(file='assets/camera-dest.png')
        camera_dest_label = tk.Label(self, image=camera_dest_btn, bg="#fff", highlightbackground="#f00",
                                   highlightthickness='0')
        camera_dest_label.image = camera_dest_btn
        camera_dest = tk.Button(self, image=camera_dest_btn, borderwidth=0, bg="#fff")
        camera_dest.bind("<1>", lambda event: self.clickedHandler("camera"))
        camera_dest.grid(column=2, row=6)
        ##################################################################
        button = ttk.Button(self, text=arabic("التالي"), command=lambda : self.showResult())
        button.grid(column=0, row=6)
        button = ttk.Button(self, text=arabic("رجوع"), command=lambda: self.controller.show_frame("TruckReception"))
        button.grid(column=1, row=6)
        ############################################################################
        self.btn_import = btn_import
        self.btn_export = btn_export
        self.imp_exp = imp_exp
        self.south_port = south_port
        self.main_port = main_port
        self.camera_dest = camera_dest
        self.operation_type_warning = operation_type_warning
        self.discharge_location_warning =discharge_location_warning
        self.destination_warning = destination_warning
        ########################################################################3
        self.clickedHandler(Readings.get_operation_type())
        self.clickedHandler(Readings.get_discharge_location())
        self.clickedHandler(Readings.get_truck_route())