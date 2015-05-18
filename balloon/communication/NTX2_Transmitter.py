import Adafruit_BBIO.UART as UART
import serial

'''Helper for NTX2 Transmitter connected on UART5 of the beaglebone'''
class NTX2_Transmitter:

    '''Constructor'''
    def __init__(self, uart, port):
        UART.setup(uart)
        self.serial = serial.Serial(port=port, baudrate=300, stopbits=2)
        
    '''Open the serial connection to the NTX2 transmitter'''
    def open(self):
        self.serial.open()

    '''Close the serial connection to the NTX2 transmitter'''
    def close(self):
        self.serial.close()

    '''Transmit text with the NTX2 transmitter'''
    def transmit(self, text):
        if self.serial.isOpen():
            self.serial.write(text)
