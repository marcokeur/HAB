__author__ = 'Tombruin'
from i2ctools_python import I2C
from HTU21D_Humidity import HTU21D
from MPL3115_Pressure import MPL3115
from BMP180_Pressure import BMP180
import time

print "Test"
device = I2C()

ID = device.readI2C(0x0C)
print ID

htu = HTU21D()
pressure = MPL3115()
pressure2 = BMP180();

while 1:
    print "pressure pascal:  {0}".format(pressure.readpressure())
    print "humidity:  {0}".format(htu.readHumidityData())
    print "pressure2:  {0}".format(pressure2.readpressure())
    time.sleep(1)