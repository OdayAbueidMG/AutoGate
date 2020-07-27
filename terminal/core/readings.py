from core.session_core import SessionCore


class Readings:
    tn = []
    trn = []
    nn = []
    date_time=''

    @staticmethod
    def get_tn():
        return Readings.tn

    @staticmethod
    def set_tn(value):
        Readings.tn.append(value)
        if SessionCore.get_session()['id']:
            SessionCore.set_tn(Readings.tn)
    @staticmethod
    def set_trn(value):
        Readings.trn.append(value)
        if SessionCore.get_session()['id']:
            SessionCore.set_trn(Readings.trn)
    @staticmethod
    def set_date_time(value):
        Readings.date_time = value
    @staticmethod
    def get_date_time():
        return Readings.date_time

    @staticmethod
    def get_trn():
        return Readings.trn

    @staticmethod
    def set_nn(value):
        Readings.nn.append(value)
        if SessionCore.get_session()['id']:
            SessionCore.set_nn(Readings.nn)
    @staticmethod
    def get_nn():
        return Readings.nn


