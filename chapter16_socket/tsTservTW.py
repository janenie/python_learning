#!/usr/bin/env python

#using Twisted, if you dont have, please install first

from twisted.internet import protocol, reactor
from time import ctime

PORT = 21567

class TSServProtocol(protocol.Protocol):
  def connectionMade(self):
    clnt = self.clnt = self.transport.getPeer().host
    print '...connected from:', clnt
  def dataReceived(self, data):
    print 'received!'
    self.transport.write('[%s] %s' % (
      ctime(), data))
    
factory = protocol.Factory()
factory.protocol = TSServProtocol
print 'Waiting for connections..'
reactor.listenTCP(PORT, factory)
reactor.run()