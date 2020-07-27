import os
from Messages.Message import Message


class ServerConfigMessage(Message):
    def __init__(self):
        """
        Message of type config sent from server.
        attributes:
        1- message_type
        2- config_data
        """
        self.message_type = "SERVER_CONFIG_MESSAGE"
        self.config_data = None

    def get_config_data(self):
        return self.config_data

    def set_config_data(self, data):
        self.config_data = data

