#!/bin/sh
python BB-BONE-GPS-GPRS.py &
echo 'GPS sensor started'
python HTU21D_Humidity.py &
echo 'Humidity sensor started'
python MPL3115_Pressure.py &
echo 'Pressure sensor started'