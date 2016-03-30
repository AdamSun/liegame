# -*- coding: utf-8 -*-

'''
    the startup of gate server
    created by Adam Sun
'''

from twisted.internet import reactor

import config
import login
from common import base
from common.event import EventManager
from common.model import user


class LGGateProtocol(base.LGBaseProtocol):
    def dataReceived(self, data):
        print data

class LGGateFactory(base.LGBaseFactory):
    def buildProtocol(self, addr):
        return LGGateProtocol()

class LGGateSession(base.LGBaseSession):
    def __init__(self, factory, connection):
        super(LGGateSession, self).__init__(factory, connection)
        self.user = user.User()


class App(object):

    def __init__(self):
        self.login_controller = None
        self.event_manager = None

    def init_controller(self):
        self.event_manager = EventManager()
        self.login_controller = login.LoginController(self.event_manager)
        self.login_controller.init_event();

    def dipose_controller(self):
        if self.login_controller:
            self.login_controller.remove_event()
            self.login_controller = None

    def start(self):
        print 'gate server start successfully'
        port = config.PORT
        reactor.listenTCP(port, LGGateFactory())
        reactor.run()

    def stop(self):
        print "disconnect the socket"
        reactor.stop()

if __name__ == '__main__':
    app = App()
    app.start()