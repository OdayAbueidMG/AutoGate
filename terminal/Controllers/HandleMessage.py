import pickle
from Messages.ServerConfigMessage import ServerConfigMessage
from Messages.message_types import *
from core.session_core import SessionCore
from core.config import BUFFER_LENGTH, Config
import time
from pages.ticketStatusMonitoring import ticketStatusMonitoring


class MessageHandler:
    def __init__(self, msg, server_socket):
        self.msg = msg
        self.server_socket = server_socket
        self.handle_message_scenario()

    # here we send the message to its path (switch case)
    def handle_message_scenario(self):
        message_type = self.msg.get('message_type')
        if message_type == SERVER_CONFIG_MESSAGE:
            # config_message = self.msg.get_config_data()
            config_message = self.msg.get('config_data')
            print(config_message,'config_message')
            Config.extract_config(self,config_message)
        if message_type == SESSION_START:
            start_session_msg = self.msg.get('session_id')
            server_time=self.msg.get('timestamp')
            currentmillis = int(round(time.time() * 1000))
            offset = server_time - currentmillis
            SessionCore.set_offset_time(offset)
            SessionCore.set_server_time(server_time)
            SessionCore.set_session_id(start_session_msg)
            ################################################3
        if message_type == SESSION_TICKET:
            create_ticket_msg = self.msg.get('ticket_id')
            SessionCore.set_ticket_id(create_ticket_msg)
            # PrintWaiting(self)
            ticketStatusMonitoring.refresh()



    # send message to client
    def send_msg_to_server(self, msg_obj=None):
        """
        serialize msg object to send it to server, send msg with header containe msg size,and its type
        """
        serialized_msg = pickle.dumps(msg_obj)
        msg_header = f"{len(serialized_msg):<{BUFFER_LENGTH}}"
        full_msg = bytes(msg_header.encode("utf-8")) + serialized_msg

        # send msg to client
        print(full_msg)
        self.server_socket.send(full_msg)

