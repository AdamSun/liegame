# -*- coding: utf-8 -*-

'''
    the startup of gate server
    created by Adam Sun
'''

from twisted.internet import reactor

import config
import login
from net import LGGateFactory, LGDBFactory
from common.event import EventManager


class App(object):

    def __init__(self):
        self.login_controller = None
        self.event_manager = None
        self.db_factory = None
        self.reactor = reactor

    def init(self):
        self.db_factory = LGDBFactory()
        self.event_manager = EventManager()
        self.login_controller = login.LoginController(self.event_manager)
        self.login_controller.init_event();

    def dipose(self):
        if self.login_controller:
            self.login_controller.remove_event()
            self.login_controller = None

    def start(self):
        print 'gate server start successfully'
        self.init()
        #listen the client to connnect
        port = config.PORT
        self.reactor.listenTCP(port, LGGateFactory())
        self.reactor.run()

    def stop(self):
        print "disconnect the socket"
        self.reactor.stop()

app = App()
if __name__ == '__main__':
    app.start()