__author__ = 'henry'

import zmq
import random
import sys
import time

port = "5556"
if len(sys.argv) > 1:
    port =  sys.argv[1]
    int(port)

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:%s" % port)


while True:
    #topic = "/sensor/gps/altitude"
    topic = random.randrange(9999,10005)
    messagedata = random.randrange(1,2150)
    print "%d %d" % (topic, messagedata)
    socket.send("%d %d" % (topic, messagedata))
    time.sleep(1)