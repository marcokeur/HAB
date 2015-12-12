import zmq
import time
import threading

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
		for topic in topics:
			self.sub.setsockopt(zmq.SUBSCRIBE, topic)
		threading.Thread.__init__ (self)
		
	def run(self):
		while True:
			data = self._poll(100)
			if data != None: 
				self.last_message[data[0]] = data[1]
			
	def get(self, topic):
		return self.last_message[topic]

	def _poll(self, timeout):
		if self.sub.poll(timeout=timeout):
			data = self.sub.recv_multipart()
			if data != None and len(data) == 2:
				return data
			else:
				return None
		else:
			return None
