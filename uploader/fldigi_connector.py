import Queue
from telemetry_receiver import TelemetryReceiver
from sentence_parser import SentenceParser
from telemetry_uploader import TelemetryUploader

# Queue for telemetry sentences
telemetryQueue = Queue.Queue()

# Connect to fldigi and start parsing telemetry sentences
receiver = TelemetryReceiver('localhost', 7322, telemetryQueue)
receiver.connect()
receiver.start()

parser = SentenceParser()
uploader = TelemetryUploader(url = 'http://localhost/telemetry/upload.php')

# Parse telemetry sentences and upload to server
while receiver.connected:
	sentence = telemetryQueue.get()
	message = parser.parse(sentence)
	uploader.upload(message)