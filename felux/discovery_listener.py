from socket import inet_ntoa
import felux

class DiscoveryListener:
    def __init__(self, manager):
        self._manager = manager

    def add_service(self, zeroconf, type, name):
        info = zeroconf.get_service_info(type, name)
        properties = info.properties.items()

        ip_address = inet_ntoa(info.address)
        host_name = info.server
        id = self._get_property(properties, "id")
        device_name = self._get_property(properties, "device_name")
        number_of_leds = self._get_property(properties, "leds")

        device = felux.Device(id, ip_address, host_name, device_name, number_of_leds)
        self._manager.add_device(device)

    def remove_server(self, zeroconf, type, name):
        info = zeroconf.get_service_info(type, name)
        properties = info.properties.items()
        id = self._get_property(properties, "id")

        devices = filter(lambda d: d.id == id, self._manager.devices)
        map(lambda d: self._manager.remove_device(d), devices)

    def _get_property(self, properties, name):
        property_list = next(filter(lambda p: p[0].decode() == name, properties))
        if property_list:
            return property_list[1].decode()
        else:
            return None


