from datetime import datetime
import time
import crcmod

class TelemetryPacket:
	'''Class for telemetry data and converting it to a telemetry sentence with checksum'''

	def __init__(self, callsign, sentence_id, lat, lon, alt, in_temp, out_temp, humidity, air_pressure):
		'''Constructor (Note: timestamp will be generated by the constructor)'''
		self.callsign 		= callsign
		self.sentence_id	= sentence_id
		self.time 			= datetime.now()
		self.timestamp		= self.time.strftime("%H-%M-%S")
		self.latitude 		= lat
		self.longitude 		= lon
		self.altitude 		= alt
		self.internal_temp 	= in_temp
		self.external_temp 	= out_temp
		self.humidity 		= humidity
		self.air_pressure 	= air_pressure
		self.checksum 		= "0x00"


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

	def to_sentence(self):
		'''Generate telemetry sentence'''
		sentence = ("$$%s,%d,%s,%.5f,%.5f,%d,%.1f,%.1f,%d,%d" % (self.callsign, self.sentence_id, self.timestamp, self.latitude, self.longitude, self.altitude, self.internal_temp, self.external_temp, self.humidity, self.air_pressure))
		self.checksum = self.calculate_checksum(sentence)
		return ("%s*%s\n" % (sentence, self.checksum))

