# coding=utf-8
__author__ = 'timoveldt'

import zmq

def main():
    """ main method """

    context = zmq.Context()
    xpub = context.socket(zmq.XPUB)
    xpub.bind("tcp://*:5559")
    xsub = context.socket(zmq.XSUB)
    xsub.bind("tcp://*:5560")

    poller = zmq.Poller()
    poller.register(xpub, zmq.POLLIN)
    poller.register(xsub, zmq.POLLIN)
    while True:
        events = dict(poller.poll(1000))
        if xpub in events:
            message = xpub.recv_multipart()
            print "[BROKER] subscription message: %r" % message[0]
            xsub.send_multipart(message)
        if xsub in events:
            message = xsub.recv_multipart()
            # print "publishing message: %r" % message
            xpub.send_multipart(message)

    # We never get here…
    xpub.close()
    xsub.close()
    context.term()

if __name__ == "__main__":
    main()
