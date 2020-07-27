# device's IP address
SERVER_HOST = "192.168.1.10"
SERVER_PORT = 5000
BUFFER_LENGTH = 10
HEADER_LENGTH = 14
TOKEN = "ODAY"

class Config:
    printer_model = ''
    front_camera_ip = ''
    rear_camera_ip = ''
    face_camera_ip = ''
    lane_view_camera_ip = ''

    def extract_config(self,config):
        if "printer" in config:
            printer_model = config["printer"]
            Config.set_print_model(printer_model)

        if "front_camera" in config:
            front_camera_ip = config['front_camera']
            Config.set_front_camera(front_camera_ip)

        if "rear_camera" in config:
            rear_camera_ip = config['rear_camera']
            Config.set_rear_camera(rear_camera_ip)

        if "face_camera" in config:
            face_camera_ip = config['face_camera']
            Config.set_face_camera(face_camera_ip)

        if "lane_view_camera" in config:
            lane_view_camera = config['lane_view_camera']
            Config.set_lane_view_camera(lane_view_camera)

    @staticmethod
    def set_print_model(value):
        Config.printer_model = value

    @staticmethod
    def get_printer_model():
        return Config.printer_model
    #####################################################
    @staticmethod
    def set_front_camera(value):
        Config.front_camera_ip = value

    @staticmethod
    def get_front_camera():
        return Config.front_camera_ip
    #####################################################
    @staticmethod
    def set_rear_camera(value):
        Config.rear_camera_ip = value

    @staticmethod
    def get_rear_camera():
        return Config.rear_camera_ip
    #####################################################
    @staticmethod
    def set_face_camera(value):
        Config.face_camera_ip = value

    @staticmethod
    def get_face_camera():
        return Config.face_camera_ip
    #####################################################
    @staticmethod
    def set_lane_view_camera(value):
        Config.lane_view_camera_ip = value

    @staticmethod
    def get_face_camera():
        return Config.lane_view_camera_ip
# PRINTER_MODEL


