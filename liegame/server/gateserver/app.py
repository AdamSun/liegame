# -*- coding: utf-8 -*-

'''
    the startup of gateserver
    created by Adam Sun
'''

from common import base
from twisted.internet import reactor
import config

class LGGateProtocol(base.LGBaseProtocol):
    def dataReceived(self, data):
        print data

class LGGateFactory(base.LGBaseFactory):
    def buildProtocol(self, addr):
        return LGGateProtocol()


def start():
    print 'gate server start successfully'
    port = config.PORT
    reactor.listenTCP(port, LGGateFactory())
    reactor.run()

if __name__ == '__main__' :
    start()