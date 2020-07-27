from Messages.Message import Message


class Session(Message):
    def __init__(self):
        super().__init__()
        self.session_id = "20200722"
        self.session_data=None
    def get_session_id(self):
        return self.session_id

    def set_session_id(self, id):
        self.session_id = id

    def set_session_data(self,data):
        self.session_data=data