import zmq
import time
import threading

class Subscriber(threading.Thread):
	'''Zeromq subscriber'''

	def __init__(self, address, topic):
		'''Default constructor'''
		self.address = address
		self.topic = topic
		self.context = None
		self.sub = None
		self.last_message = None
		threading.Thread.__init__ (self)
		
	def run(self):
		while True:
			data = self._poll(100)
			if data != None: 
				self.last_message = data
			
	def get(self):
		return self.last_message

	def connect(self):
		'''Connect the zeromq subscriber'''
		context = zmq.Context()
		self.sub = context.socket(zmq.SUB)
		self.sub.connect(self.address)
		self.sub.setsockopt(zmq.SUBSCRIBE, self.topic)

	def _poll(self, timeout):
		if self.sub.poll(timeout=timeout):
			data = self.sub.recv_multipart()
			if data != None and len(data) == 2:
				return data[1]
			else:
				return None
		else:
			return None
