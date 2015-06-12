__author__ = 'timoveldt'

def publisher(ctx):
    pub = ctx.socket(zmq.PUB)
    pub.connect(xsub_url)
    # pub.bind(xpub_url)
    for n in range(1000):
        for topic in "ABC":
            msg = [topic, str(n)]
            pub.send_multipart(msg)
        time.sleep(0.25)

