__author__ = 'henry'


import os
from time import sleep
import json



import urllib2

gopro_ip = "10.5.5.9"
gopro_ip = "localhost"
gopro_streaming_port = "8554"
ffmpegCommand = "ffmpeg -f mpegts -i \"udp://{0}:{1}?fifo_size=10000\" -vframes 1 test.jpeg".format(gopro_ip,gopro_streaming_port)


print ffmpegCommand
os.system("ls -lah")



json_data = u'{"answer": [42.2], "abs": 42}'
data = json.loads(json_data)






class GoProInterface :
    streaming_timeout = 1;
    url_base = "http://{0}/".format(gopro_ip)
    url_stream_restart = "gp/gpExec?p1=gpStreamA9&c1=restart"
    url_stream_start = "gp/gpExec?p1=gpStreamA9&c1=start"
    url_stream_stop = "gp/gpExec?p1=gpStreamA9&c1=stop"

    def __init__(self):
        print self

    def send_command(self, cmd):
        url = self.url_base + cmd.format("###")
        #print url
        try:
            result = urllib2.urlopen(url, timeout=2).read()
        except IOError, e:
            print 'Failed to open "%s".' % url

    def startStreaming(self, seconds):
        remaining = seconds;
        self.send_command(self.url_stream_start)

        while remaining > 0:

            self.send_heartbeat()
            remaining -= 1
        self.send_command(self.url_stream_stop)

    def send_heartbeat(self):
        self.send_command(self.url_stream_restart)
        sleep(self.streaming_timeout)

GoPro = GoProInterface()
GoPro.startStreaming(3)



