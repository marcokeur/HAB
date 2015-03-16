__author__ = 'Tombruin'
from Adafruit_I2C import Adafruit_I2C
import time

BMP180_REG_CONTROL = 0xF4
BMP180_REG_RESULT = 0xF6
BMP180_COMMAND_PRESSURE3 = 0xF4

class BMP180:
    address = 0x77

    # Constructor
    def __init__(self):
        self.i2c = Adafruit_I2C(self.address)

    def readpressure(self):
        self.i2c.write8(BMP180_REG_CONTROL, BMP180_COMMAND_PRESSURE3)
        time.sleep(0.026)
        data = self.i2c.readList(BMP180_REG_RESULT, 3)
        pressure = (data[0] * 256.0) + data[1] + (data[2]/256.0)
        return pressure
