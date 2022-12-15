# Go1 scripts and knowhow

## 1) Method and script for using USB-Modem on the raspberry to connect to internet
use addUSB-Modem.sh on the raspberry (192.168.123.161)<br>
Boot the Go1 and wait until it stands up.<br>
Plug in the USB-Modem.<br>
Check with "ip r" if the interface is up. Normally as soon as you see by indicator at the stick that the internet connection is done.<br>
Call<br> 
    sudo addUSB-Modem.sh<br>
check with "ip r" and a ping to a server in the internet.<br>


## 2) Turn of video/audio using processes on head nano


## 3) stream video of frontcam with ffmpeg to rtsp-server
## 4) Turn on internal wlan
use wifi_up.sh on the raspberry (192.168.123.161)<br>
Boot the Go1 and wait until it stands up.<br>
Call<br> 
    sudo wifi_up.sh<br>
check with "ip r" if the interface is up.<br>

## 5) Ressources
you shall consider taking a deep dive into <br>
https://github.com/MAVProxyUser/YushuTechUnitreeGo1




