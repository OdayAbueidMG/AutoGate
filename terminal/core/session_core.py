
class SessionCore:
    session_obj = {'id': None,'ticket_id':None, 'data_collection': {},'events': None}
    server_time = ''
    offset_time = 0

    @staticmethod
    def set_offset_time(value):
        SessionCore.offset_time = value

    @staticmethod
    def get_offset_time():
        return SessionCore.offset_time

    @staticmethod
    def set_server_time(value):
        SessionCore.server_time = value
    @staticmethod
    def get_server_time():
        return SessionCore.server_time
    @staticmethod
    def set_session_id(value):
        SessionCore.session_obj['id'] = value

    @staticmethod
    def get_session():
        return SessionCore.session_obj

    @staticmethod
    def set_ticket_id(value):
        SessionCore.session_obj['ticket_id'] = value

    @staticmethod
    def set_tn(value):
        SessionCore.session_obj['data_collection']['tn'] = value

    @staticmethod
    def get_tn():
        return SessionCore.session_obj['data_collection']['tn']

    @staticmethod
    def set_trn(value):
        SessionCore.session_obj['data_collection']['trn'] = value

    @staticmethod
    def get_trn():
        return SessionCore.session_obj['data_collection']['trn']

    @staticmethod
    def set_nn(value):
        SessionCore.session_obj['data_collection']['nn'] = value

    @staticmethod
    def get_nn():
        return SessionCore.session_obj['data_collection']['nn']



