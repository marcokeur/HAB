__author__ = 'henry'


import os
from time import sleep
import json
import sys
import zmq

import time  
from watchdog.observers import Observer  
from watchdog.events import PatternMatchingEventHandler  

path = sys.argv[1] if len(sys.argv) > 1 else '.'

context = zmq.Context()
pub = context.socket(zmq.PUB)
pub.connect("tcp://localhost:5560")
pub.setsockopt(zmq.CONFLATE, 1)
    
class MyHandler(PatternMatchingEventHandler):
    patterns = ["*.jpg", "*.jpeg"]

    def process(self, event):
        # the file will be processed there
        print event.src_path, event.event_type  # print now only for degug
        
        msg = ["/camera/picture/raw/location", event.src_path]
        pub.send_multipart(msg)

    def on_created(self, event):
        self.process(event)

if __name__ == '__main__':
    observer = Observer()
    observer.schedule(MyHandler(), '/tmp/images')
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()