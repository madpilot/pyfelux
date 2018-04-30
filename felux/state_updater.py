import asyncio

class StateUpdater(asyncio.DatagramProtocol):
    def __init__(self, loop, manager):
        self.loop = loop
        self.manager = manager
        self.transport = None

    def connection_made(self, transport):
        self.transport = transport

    def datagram_received(self, data, addr):
        self.manager.update(data)

    def wait(self, device):
        return self.manager.wait_for_response(device, self.loop)

    def cleanup(self):
        if self.transport:
            self.transport.close()
            self.transport = None
