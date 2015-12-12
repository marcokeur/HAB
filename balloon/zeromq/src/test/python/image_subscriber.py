__author__ = 'timoveldt'

import zmq
import time

topic = "/camera/picture/processed/location"

def main():
    context = zmq.Context()

    sub = context.socket(zmq.SUB)
    sub.connect("tcp://localhost:5559")
    sub.setsockopt(zmq.SUBSCRIBE, topic)
    print "subscribed to: %r" % topic
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
