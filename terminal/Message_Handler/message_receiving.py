import pickle

from core.config import HEADER_LENGTH


def recive_header_message(client_socket):
    # get message header(size), recive only HEADER_LENGTH bytes
    msg_header = client_socket.recv(HEADER_LENGTH)
    if not msg_header:
        return (None, None)
    header = msg_header.decode("utf-8").split("_")
    message_size = int(header[0])
    message_type = header[1]
    if message_type:
        return (message_size, message_type)
    return (message_size, None)


def recive_full_message(message_size, client_socket):
    full_msg = client_socket.recv(message_size)
    msg_obj = pickle.loads(full_msg)
    return msg_obj


def recive_pdf_message(message_size, client_socket):
    with open("pdf.pdf", "wb") as f:
        for _ in range(message_size):
            bytes_read = client_socket.recv(message_size)
            if not bytes_read:
                # nothing is received
                # file transmitting is done
                break
            # write to the file the bytes we just received
            f.write(bytes_read)

        # TODO::print waybill
