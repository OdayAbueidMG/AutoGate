from Messages.Message import Message


class Ack(Message):
    def __init__(self):
        self.message_type = "ACK"
        self.ack = False
        self.id = "Random"

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

