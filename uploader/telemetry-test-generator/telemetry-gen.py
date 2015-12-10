#!/usr/bin/env python
from datetime import datetime
import time
from datetime import timedelta
import crcmod

#$$CALLSIGN,sentence_id,time,latitude,longitude,altitude,speed,internal_temperature,external_temperature,humidity,air_pressure,ascent_rate*CHECKSUM\n

'''Generator for HAB telemetry test data'''
class Generator:

	'''Set initial values for telemetry data'''
	def __init__(self):
		self.callsign 		= "althab"
		self.sentence_id	= 1
		self.time 			= datetime.now()
		self.timestamp		= "16-01-52"
		self.latitude 		= 0.55444
		self.longitude 		= 42.44431
		self.altitude 		= 500
		self.speed 			= 5.3
		self.internal_temp 	= 3.0
		self.external_temp 	= -30.0
		self.humidity 		= 40
		self.air_pressure 	= 100
		self.ascent_rate 	= 4.8
		self.checksum 		= "0x22"


	'''Generate the telemetry string without checksum'''
	def generate_telemetry_string(self):
		return ("$$%s,%d,%s,%.5f,%.5f,%d,%.1f,%.1f,%.1f,%d,%d,%.1f" % (self.callsign, self.sentence_id, self.timestamp, self.latitude, self.longitude, self.altitude, self.speed, self.internal_temp, self.external_temp, self.humidity, self.air_pressure,self.ascent_rate))

		
	def calculate_checksum(self, data):
		"""
		Calculate the CRC16 CCITT checksum of *data*.
		(CRC16 CCITT: start 0xFFFF, poly 0x1021)
		Returns an upper case, zero-filled hex string with no prefix such as
		``0A1B``.
		>>> crc16_ccitt("hello,world")
		'E408'
		"""
		data = data[2:] # Ignore start tokens ($$)
		crc16 = crcmod.predefined.mkCrcFun('crc-ccitt-false')
		return hex(crc16(data))[2:].upper().zfill(4)

	


	'''Increment the time by 30 seconds for testing'''
	def updateTime(self):
		self.time = self.time + timedelta(seconds=30)
		self.timestamp = self.time.strftime("%H-%M-%S")


## GENERATE SOME TEST DATA
generator = Generator()

for i in range(0, 100):
	generator.sentence_id = i
	generator.updateTime()
	telemetry_string = generator.generate_telemetry_string()
	checksum = generator.calculate_checksum(telemetry_string)
	print ("%s*%s" % (telemetry_string, checksum))
