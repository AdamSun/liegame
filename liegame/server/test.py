# -*- coding: utf-8 -*-

'''
    created by Adam Sun
'''

from twisted.internet.protocol import Protocol

class Echo(Protocol):

    def __init__(self, factory):
        self.factory = factory

    def dataReceived(self, data):
        self.transport.write(data)

    def connectionMade(self):
        self.factory.numProtocols = self.factory.numProtocols + 1
        self.transport.write(
            "Welcome! There are currently %d open connections.\n" %
            (self.factory.numProtocols,))

    def connectionLost(self, reason):
        self.factory.numProtocols = self.factory.numProtocols - 1



class QOTD(Protocol):
    def connectionMade(self):
        self.transport.write("An apple a day keeps the doctor away\r\n")
        self.transport.loseConnection()