# -*- coding: utf-8 -*-

'''
    super class define need to be inherited
    created by Adam Sun
'''

from twisted.internet import protocol
import struct

class LGBaseProtocol(protocol.Protocol):

    def connectionMade(self):
        self.factory.add_connection(self)
        assert not hasattr(self, 'session')
        self.createSession()

    def connectionLost(self, reason):
        self.session.lost_connection()
        self.factory.remove_connection()

    def dataReceived(self, data):
        self.session.read_data(data)

    def createSession(self):
        self.session = LGBaseSession(self.factory, self)


class LGBaseFactory(protocol.Factory):

    def __init__(self):
        self.__connections = []

    def add_connection(self, con):
        """
        record the protocol
        :param con:
        :return:
        """
        self.__connections.append(con)

    def remove_connection(self, con):
        """
        remove the record of protocol
        :param con:
        :return:
        """
        self.__connections.remove(con)

    def send_all(self, data):
        for con in self.__connections:
            con.transport.write(data)

    def buildProtocol(self, addr):
        return LGBaseProtocol()


#包头长度
HEADER_LEN = 2
#命令长度
OPCODE_LEN = 2

class Package(object):
    def __init__(self, cmd, data = None):
        self.read_cursor = 0
        self.cmd = cmd
        if data:
            assert isinstance(data, str)
            self.pkg_data = data
        else:
            self.pkg_data = ''

    def reset_read_cursor(self):
        self.read_cursor = 0

    def get_full_size(self):
        return 4 + len(self.pkg_data)

    def get_full_data(self):
        return struct.pack('>H', len(self.pkg_data)+2) + struct.pack('<H', self.cmd) + self.pkg_data

    def __lshift__(self, arg):
        #对于字符串，用[str_length(uint16)]跟[字符串]串接表示
        #log.msg('pkg %s << %s' % (opcodes[self.cmd],str(arg)), logLevel = logging.DEBUG)
        if isinstance(arg, tuple):
            assert len(arg) > 1
            format = arg[0]
            assert isinstance(format, str) and len(format) > 0
            if format[0] not in ('>','<'):
                format = '<' + format
            else:
                if format[0] == '>':
                    format = '<' + format[1:]
            self.pkg_data += struct.pack(format, *(arg[1:]))
        else:
            assert False
        return self

    def __rshift__(self, format):
        assert isinstance(format, str) and len(format) > 0
        if format[0] not in ('>','<'):
            format = '<' + format
        else:
            if format[0] == '>':
                format = '<' + format[1:]
        size = struct.calcsize(format)
        if size > len(self.pkg_data) - self.read_cursor:
            return None
        rt = struct.unpack_from(format, self.pkg_data, self.read_cursor)
        self.read_cursor += size
        return rt


class LGBaseSession(object):
    """
    session base class
    """

    def __init__(self, factory, connection):
        self.factory = factory
        self.connection = connection

    def read_data(self, data):
        pass

    def send_data(self, data):
        if self.connection:
            self.connection.transport.write(data)
            return True
        return False

    def send_package(self, pkg):
        assert isinstance(pkg, Package)
        self.send_data(pkg.get_full_data())

    def is_connected(self):
        return self.connection != None

    def lost_connection(self):
        self.connection = None