#!/usr/bin/env python

from telemetry_receiver import TelemetryReceiver
from sentence_parser import SentenceParser
from telemetry_uploader import TelemetryUploader


parser = SentenceParser()
uploader = TelemetryUploader(url = 'https://hab-henryfinlandia.c9users.io/backend/telemetry.php')

data = parser.parse("$$althab,9,18-30-31,0.55444,42.44431,500,5.3,3.0,-30.0,40,100,4.8*59B5")
response = uploader.upload(data)
print response.text