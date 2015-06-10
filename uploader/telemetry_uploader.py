import urllib

class TelemetryUploader:
	'''Upload telemetry sentences to server'''


	def __init__(self, url):
		'''Constructor'''
		self.url = url


	def upload(self, message):
		'''Upload telemetry data to the server'''
		query_string = urllib.urlencode(message)
		request = "%s?%s" % (self.url, query_string)
		print request
		#result = urllib.urlopen(request).read()
		#print result.to_s