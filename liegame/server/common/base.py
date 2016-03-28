# -*- coding: utf-8 -*-

'''
    super class define need to be inherited
    created by Adam Sun
'''

from twisted.internet import protocol

class LGBaseProtocol(protocol.Protocol):
    def dataReceived(self, data):
        self.transport.write(data)


class LGBaseFactory(protocol.Factory):

    def buildProtocol(self, addr):
        return LGBaseProtocol()