__author__ = 'timoveldt'

import zmq
import time


def main():
    context = zmq.Context()

    pub = context.socket(zmq.PUB)
    pub.connect("tcp://localhost:5560")

    topics = ['/sensor/gps/location', '/sensor/temperature/inside', '/sensor/temperature/outside', '/sensor/airpressure', '/sensor/humidity', '/sensor/gps/altitude']

    for n in range(1000):
        for topic in topics:
            msg = [topic, str(n)]
            pub.send_multipart(msg)
  	    time.sleep(0.1)
        time.sleep(0.2)
        print "Sent %d to topics" % n
    context.term()


if __name__ == "__main__":
    main()
