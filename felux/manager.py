class Manager:
    def __init__(self, callback=None):
        self._devices = []
        self._callback = callback
        self._futures = {}

    def add_device(self, device):
        if device.id in map(lambda d: d.id, self._devices):
            devices = filter(lambda d: d.id == device.id, self._devices)
            # We already know about the device, so clone the device details, while keeping the state.
            # Note to future self: map is a generator - it doesn't execute until you do something to it - hence the list that doesn't seem to do anyhting.
            list(map(lambda d: d.copy(device), devices))

            if self._callback:
                self._callback(('update', device.id))
        else:
            self._devices.append(device)

            if self._callback:
                self._callback(('add', device.id))

    def remove_device(self, device):
        self._devices = list(filter(lambda d: d != device, self.devices))
        if self._callback:
            self._callback(('remove', device.id))

    def update(self, data):
        decoded = felux.API.decode(data)
        devices = list(filter(lambda d: d.id == decoded['id']))
        map(lambda d: d.set_state(decoded), devices)

        if device.id in self._futures:
            future = self._futures[device.id]
            future.set_result(decoded)
            self._futures = list(filter(lambda f: f == future, self._futures))

    def wait_for_response(self, device, loop):
        if not (device.id in self._futures):
            self._futures.append(loop.create_future())

        return self._futures[device.id]

    @property
    def devices(self):
        return self._devices


