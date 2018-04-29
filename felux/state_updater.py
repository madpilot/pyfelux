import asyncio

class StateUpdater(asyncio.DatagramProtocol):
    def __init__(self, loop, light):
        self.loop = loop
        self.light = light
        self.future = asyncio.Future();
        self.transport = None

    def connection_made(self, transport):
        self.transport = transport

    def datagram_received(self, data, addr):
        self.light.set_state(data)

        if self.future and not self.future.done():
            self.future.set_result(None)

    def wait(self):
        if self.future == None or self.future.done():
            self.future = asyncio.Future();
        return self.future

    def cleanup(self):
        if self.transport:
            self.transport.close()
            self.transport = None
