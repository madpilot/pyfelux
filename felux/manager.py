class Manager:
    def __init__(self, callback=None):
        _devices = {}
        _callback = callback

    def add_device(self, device):
        _devices = list(filter(lambda d: d.id != device.id))
        append(_devices, device)
        callback((:add, device))

    def remove_device(self, device):
        _devices = list(filter(lambda d: d != device))
        callback((:remove, device))

    @property
    def devices(self):
        return _devices


