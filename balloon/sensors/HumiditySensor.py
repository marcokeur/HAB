__author__ = 'Tombruin'
import time
from Adafruit_I2C import Adafruit_I2C

# ===========================================================================
# HTU21D Class
# ===========================================================================

class HTU21D:
    i2c = None  # HTU21D Address
    address = 0x40

    # Commands
    TRIGGER_TEMP_MEASURE_HOLD = 0xE3
    TRIGGER_HUMD_MEASURE_HOLD = 0xE5
    READ_USER_REG = 0xE7

    # Constructor
    def __init__(self):
        self.i2c = Adafruit_I2C(self.address)

    def readUserRegister(self):
        # Read a byte
        value = self.i2c.readU8(self.READ_USER_REG)
        return value

    def readTemperatureData(self):
        # value[0], value[1]: Raw temperature data
        # value[2]: CRC
        value = self.i2c.readList(self.TRIGGER_TEMP_MEASURE_HOLD, 3)

        if not self.crc8check(value):
            return -255

        rawTempData = ( value[0] << 8 ) + value[1]

        # Zero out the status bits but keep them in place
        rawTempData = rawTempData & 0xFFFC;

        # Calculate the actual temperature
        actualTemp = -46.85 + (175.72 * rawTempData / 65536)

        return actualTemp

    def readHumidityData(self):
        # value[0], value[1]: Raw relative humidity data
        # value[2]: CRC
        value = self.i2c.readList(self.TRIGGER_HUMD_MEASURE_HOLD, 3)

        if not self.crc8check(value):
            return -255

        rawRHData = ( value[0] << 8 ) + value[1]

        # Zero out the status bits but keep them in place
        rawRHData = rawRHData & 0xFFFC;

        # Calculate the actual RH
        actualRH = -6 + (125.0 * rawRHData / 65536)

        return actualRH

    def crc8check(self, value):
        remainder = ( ( value[0] << 8 ) + value[1] ) << 8
        remainder |= value[2]

        # POLYNOMIAL = 0x0131 = x^8 + x^5 + x^4 + 1
        # divsor = 0x988000 is the 0x0131 polynomial shifted to farthest left of three bytes
        divsor = 0x988000

        for i in range(0, 16):
            if ( remainder & 1 << (23 - i) ):                remainder ^= divsor
            divsor = divsor >> 1

        if remainder == 0:
            return True
        else:
            return False