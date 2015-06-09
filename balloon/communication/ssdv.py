import subprocess
import os

class SSDV:
	'''Wrapper for command line ssdv tool (https://github.com/fsphil/ssdv)'''

	
	def encode(self, callsign, image_id, image_file):
		'''Encode JPEG image as SSDV packets. Returns an array of packages'''
		imagepackets = []
		output_file = "/tmp/output_%s.ssdv" % image_id
		subprocess.call(["ssdv", "-e", "-c", callsign, "-i", image_id, image_file, output_file])
		f = open(output_file, 'rb')
		packets = os.path.getsize(output_file) >> 8
		for i in range(packets):
			packet = f.read(256)
			imagepackets.append(packet)

		return imagepackets
