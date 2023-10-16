from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor
from random import randint

class Client(DatagramProtocol):
    #initialize protocol with host and port
    #can be changed
    def __init__(self, host, port):
        #must change
        if host == 'localhost':
            host = "127.0.0.1"

        self.id = (host, port) #array of host name and port
        self.address = None #non by default -- does have anybody to talk to once connected
        print("Working on id", self.id)

    #once data is received
    def datagramReceived(self, datagram, addr):
        print(addr, ":", datagram)#print address and data sent

    #send message
    def send_message(self):
        while True:
            self.transport.write(input().encode('utf-8'), self.address)#send message to specified address

if __name__ == '__main__':
    port = randint(1000, 5000)
    reactor.listenUDP(port, Client('localhost', port))
    reactor.run()

        