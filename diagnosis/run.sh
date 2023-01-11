#!/bin/bash
myNow=$(date +"%T")
eval echo "$myNow [diagnosis] starting... " $toStartlog
sleep 30
myNow=$(date +"%T")
eval echo "$myNow [diagnosis] starting the monitor" $toStartlog
python /home/pi/Unitree/autostart/diagnosis/snif_bms.py

