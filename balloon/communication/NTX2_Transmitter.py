import Adafruit_BBIO.UART as UART
import serial

class NTX2_Transmitter:
    '''Helper for NTX2 Transmitter connected on UART5 of the beaglebone'''

    def __init__(self, uart, port):
        '''Constructor'''
        UART.setup(uart)
        self.serial = serial.Serial(port=port, baudrate=300, stopbits=2)
        
    def open(self):
        '''Open the serial connection to the NTX2 transmitter'''
        self.serial.open()

    def close(self):
        '''Close the serial connection to the NTX2 transmitter'''
        self.serial.close()

    def transmit(self, text):
         '''Transmit text with the NTX2 transmitter'''
         if self.serial.isOpen():
            self.serial.write(text)
