__author__ = 'timoveldt'

import zmq
import time


def main():
    context = zmq.Context()

    pub = context.socket(zmq.PUB)
    pub.connect("tcp://localhost:5560")
    for n in range(1000):
        for topic in "ABC":
            msg = [topic, str(n)]
            pub.send_multipart(msg)
        time.sleep(0.25)
        print "Sent %d to topics" % n
    context.term()


if __name__ == "__main__":
    main()
