from threading import Thread

__author__ = 'timoveldt'

import zmq
import time

def publisher(context):
    pub = context.socket(zmq.PUB)
    pub.connect("tcp://localhost:5560")
    for n in range(1000,2000):
        msg = ["D", str(n)]
        pub.send_multipart(msg)
        time.sleep(0.25)

def subscriber(context):
    sub = context.socket(zmq.SUB)
    sub.connect("tcp://localhost:5559")
    topics = "BD"
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

def main():
    ctx = zmq.Context()
    threads = [ Thread(target=f, args=(ctx,)) for f in (publisher, subscriber) ]
    [ t.start() for t in threads ]
    while True:
        try:
            time.sleep(1)
        except KeyboardInterrupt:
            break
    print "terminating"
    ctx.term()
    [ t.join() for t in threads ]
    print "terminated"

if __name__ == '__main__':
    main()
