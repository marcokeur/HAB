#!/bin/sh


CAMERA_GOPRO_APP="/home/ubuntu/workspace/balloon/camera/camerainterface/src/GoProInterface.py"

CAMERA_PID_FILE="/tmp/camera.pid"

CAMERA_PID=$(cat $CAMERA_PID_FILE)

echo "CAMERA PID " $CAMERA_PID



while true; do 

    #echo $CAMERA_PID

    echo CAMERA_PID_ACTIVE=`ps aux | grep $CAMERA_PID`


    #echo "sleep"
    sleep 4
done