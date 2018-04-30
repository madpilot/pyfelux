import felux

class Device:
    def __init__(self, id, ip_address, host_name, device_name, number_of_leds):
        self._id = id
        self._ip_address = ip_address
        self._host_name = host_name
        self._device_name = device_name
        self._number_of_leds = number_of_leds

        api = felux.API(self.ip_address)
        self._state = felux.State(api, self.device_name)

    def copy(self, device):
        self._ip_address = device.ip_address
        self._host_name = device.host_name
        self._device_name = device.device_name
        self._number_of_leds = device.number_of_leds

        api = felux.API(self.ip_address)
        self._state.update_light(api)

    def __repr__(self):
        return "Device " + self._id + " {ip_address=" + self._ip_address + ",host_name=" + self._host_name + ",device_name=" + self._device_name + ",leds=" + str(self._number_of_leds)

    @property
    def id(self):
        return self._id

    @property
    def ip_address(self):
        return self._ip_address

    @property
    def host_name(self):
        return self._host_name

    @property
    def device_name(self):
        return self._device_name

    @property
    def number_of_leds(self):
        return self._number_of_leds

    @property
    def is_on(self):
        return self_state.is_on

    @property
    def brightness(self):
        return self._state.brightness

    @property
    def hue(self):
        return self._state.hue

    @property
    def saturation(self):
        return self._state.saturation

    @property
    def value(self):
        return self._state.value

    @property
    def light(self):
        return self._state.light

    def turn_on(self, duration = 0):
        self._state.turn_on(duration)

    def turn_off(self, duration = 0):
        self._state.turn_off(duration)

    def set_brightness(self, brightness, duration = 0):
        self._state.set_brightness(brightness, duration)

    def set_hsv(self, hue, saturation, value, duration = 0):
        self._state.set_hsv(hue, saturation, value, duration)

    def set_rgb(self, red, green, blue, duration = 0):
        self._state.set_rgb(red, green, blue, duration)

    def set_hue(self, hue, duration = 0):
        self._state.set_hue(hue, duration)

    def set_saturation(self, saturation, duration = 0):
        self._state.set_saturation(saturation, duration)

    def set_value(self, value, duration = 0):
        self._state.set_value(value, duration)

    def update(self):
        self._state.update()

    def set_state(self, state):
        self._state.set_state(state)
