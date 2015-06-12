# coding=utf-8
__author__ = 'timoveldt'

import zmq


def init():
    context = zmq.Context()
    xpub = context.socket(zmq.XPUB)
    xpub.bind("tcp://*:5559")
    xsub = context.socket(zmq.XSUB)
    xsub.bind("tcp://*:5560")

    poller = zmq.Poller()
    poller.register(xpub, zmq.POLLIN)
    poller.register(xsub, zmq.POLLIN)

    return context, xpub, xsub, poller


def main():
    """ main method """
    try:
        mainLoop()
    except KeyboardInterrupt as e:
        print "Done, closing down broker!", \
            "No more messages will be routed and the balloon can be considered dead if you see this."


def mainLoop():
    while True:
        print "###########################\n# (Re)starting...\n###########################"
        context, xpub, xsub, poller = init()
        print "Initialized"
        routeMessagesLoop(context, poller, xpub, xsub)


def routeMessagesLoop(context, poller, xpub, xsub):
    while True:
        try:
            events = dict(poller.poll(1000))
            if xpub in events:
                message = xpub.recv_multipart()
                print "[BROKER] subscription message: %r" % message[0]
                xsub.send_multipart(message)
            if xsub in events:
                message = xsub.recv_multipart()
                xpub.send_multipart(message)
        except KeyboardInterrupt as e:
            raise e
        except Exception as e:
            print "Got an exception, closing and restarting.", e
            try:
                xpub.close()
                xsub.close()
            except:
                print "Exception closing sockets, ignoring"
            try:
                context.term()
            except:
                print "Exception closing context, ignoring"
            break


if __name__ == "__main__":
    main()
