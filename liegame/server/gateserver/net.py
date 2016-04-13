# -*- coding: utf-8 -*-

"""
   the subclass of the internet api
    created by Adam Sun
"""
from common import base
from common.model import user
import app
import config
import queue

################################ gate net api #####################################

class LGGateProtocol(base.LGBaseProtocol):
    def create_session(self):
        self.session = LGGateSession(self.factory, self)

class LGGateFactory(base.LGBaseFactory):
    protocol = LGGateProtocol

class LGGateSession(base.LGBaseSession):
    def __init__(self, factory, connection):
        super(LGGateSession, self).__init__(factory, connection)
        self.user = user.User()
        self.queue = queue.Queue()


    def handle_data(self, type, subtype, data):
        self.connnect_db()
        # if the db server is not connected, we should do nothing but wait
        if self.db_factory == None or self.db_factory.db_connection_status == config.DB_CONNECTION_STATUS_CONNECT:
            self.queue.push(self.handle_data, (type, subtype, data))
            return
        if type == config.MODULE_USER:
            self.handle_user(type, subtype, data)

    def lost_connection(self):
        self.db_factory = None

    def handle_user(self, type, subtype, data):
        if subtype == config.MODULE_USER_CREATE:
            (username, password, nick_name, email, avatar, is_admin) = data >> 'sssssB'


    def connnect_db(self):
        if self.db_factory != None:
            return
        self.db_factory = LGDBFactory(self)
        db_ip = config.DB_SERVER_IP
        db_port = config.DB_SERVER_PORT
        app.app.reactor.connnectTCP(db_ip, db_port, self.db_factory)

    def delay_handle_data(self):
        """
        handle the data after the db server is connected
        :return:
        """
        len = self.queue.len()
        for i in range(0, len):
            element = self.queue.pop()
            if element != None:
                element[0](element[1][0], element[1][1], element[1][2])


################################ db net api #####################################

class LGDBProtocol(base.LGBaseProtocol):

    def __init__(self):
        super(LGDBProtocol, self).__init__()

    def create_session(self):
        self.session = LGDBSession(self.factory, self)

    def connectionMade(self):
        super(LGDBProtocol, self).connectionMade()
        self.factory.db_connection_status = config.DB_CONNECTION_STATUS_CONNECT
        self.factory.gate_session.delay_handle_data()


class LGDBFactory(base.LGBaseFactory):
    protocol = LGDBProtocol

    def __init__(self, gate_session):
        super(LGDBProtocol, self).__init__()
        self.gate_session = gate_session
        self.db_connection_status = config.DB_CONNECTION_STATUS_DISCONNECT

    def remove_connection(self, con):
        self.gate_session = None

class LGDBSession(base.LGBaseSession):

    def __init__(self, factory, connection):
        super(LGGateSession, self).__init__(factory, connection)

    def handle_data(self, type, subtype, data):
        if (self.factory != None) and (self.factory.gate_session != None):
            self.factory.gate_session.handle_data(type, subtype, data)