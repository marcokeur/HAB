#!/bin/sh
python BB-BONE-GPS-GPRS.py > log-gps.txt &
echo 'GPS sensor started'
python HTU21D_Humidity.py > log-hum.txt &
echo 'Humidity sensor started'
python MPL3115_Pressure.py > log-pres.txt &
echo 'Pressure sensor started'