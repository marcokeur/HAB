import zmq
import time
import threading
import time

class Subscriber(threading.Thread):
	'''Zeromq subscriber'''

	def __init__(self, address, topics):
		'''Default constructor'''
		self.address = address
		self.context = None
		self.sub = None
		self.last_message = {}
		context = zmq.Context()
		self.sub = context.socket(zmq.SUB)
		self.sub.connect(self.address)
		self.isRunning = False
		for topic in topics:
			self.sub.setsockopt(zmq.SUBSCRIBE, topic)
			self.last_message[topic] = None
		threading.Thread.__init__ (self)
		
	def run(self):
		self.isRunning = True
		while self.isRunning:
			if self.sub.poll(timeout=500):
				data = self.sub.recv_multipart()
				if data != None and len(data) == 2:
					self.last_message[data[0]] = data[1]
			else:
				time.sleep(1)
				
	def get(self, topic):
		return self.last_message[topic]
		
	def stop(self):
		self.isRunning = False
	