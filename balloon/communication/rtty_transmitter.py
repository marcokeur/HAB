#!/usr/bin/env python

from NTX2_Transmitter import NTX2_Transmitter
from ssdv import SSDV
from telemetry_packet import TelemetryPacket

# Setup NTX2 transmitter
NTX2_Transmitter transmitter = NTX2_Transmitter(uart="UART5", port="/dev/ttyO5")
transmitter.open()

# Setup SSDV
SSDV ssdv = SSDV()
image_id = 1
TELEMETRY_EVERY=4

while 1:
	try:
		# Get latest image file from zeromq and generate SSDV packets
		image_file = "test_image.jpeg"
		image_packets = ssdv.encode(callsign='altran', image_id=image_id, image_file)
		image_id += 1

		# Transmit 1 telemetry packet for every 4 SSDV packets 
		i = 0
		for packet in image_packets:
			if (i % TELEMETRY_EVERY) == 0:
				# Get sensor values from zeromq
				# Get gps data from zeromq
				# Extract latitude, longitude, altitude
				# Calculate speed and ascent_rate

				# Create TelemetryPacket
				TelemetryPacket telemetry = TelemetryPacket(callsign='altran', 
															sentence_id='1', 
															lat=0.0, 
															lon=0.0, 
															alt=0, 
															speed=0, 
															in_temp=0.0, 
															out_temp=0.0, 
															humidity=100, 
															air_pressure=100, 
															ascent_rate=5.0)
				
				# Generate telemetry sentence with CRC checksum
				sentence = telemetry.to_sentence()

				# Send telemetry packet
				transmitter.transmit(sentence)

			transmitter.transmit(packet)
			i += 1
	except Exception:
		pass # Ignore exceptions

transmitter.close()
