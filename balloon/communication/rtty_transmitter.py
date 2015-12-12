#!/usr/bin/env python

from NTX2_Transmitter import NTX2_Transmitter
from ssdv import SSDV
from telemetry_packet import TelemetryPacket
from subscriber import Subscriber


TELEMETRY_EVERY = 4
BROKER_URL = "tcp://localhost:5559"

# Topics
GOOD_IMAGES_TOPIC = "/camera/picture/processed/location"
HUMIDITY_TOPIC = "/sensor/humidity"
GPS_TOPIC = "/sensor/gps/location"
TEMP_INTERNAL_TOPIC = "/sensor/temperature/inside"
TEMP_EXTENAL_TOPIC = "/sensor/temperature/outside"
AIR_PRESSURE_TOPIC = "/sensor/airpressure"

# NTX2 Configuration
NTX2_UART = "UART5"
NTX2_PORT = "/dev/ttyO5"


class RTTY_Transmitter:
	'''Transmitter for telemetry data'''
	
	def __init__(self):
		'''Default constructor. Initialize connection with NTX2 transmitter and subscribe to topics (images and telemetry)'''
		# Setup NTX2 transmitter
		self.transmitter = NTX2_Transmitter(uart=NTX2_UART, port=NTX2_PORT)
		self.transmitter.open()
		
		# Setup SSDV
		self.ssdv = SSDV()
		
		# Image receiver
		self.subscriber = Subscriber(BROKER_URL, [GOOD_IMAGES_TOPIC, HUMIDITY_TOPIC, GPS_TOPIC, TEMP_INTERNAL_TOPIC, TEMP_EXTENAL_TOPIC, AIR_PRESSURE_TOPIC])
		self.subscriber.start()
		
		self.image_id = 1
		self.sentence_id = 1


	def run(self):
		'''Read last good image, telemetry data and send with NTX2 transmitter'''
		while True:
			try:
				# Get latest image file from zeromq and generate SSDV packets
				image_file = self.subscriber.get(GOOD_IMAGES_TOPIC)
				if image_file != None:
					self.send_image_with_telemetry(image_file)
				else:
					self.send_telemetry()
			except Exception, e:
				raise e
		

	def send_telemetry(self):
		'''Get and send telemetry data'''

		# Get and build a telemetry packet
		telemetry = self._buildTelemetryPacket()
		
		# Generate telemetry sentence with CRC checksum
		sentence = telemetry.to_sentence()

		# Send telemetry packet
		self.transmitter.transmit(sentence)
		self.sentence_id += 1

		
		
	def send_image_with_telemetry(self, image_file):
		'''Send image with interleaved telemetry data'''
		i = 0
		image_packets = self.ssdv.encode(callsign='altran', image_id=str(self.image_id), image_file=image_file)
		for ssdv_packet in image_packets:
			if (i % TELEMETRY_EVERY) == 0:
				self.send_telemetry()
				
			self.transmitter.transmit(ssdv_packet)
			i += 1
			
		self.image_id += 1	
		
		
	def _buildTelemetryPacket(self):
		gps_data = self._getGPSdata()
		humidity = self._getHumidity()
		internal_temp = self._getInternalTemperature()
		external_temp = self._getExternalTemperature()
		air_pressure = self._getAirPressure()
		
		telemetry = TelemetryPacket(callsign='altran', 
		 							sentence_id=self.sentence_id, 
		 							lat=gps_data['lat'], 
		 							lon=gps_data['lon'], 
		 							alt=gps_data['alt'], 
		 							in_temp=internal_temp, 
		 							out_temp=external_temp, 
		 							humidity=humidity, 
		 							air_pressure=air_pressure)
		return telemetry
		
	def _getGPSdata(self):
		gps_string = self.subscriber.get(GPS_TOPIC)
		gps_data = { 'lat' : float(0.0000), 
					 'lon' : float(0.0000),
					 'alt' : int(0) }
		if gps_string != None:
			gps = gps_string.split(",")
			gps_data['lat'] = float(gps[0])
			gps_data['lon'] = float(gps[1])
			gps_data['alt'] = int(float(gps[2]))
		return gps_data
		
	
	def _getHumidity(self):
		humidity = self.subscriber.get(HUMIDITY_TOPIC)
		if humidity == None:
			humidity = 0
		return int(humidity)
		
	def _getInternalTemperature(self):
		temp = self.subscriber.get(TEMP_INTERNAL_TOPIC)
		if temp == None:
			temp = float(0.0)
		return float(temp)
		
	def _getExternalTemperature(self):
		temp = self.subscriber.get(TEMP_EXTENAL_TOPIC)
		if temp == None:
			temp = float(0.0)
		return float(temp)
		
	def _getAirPressure(self):
		air_pressure = self.subscriber.get(AIR_PRESSURE_TOPIC)
		if air_pressure == None:
			air_pressure = 0
		return int(air_pressure)


if __name__ == "__main__":
    rtty_transmitter = RTTY_Transmitter()
    rtty_transmitter.run()