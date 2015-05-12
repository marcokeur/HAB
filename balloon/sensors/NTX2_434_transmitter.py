__author__ = 'EmielSchimmel'
import Adafruit_BBIO.UART as UART
import serial

# ===========================================================================
# The NXT2 communication controller will be connected to UART3.
# Because this UART is not containing a RX pin that is not required.
# The communication chips works best at an baud-rate of xx
# ===========================================================================


class NXT2_transmitter:

    # Constructor
    def __init__(self):
        UART.setup("UART5")
        self.serial3 = serial.Serial(   port = "/dev/ttyO5",
                                        baudrate = 300,
                                        stopbits = 2)
        self.serial3.open()

    def transmit(self, text):
         if self.serial3.isOpen():
             self.serial3.write(text)


    def close(self):
        self.serial3.close()
