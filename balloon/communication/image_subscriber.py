import zmq
import time

class ImageSubscriber:
	'''Zeromq subscriber for the images queue'''

	def __init__(self, address, topic):
		'''Default constructor'''
		self.address = address
		self.topic = topic
		self.context = None
		self.sub = None

	def connect(self):
		'''Connect the zeromq subscriber'''
		context = zmq.Context()
	    self.sub = context.socket(zmq.SUB)
	    self.sub.connect(self.address)
	    self.sub.setsockopt(zmq.SUBSCRIBE, self.topic)
	    self.sub.setsockopt(zmq.CONFLATE, 1)

	def poll(self, timeout):
		if sub.poll(timeout=timeout):
			return sub.recv_multipart()
		else:
			return None
