# -*- coding: utf-8 -*-

"""
    the entrance of db server
    created by Adam Sun
"""

from twisted.internet import reactor
from twisted.enterprise import adbapi
import config
from common import base
import dbconnection
from common.model import user
import hashlib
import MySQLdb


dbpool = adbapi.ConnectionPool("MySQLdb", config.MYSQL_IP, config.MYSQL_USER, config.MYSQL_PASSWORD, config.DB_NAME)

class LGDBProtocol(base.LGBaseProtocol):
    def dataReceived(self, data):
        print data

    def connectionMade(self):
        if self.factory.connection_count() >= config.MAX_CONNECTION_NUMBER:
            self.transport.write("the connection is full")
            print "the connection is full"
        else:
           super(LGDBProtocol, self).connectionMade()

class LGDBFactory(base.LGBaseFactory):
    def buildProtocol(self, addr):
        return LGDBProtocol()

class LGDBSession(base.LGBaseSession):
    def __init__(self, factory, connection):
        super(LGDBSession, self).__init__(factory, connection)
        if config.db_type == config.DB_TYPE_MYSQL:
            self.user = user.User()
            self.db_connection = dbconnection.MYSQLConnnection(self, dbpool)
            self.db_connection.connect()

    def lost_connection(self):
        super(LGDBSession, self).lost_connection()
        if self.db_connection:
            self.db_connection.disconnect()
            self.db_connection = None

class App(object):

    def start(self):
        if config.DEBUG_MODE:
            self.test_db()
        print 'db server start successfully'
        port = config.PORT
        reactor.listenTCP(port, LGDBFactory())
        reactor.run()

    def stop(self):
        print "disconnect the socket"
        reactor.stop()

    def test_db(self):
        for i in range(0, 1000):
            session = LGDBSession(None, None)
            session.user.user_name = u"adam123%s" % i
            session.user.password = hashlib.sha224(u"123456").hexdigest()
            session.user.nick_name = u"Adam"
            session.user.email = u"123@qq.com"
            session.user.avatar = u"http://127.0.0.1/liegamedata/avatar/default.png"
            session.user.is_admin = 0
            session.db_connection.query(0, 1)



if __name__ == '__main__':
    app = App()
    app.start()