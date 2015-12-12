
class SentenceParser:
	'''Telemetry sentence parser'''

	def parse(self, sentence):
		'''Parse telemetry sentence and return TelemetryPacket'''
		telemetry = {}
		a = sentence.split('*')
		telemetry_string = a[0]
		telemetry_data = telemetry_string[2:]
		data = telemetry_data.split(',')
		if data is None:
			return None

		telemetry['callsign'] 				= data[0]
		telemetry['sentence_id'] 			= data[1]
		telemetry['timestamp_balloon'] 		= data[2]
		telemetry['latitude'] 				= data[3]
		telemetry['longitude'] 				= data[4]
		telemetry['altitude'] 				= data[5]
		telemetry['internal_temp'] 			= data[6]
		telemetry['external_temp'] 			= data[7]
		telemetry['humidity'] 				= data[8]
		telemetry['air_pressure'] 			= data[9]

		return telemetry
