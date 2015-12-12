import requests

class TelemetryUploader:
	'''Upload telemetry sentences to server'''


	def __init__(self, url):
		'''Constructor'''
		self.url = url


	def upload(self, message):
		post_response = requests.post(url=self.url, data=message)
		return post_response
		