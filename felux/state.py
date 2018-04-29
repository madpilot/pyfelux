class State:
    def __init__(self, light, name):
        self._light = light
        self._name = name
        self._hue = 0
        self._saturation = 0
        self._value = 0
        self._brightness = 0
        self._on = False

    @property
    def name(self):
        return self._name

    @property
    def is_on(self):
        return self._on

    @property
    def brightness(self):
        return self._brightness

    @property
    def hue(self):
        return self._hue

    @property
    def saturation(self):
        return self._saturation

    @property
    def value(self):
        return self._value

    @property
    def light(self):
        return self._light

    def turn_on(self, duration = 0):
        self._light.on(duration)
        self._on = True

    def turn_off(self, duration = 0):
        self._light.off(duration)
        self._on = False

    def set_brightness(self, brightness, duration = 0):
        self._light.set_brightness(brightness, duration)
        self._brightness = brightness
        self._on = self._brightness != 0

    def set_hsv(self, hue, saturation, value, duration = 0):
        self._light.set_hsv(hue, saturation, value, duration)
        self._hue = hue
        self._saturation = saturation
        self._value = value

    def set_rgb(self, red, green, blue, duration = 0):
        self._light.set_rgb(red, green, blue, duration)

    def set_hue(self, hue, duration = 0):
        self._light.set_hue(hue, duration)
        self._hue = hue

    def set_saturation(self, saturation, duration = 0):
        self._light.set_saturation(saturation, duration)
        self._saturation = saturation

    def set_value(self, value, duration = 0):
        self._light.set_value(value, duration)
        self._value = value

    def update(self):
        self._light.get_state()

    def set_state(self, packet):
        decoded = self._light.decode(packet)

        if decoded != None:
            self._hue = decoded["hue"]
            self._saturation = decoded["saturation"]
            self._value = decoded["value"]
            self._brightness = decoded["brightness"]
