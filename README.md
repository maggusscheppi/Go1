# Go1 scripts and knowhow

## 1) Method and script for using USB-Modem on the raspberry to connect to internet
use addUSB-Modem.sh on the raspberry (192.168.123.161)<br>
Boot the Go1 and wait until it stands up.<br>
Plug in the USB-Modem.<br>
Check with <code>ip r</code> if the interface is up. Normally as soon as you see by indicator at the stick that the internet connection is done.<br>
Call<code>sudo addUSB-Modem.sh</code><br>
Check with <code>ip r</code> and a ping to a server in the internet.<br>


## 2) Turn of video/audio using processes on head nano
On the head nano (192.168.123.13):<br>
In some cases you may want to access cam or speaker of the head nano for your own purposes.<br>
You have to kill these processes: <br>
<code>pkill -f wsaudio</code><br>
<code>pkill -f point_cloud_nod</code><br>
<code>pkill -f example_point</code><br>

## 3) Stream video of frontcam with ffmpeg to rtsp-server
On the head nano (192.168.123.13):<br>
If the video device /dev/video1 (the frontcam) is available, try this:<br>
<code>ffmpeg -f video4linux2 -i /dev/video1 -vcodec libx264 -preset:v ultrafast -tune zerolatency -framerate 15 -f flv 'rtsp://yourRTSPserver/yourRTSPconnectionPoint'
</code>

## 4) Let the dog bark
On the head nano (192.168.123.13):<br>
If the audio device is available, try this:<br>
<code>aplay -D plughw:2,0 yourFavoriteWaveFile</code><br>

## 5) Change volume of loudspeaker
On the head nano (192.168.123.13):<br>
Change the volume to maximum:<br>
<code>amixer -c 2  set Speaker 100%</code>

## 6) Turn on internal wlan
use wifi_up.sh on the raspberry (192.168.123.161)<br>
Boot the Go1 and wait until it stands up.<br>
Call <code>sudo wifi_up.sh</code><br>
Check with <code>ip r</code> if the interface is up.<br>

## 7) Add your own web interface
You may want to create your own web interface next to the standard views from unitree.<br>
Here is a simple recipe with a sample page:<br>
Find the unitree web root: <code>./Unitree/autostart/webMonitor/dist/</code><br>
Create a folder with your index.html, e.g. <code>./Unitree/autostart/webMonitor/dist/myDog</code><br>
Take the sample files myDog/index.html, boxes.css, mqtt_util.js and mqttws31.js and place them there.<br>
Call http://192.168.12.1/myDog/<br><br>
<img src="https://github.com/maggusscheppi/Go1/blob/main/myDog_ScreenShot.jpg" width=200px;/>

## Ressources
### https://github.com/MAVProxyUser/YushuTechUnitreeGo1
### brain of my best friend




