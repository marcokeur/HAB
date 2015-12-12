#!/usr/bin/env python

from NTX2_Transmitter import NTX2_Transmitter
from ssdv import SSDV
from telemetry_packet import TelemetryPacket
from subscriber import Subscriber


TELEMETRY_EVERY = 4
BROKER_URL = "tcp://localhost:5559"
GOOD_IMAGES_TOPIC = "/camera/picture/processed/location"
TELEMETRY_TOPIC = "/communication/rf"
HUMIDITY_TOPIC = "/sensor/humidity"
GPS_TOPIC = "/sensor/gps/location"
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
		self.imageSubscriber = Subscriber(BROKER_URL, GOOD_IMAGES_TOPIC)
		self.imageSubscriber.connect()
		self.imageSubscriber.start()
		
		# Telemetry receiver 
		self.telemetrySubscriber = Subscriber(BROKER_URL, TELEMETRY_TOPIC)
		self.telemetrySubscriber.connect()
		self.telemetrySubscriber.start()
		
		# Humidity subscription
		self.gpsSubscriber = Subscriber(BROKER_URL, GPS_TOPIC)
		self.gpsSubscriber.connect()
		self.gpsSubscriber.start()
		
		self.image_id = 1
		self.sentence_id = 1


	def run(self):
		'''Read last good image, telemetry data and send with NTX2 transmitter'''

		while True:
			# Get latest image file from zeromq and generate SSDV packets
			image_file = self.imageSubscriber.get()
			if image_file != None:
				self.send_image_with_telemetry(image_file)
			else:
				self.send_telemetry()
		

	def send_telemetry(self):
		'''Get and send telemetry data'''
		# Get latest telemetry data
		#data = self.telemetrySubscriber.get()
		#if data == None:
		#	return
		
		# TODO: build TelemetryPacket from data
		
		lat = 0.0
		lon = 0.0
		alt = 0
		gps_string = self.gpsSubscriber.get()
		if gps_string != None:
			gps = gps_string.split(",")
			lat = float(gps[0])
			lon = float(gps[1])
			alt = int(float(gps[2]))
		
		# Create TelemetryPacket
		telemetry = TelemetryPacket(callsign='altran', 
									sentence_id=self.sentence_id, 
									lat=lat, 
									lon=lon, 
									alt=alt, 
									in_temp=0.0, 
									out_temp=0.0, 
									humidity=0, 
									air_pressure=100)
		
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


if __name__ == "__main__":
    rtty_transmitter = RTTY_Transmitter()
    rtty_transmitter.run()