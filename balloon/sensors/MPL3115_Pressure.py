__author__ = 'Tombruin'
from Adafruit_I2C import Adafruit_I2C
import time
import zmq

MPL3115_STATUS              =0x00
MPL3115_PRESSURE_DATA       =0x01
MPL3115_DR_STATUS           =0x06
MPL3115_DELTA_DATA          =0x07
MPL3115_WHO_AM_I            =0x0c
MPL3115_FIFO_STATUS         =0x0d
MPL3115_FIFO_DATA           =0x0e
MPL3115_FIFO_SETUP          =0x0e
MPL3115_TIME_DELAY          =0x10
MPL3115_SYS_MODE            =0x11
MPL3115_INT_SORCE           =0x12
MPL3115_PT_DATA_CFG         =0x13
MPL3115_BAR_IN_MSB          =0x14
MPL3115_P_ARLARM_MSB        =0x16
MPL3115_T_ARLARM            =0x18
MPL3115_P_ARLARM_WND_MSB    =0x19
MPL3115_T_ARLARM_WND        =0x1b
MPL3115_P_MIN_DATA          =0x1c
MPL3115_T_MIN_DATA          =0x1f
MPL3115_P_MAX_DATA          =0x21
MPL3115_T_MAX_DATA          =0x24
MPL3115_CTRL_REG1           =0x26
MPL3115_CTRL_REG2           =0x27
MPL3115_CTRL_REG3           =0x28
MPL3115_CTRL_REG4           =0x29
MPL3115_CTRL_REG5           =0x2a
MPL3115_OFFSET_P            =0x2b
MPL3115_OFFSET_T            =0x2c
MPL3115_OFFSET_H            =0x2d


class MPL3115:

    address = 0x60

    # Constructor
    def __init__(self):
        self.i2c = Adafruit_I2C(self.address)
        # Set to Barometer with an oversampling ratio = 16
        self.i2c.write8(MPL3115_CTRL_REG1, 0x20)
        # Enable Data Flags in PT_DATA_CFG
        self.i2c.write8(MPL3115_PT_DATA_CFG, 0x07)
        # Set Active (polling)
        self.i2c.write8(MPL3115_CTRL_REG1, 0x21)

    def readpressure(self):
        pressure = 0
        while 1:
            sensorstatus = self.i2c.readU8(MPL3115_STATUS)
            # check if pressure dat is ready [STATUS, 0x00 register]
            if sensorstatus & (1 << 2):
                OUT_P_MSB = self.i2c.readU8(0x01)
                OUT_P_CSB = self.i2c.readU8(0x02)
                OUT_P_LSB = self.i2c.readU8(0x03)

                pressure_whole = OUT_P_MSB << 16 | OUT_P_CSB << 8 | OUT_P_LSB
                pressure_whole >>= 6
                OUT_P_LSB &= 0b00110000
                OUT_P_LSB >>= 4
                pressure_decimal = OUT_P_LSB/4.0

                pressure = pressure_whole + pressure_decimal
                break
            else:
                # print "data not ready"
                pass
            time.sleep(0.05)
        return pressure
		
def main():	
	pres = MPL3115()
	context = zmq.Context()
	pub = context.socket(zmq.PUB)
	pub.connect("tcp://localhost:5560")
	while 1:
		humidity = pres.readpressure() / 100;
		print "Air pressure: %d mbar" % humidity
		msg = ["/sensor/airpressure", str(humidity)]
		pub.send_multipart(msg)
		time.sleep(1)
		
# Only run the code when executed by it self. and not imported			
if __name__ == "__main__":
    main()	