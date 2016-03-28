# -*- coding: utf-8 -*-

'''
    created by Adam Sun
'''

from twisted.internet.protocol import Factory
from twisted.internet.endpoints import TCP4ServerEndpoint
from twisted.internet import reactor
from test import QOTD

class QOTDFactory(Factory):

    def buildProtocol(self, addr):
        return QOTD()


#start the server
print('start the server')
endpoint = TCP4ServerEndpoint(reactor, 8007)
endpoint.listen(QOTDFactory())
reactor.run()