class Device:
    def __init__(self, id, ip_address, host_name, device_name, number_of_leds):
        self._id = id
        self._ip_address = ip_address
        self._host_name = host_name
        self._device_name = device_name
        self._number_of_leds = number_of_leds

        api = API(self.ip_address)
        self._state = State(api, self.device_name)

    @property
    def id(self):
        return _id

    @property
    def ip_address(self):
        return _ip_address

    @propery
    def host_name(self):
        return _host_name

    @property
    def device_name(self):
        return _device_name

    @propery
    def number_of_leds(self):
        return _number_of_leds

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
