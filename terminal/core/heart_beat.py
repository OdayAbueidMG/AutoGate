
class HeartBeat:
    socket_status=False

    @staticmethod
    def set_socket_status(value):
        HeartBeat.socket_status = value

    @staticmethod
    def get_socket_status():
        return HeartBeat.socket_status