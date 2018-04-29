class Manager:
    def __init__(self, callback=None):
        self._devices = []
        self._callback = callback

    def add_device(self, device):
        self._devices = list(filter(lambda d: d.id != device.id, self._devices))
        self._devices.append(device)
        if self._callback:
            self._callback(('add', device))

    def remove_device(self, device):
        self._devices = list(filter(lambda d: d != device, self.devices))
        if self._callback:
            self._callback(('remove', device))

    def update(self, data):
       decoded = felux.API.decode(data)
       devices = list(filter(lambda d: d.id == decoded['id']))
       map(lambda d: d.set_state(decoded), devices)

    @property
    def devices(self):
        return self._devices


