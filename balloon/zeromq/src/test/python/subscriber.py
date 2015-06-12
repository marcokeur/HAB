__author__ = 'timoveldt'

import zmq
import time


def main():
    context = zmq.Context()

    sub = context.socket(zmq.SUB)
    sub.connect("tcp://localhost:5559")
    topics = 'AC'
    for topic in topics:
        sub.setsockopt(zmq.SUBSCRIBE, topic)
    print "subscribed to: %r" % topics
    while True:
        time.sleep(0.3)
        while True:
            if sub.poll(timeout=1000):
                print "received", sub.recv_multipart()
            else:
                print "Breaking loop, got nothing..."
                break


if __name__ == "__main__":
    main()
