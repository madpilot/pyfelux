import array
import socket

class API:
    COMMAND_OFF = 0x00
    COMMAND_ON = 0x01
    COMMAND_GET_STATE = 0x02
    COMMAND_SET_BRIGHTNESS = 0x03
    COMMAND_SET_HUE = 0x04
    COMMAND_SET_SATURATION = 0x05
    COMMAND_SET_VALUE = 0x06
    COMMAND_SET_HSV = 0x07
    COMMAND_SET_RGB = 0x08
    COMMAND_SET_ANIMATION = 0x09
    COMMAND_LIST_ANIMATIONS = 0x0A
    COMMAND_RAW = 0x0B

    ANIMATION_NONE = 0x00
    ANIMATION_RAW = 0x01
    ANIMATION_CUSTOM = 0x02

    PORT = 7269
    MAGIC = 0x48

    def __init__(self, address):
        self.address = address
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def off(self, duration):
        packet = self.build_packet(API.COMMAND_OFF)
        self.append_duration(packet, duration)
        self.send_packet(packet)

    def on(self, duration):
        packet = self.build_packet(API.COMMAND_ON)
        self.append_duration(packet, duration)
        self.send_packet(packet)

    def get_state(self):
        packet = self.build_packet(API.COMMAND_GET_STATE)
        self.send_packet(packet)

    def set_brightness(self, brightness, duration):
        packet = self.build_packet(API.COMMAND_SET_BRIGHTNESS)
        packet.append(self.__pack(brightness * 255 / 100) & 0xFF)
        self.append_duration(packet, duration)
        self.send_packet(packet)

    def set_hsv(self, hue, saturation, value, duration):
        packet = self.build_packet(API.COMMAND_SET_HSV)
        packet.append(self.__pack(hue * 255 / 365) & 0xFF)
        packet.append(self.__pack(saturation * 255 / 100) & 0xFF)
        packet.append(self.__pack(value * 255 / 100) & 0xFF)
        self.append_duration(packet, duration)
        self.send_packet(packet)

    def set_hue(self, hue, duration):
        packet = self.build_packet(API.COMMAND_SET_HUE)
        packet.append(self.__pack(hue * 255 / 365) & 0xFF)
        self.append_duration(packet, duration)
        self.send_packet(packet)

    def set_saturation(self, saturation, duration):
        packet = self.build_packet(API.COMMAND_SET_SATURATION)
        packet.append(self.__pack(saturation * 255 / 100) & 0xFF)
        self.append_duration(packet, duration)
        self.send_packet(packet)

    def set_value(self, value, duration):
        packet = self.build_packet(API.COMMAND_SET_VALUE)
        packet.append(self.__pack(value * 255 / 100) & 0xFF)
        self.append_duration(packet, duration)
        self.send_packet(packet)

    # Not supported yet
    # def set_animation(self, animation):
        # return None

    def build_packet(self, command):
        return bytearray([API.MAGIC, command])

    def append_duration(self, packet, duration):
        duration = self.__pack(duration)
        packet.extend([ duration >> 8 & 0xFF, duration & 0xFF ])

    def send_packet(self, packet):
        self.socket.sendto(packet, (self.address, API.PORT))

    def __pack(self, number):
        return round(number)

    def decode(self, packet):
        if len(packet) == 12 and packet[0] == API.MAGIC and packet[1] == 0xF0:
            return {
                "id" : int.from_bytes(packet[2:6], byteorder='little', signed=False),
                "hue": packet[6] * 365 / 255,
                "saturation": packet[7] * 100 / 255,
                "value": packet[8] * 100 / 255,
                "brightness": packet[9] * 100 / 255,
                "animation_type": packet[10],
                "animation_index": packet[11]
            }
        else:
            return None
