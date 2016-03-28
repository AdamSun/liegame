# -*- coding: utf-8 -*-

'''
    socket for connecting the server
    created by Adam Sun
'''

from twisted.internet import protocol, reactor
from model import globaldata

class LieGameProtocol(protocol.Protocol):
    def connectionMade(self):
        self.transport.write("hello, server")

    def dataReceived(self, data):
        globaldata.test_data = data
        globaldata.test_data_change = True
        self.transport.loseConnection()


class LieGameFactory(protocol.ClientFactory):
    def buildProtocol(self, addr):
        return LieGameProtocol()

    def clientConnectionFailed(self, connector, reason):
        print "Connection failed"
        reactor.stop()

    def clientConnectionLost(self, connector, reason):
        print "Connection lost"
        reactor.stop()