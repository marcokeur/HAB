#!/usr/bin/env python
import socket
import sys
import time
import os
import getopt

# unbuffered output
sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)
sys.stderr = os.fdopen(sys.stdout.fileno(), 'w', 0)

def main(argv):
	# parse command line arguments
	datafile = ''
	try:
		opts, args = getopt.getopt(argv, "hf:",["file="])
	except getopt.GetoptError:
		print "telemetry_server.py -f <file>"
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print 'telemetry_server.py -f <file>'
			sys.exit(0)
		elif opt in ("-f", "--file"):
			datafile = arg
	
	if datafile == '':
		print 'telemetry_server.py -f <file>'
		sys.exit(2)
	
	# Start TCP server		
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server_address = ('localhost', 7322)
	print ('starting server %s:%s' % server_address)
	sock.bind(server_address)

	# Listen for incoming connections
	sock.listen(1)

	while True:
		# Wait for a connection
		print 'waiting for a connection'
		connection, client_address = sock.accept()

		try:
			print ('connection from %s:%s' % client_address)

			# Receive the data in small chunks and retransmit it
			for line in open(datafile, 'r'):
				for c in line:
					connection.send(c)
					time.sleep(0.05)     
		except:
			print "connection closed"
		finally:
			# Clean up the connection
			connection.close()
			
			
if __name__ == "__main__":
    main(sys.argv[1:])

