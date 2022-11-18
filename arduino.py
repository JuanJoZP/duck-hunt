import serial
import time


class Arduino:
    def __init__(self) -> None:
        self.ard = serial.Serial("COM3", 57600)

    def read(self):
        try:
            values = self.ard.readline().decode()
        except UnicodeDecodeError:
            return []
        return values.split(" ")
