import socket
import sys
import crc16
import threading
import Queue

class TelemetryReceiver(threading.Thread):
	'''
		Telemetry receiver connects to dl-fldigi, 
		rebuilds telemetry sentences and checks the CRC checksum
	'''

	def __init__(self, host, port, queue):
		'''Constructor'''
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.server_address = (host, port)
		self.connected = False
		self.queue = queue
		threading.Thread.__init__ (self)
		
	def connect(self):
		'''Connect to DL-Fldigi rx socket'''
		print 'connecting to %s port %s' % self.server_address
		self.sock.connect(self.server_address)
		self.connected = True

	def disconnect(self):
		'''Disconnect socket'''
		self.sock.close()
		self.connected = False

	def isConnected(self):
		return self.connected

	def run(self):
		'''Receive telemetry data'''
		telemetry_sentence = ""
		prev = ''
		start_detected = False
		end_detected = False

		while self.connected == True:
			# Read character from socket
			cur = self.sock.recv(8)

			# Wait for sentence header
			if not start_detected:
				start_detected = (cur == '$' and prev == '$')
				telemetry_sentence = "$$"

			# Read telemetry data while start detected but no end
			elif start_detected and not end_detected:
				end_detected = (cur == '\n')
				if not end_detected:
					telemetry_sentence += cur

			# If start and end are detected, check the CRC checksum		
			if start_detected and end_detected:
				a = telemetry_sentence.split('*')
				if len(a) == 2:
					crc = hex(crc16.crc16xmodem(a[0], 0xffff))
					received_crc = hex(int(a[1], 16))
					crc_valid = (crc == received_crc)
					if crc_valid:
						self.queue.put(telemetry_sentence)
					else:
						print telemetry_sentence
						print >>sys.stderr, 'checksum error'
			# Store cur in prev	
			prev = cur