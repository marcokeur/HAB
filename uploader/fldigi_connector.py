#!/usr/bin/env python

import Queue
import sys
import os
from telemetry_receiver import TelemetryReceiver
from sentence_parser import SentenceParser
from telemetry_uploader import TelemetryUploader

sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)
sys.stderr = os.fdopen(sys.stdout.fileno(), 'w', 0)


# Queue for telemetry sentences
telemetryQueue = Queue.Queue()

# Connect to fldigi and start parsing telemetry sentences
receiver = TelemetryReceiver('localhost', 7322, telemetryQueue)
receiver.connect()
receiver.start()

parser = SentenceParser()
uploader = TelemetryUploader(url = 'https://hab-tomregelink.c9users.io/website/backend/telemetry.php')

# Parse telemetry sentences and upload to server
while receiver.connected:
	sentence = telemetryQueue.get()
	message = parser.parse(sentence)
	uploader.upload(message)
