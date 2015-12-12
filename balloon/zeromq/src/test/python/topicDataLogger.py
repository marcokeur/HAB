__author__ = 'nielshendriks'

import zmq
import time
import datetime

def main():
# Get first timestam
    ts = time.time()
    tsf = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

# Initialize ZeroMQ
    context = zmq.Context()
    sub = context.socket(zmq.SUB)
    sub.connect("tcp://localhost:5559")

# Create list of topics that we need to save to disk
    topics = ['/sensor/gps/location', '/sensor/temperature/inside', '/sensor/temperature/outside', '/sensor/airpressure', '/sensor/humidity', '/sensor/gps/altitude']

# Open log files for the topics and write initial timestamp and header to it.
    location = open("location.txt", 'a')
    temp_inside = open("temp_int.txt", 'a')
    temp_outside = open("temp_ext.txt", 'a')
    humidity = open("humidity.txt", 'a')
    altitude = open("altitude.txt", 'a')

    location.write("initial time: " + tsf + "\n")
    location.write("TimeStamp TopicName Value \n")
    
    temp_inside.write("initial time: " + tsf + "\n")
    temp_inside.write("TimeStamp TopicName Value \n")
   
    temp_outside.write("initial time: " + tsf + "\n")
    temp_outside.write("TimeStamp TopicName Value \n")
    
    humidity.write("initial time: " + tsf + "\n")
    humidity.write("TimeStamp TopicName Value \n")
    
    altitude.write("initial time: " + tsf + "\n")
    altitude.write("TimeStamp TopicName Value \n")

# Subscribe to the topics in the list.
    for topic in topics:
        sub.setsockopt(zmq.SUBSCRIBE, topic)
    
    print "subscribed to: %r" % topics
    while True:
        time.sleep(0.1)
        while True:
            if sub.poll(timeout=1000):
# Update timestamp
                msg = sub.recv_multipart()
		ts = time.time()
		tsf = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')		
		# Write message to logfiles
	    	if msg[0] == '/sensor/gps/location':
		    location.write(tsf + " " + msg[0] + "  " + msg[1] + "\n")
		    break
		
	    	if msg[0] == 'sensor/temperature/inside':
		    temp_inside.write(tsf + " " + msg[0] + "  " + msg[1] + "\n")
		    break

	    	if msg[0] == '/sensor/temperature/outside':
		    temp_outside.write(tsf + " " + msg[0] + "  " + msg[1] + "\n")
		    break

	    	if msg[0] == '/sensor/humidity':
		    humidity.write(tsf + " " + msg[0] + "  " + msg[1] + "\n")
		    break

	    	if msg[0] == '/sensor/gps/altitude':
		    altitude.write(tsf + " " + msg[0] + "  " + msg[1] + "\n")
		    break
            else:
                print "Breaking loop, got nothing..."
                break


if __name__ == "__main__":
    main()
