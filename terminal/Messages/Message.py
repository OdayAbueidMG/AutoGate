class Message:
    def __init__(self):
        self.message_type = None
        self.ack = True

    def json(self):
        return self.__dict__
    def get_type(self):
        return self.message_type

    def set_type(self, message_type):
        self.message_type = message_type

    def get_ack(self):
        return self.ack

    def set_ack(self, ack):
        self.ack = ack