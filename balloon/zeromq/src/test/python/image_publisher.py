__author__ = 'timoveldt'

import zmq
import time

from os import listdir
from os.path import isfile, join, abspath



def main():
    context = zmq.Context()

    pub = context.socket(zmq.PUB)
    pub.connect("tcp://localhost:5560")

    dir = "../../../../camera/imageprocessing/src/test/resources/hab-image-processing/"
    onlyfiles = [f for f in listdir(dir) if isfile(join(dir, f))]

    for file in onlyfiles:
        image_file = abspath(dir + file)
        pub.send_multipart(["/camera/picture/raw/location", image_file])
        time.sleep(0.25)
        print "Sent '%s' to topics" % image_file
    context.term()

if __name__ == "__main__":
    main()
