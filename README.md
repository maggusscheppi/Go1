# Go1 scripts and knowhow

* [Connect the bot with LTE to the Internet](#method-and-script-for-using-usb-modem-on-the-raspberry-to-connect-to-internet)
* [Turn of video/audio using processes on head nano](#turn-of-videoaudio-using-processes-on-head-nano)
* [Stream video of frontcam with ffmpeg to rtsp-server](#stream-video-of-frontcam-with-ffmpeg-to-rtsp-server)
* [Let the dog bark](#let-the-dog-bark)
* [Change volume of loudspeaker](#change-volume-of-loudspeaker)
* [Turn on internal wlan](#turn-on-internal-wlan)
* [Add your own web interface](#add-your-own-web-interface)
* [Run your own scripts at boot](#run-your-own-scripts-at-boot)
* [Let the head led blink red when battery soc is 4](#let-the-head-led-blink-red-when-battery-soc-is-4)
* [Using mqtt-explorer on a host connected with Go1](#using-mqtt-explorer-on-a-host-connected-with-go1)
* [Network hints for working with the GO1 in LAN/WAN](#network-hints-for-working-with-the-go1)
* [Ressources](#ressources)

## Method and script for using USB-Modem on the raspberry to connect to internet
use addUSB-Modem.sh on the raspberry (192.168.123.161)<br>
Boot the Go1 and wait until it stands up.<br>
Plug in the USB-Modem.<br>
Check with <code>ip r</code> if the interface is up. Normally as soon as you see by indicator at the stick that the internet connection is done.<br>
Call<code>sudo addUSB-Modem.sh</code><br>
Check with <code>ip r</code> and a ping to a server in the internet.<br>


## Turn of video/audio using processes on head nano
On the head nano (192.168.123.13):<br>
In some cases you may want to access cam or speaker of the head nano for your own purposes.<br>
You have to kill these processes: <br>
<code>pkill -f wsaudio</code><br>
<code>pkill -f point_cloud_nod</code><br>
<code>pkill -f example_point</code><br>

## Stream video of frontcam with ffmpeg to rtsp-server
On the head nano (192.168.123.13):<br>
If the video device /dev/video1 (the frontcam) is available, try this:<br>
<code>ffmpeg -nostdin -f video4linux2 -i /dev/video1 -vcodec libx264 -preset:v ultrafast -tune zerolatency -framerate 15 -f flv 'rtsp://yourRTSPserver/yourRTSPconnectionPoint'
</code><br>
For running ffmpeg in the background -nostdin is important because per default ffmpeg expects a user to quit a task.

## Let the dog bark
On the head nano (192.168.123.13):<br>
If the audio device is available, try this:<br>
<code>aplay -D plughw:2,0 yourFavoriteWaveFile</code><br>

## Change volume of loudspeaker
On the head nano (192.168.123.13):<br>
Change the volume to maximum:<br>
<code>amixer -c 2  set Speaker 100%</code>

## Turn on internal wlan
use wifi_up.sh on the raspberry (192.168.123.161)<br>
Boot the Go1 and wait until it stands up.<br>
Call <code>sudo wifi_up.sh</code><br>
Check with <code>ip r</code> if the interface is up.<br>
Set your favorite home network by adding this at the end:<br>
<code>/etc/wpa_supplicant/wpa_supplicant.conf</code><br>
<code>network={
        ssid="yourSSID"
        psk="yourSecretPwD"
        key_mgmt=WPA-PSK
}</code>

## ... and bring head and nanos into the internet
after activating the internal lan you have to change standard routes on head and nanos to point to the raspi<br>
<code>
sudo ip route delete default 192.168.123.1
sudo ip route add default 192.168.123.161
</code>

## Add your own web interface
You may want to create your own web interface next to the standard views from unitree.<br>
Here is a simple recipe with a sample page:<br>
Find the unitree web root: <code>./Unitree/autostart/webMonitor/dist/</code><br>
Create a folder with your index.html, e.g. <code>./Unitree/autostart/webMonitor/dist/myDog</code><br>
Take the sample files and place them there.<br>
Call http://192.168.12.1/myDog/<br><br>
UI: <img src="https://github.com/maggusscheppi/Go1/blob/main/myDog_ScreenShot.jpg" width=200px;/> Commands: <img src="https://github.com/maggusscheppi/Go1/blob/main/myDog_ScreenShot_Commands.jpg" width=200px;/>

## Run your own scripts at boot
You may want to run your own scripts when the bot is starting.<br>
Unitree made some trick by using Lightdm to tell that user pi is an autologin user.<br>
Check then <code>\~/Unitree/autostart/.startlist.sh</code><br>
for a list of tasks to start.<br>
Each entry must be a name of a subfolder with a startscript.<br>
E.g.<br>
<code>~/Unitree/autostart/tunnel/tunnel.sh</code><br>

## Let the head led blink red when battery soc is 4
You may want to have an indicator that your dog wants to lay down before the energy is too low.<br>
Unfortunately the app does not warn you.<br>
With a python script that start with boot phase (see chapter 8) the battery state is monitored via mqtt.<br>
At soc (state of charge [100...0]) 3 the system will stop engines, the bot will lay down.<br>
This script warns you at soc = 3 with red led blinking.<br>
Copy the directory <code>\~/Unitree/autostart/diagnosis</code> to your raspi.<br>
Edit <code>.startlist.sh</code> and add at the end the line <code>diagnosis</code>.<br>
Now take the webpart <code>\~/Unitree/autostart/webMonitor/dist/diagnosis</code> and copy it also on your system.<br>
At next boot phase this script will run. You may check by <br>
<code>tail -f ~/Unitree/autostart/webMonitor/dist/diagnosis/bms.csv</code><br>
if data is stored or by accessing the web visualisation with <code>http://192.168.12.1/diagnosis</code><br>
Webview:<br>
<img src="https://github.com/maggusscheppi/Go1/blob/main/bms_view.jpg" width=300px;/>

## Using mqtt-explorer on a host connected with Go1
see <https://github.com/maggusscheppi/Go1/blob/main/go1_mqtt.pdf/>

## Network hints for working with the GO1
see <https://github.com/maggusscheppi/Go1/blob/main/GO1%20goes%20internet.pdf>

## Ressources
### https://github.com/MAVProxyUser/YushuTechUnitreeGo1
all about the dog

### https://github.com/Bin4ry/free-dog-sdk
get rid of sdk binaries

### https://gist.github.com/dbaldwin/b31835f87f16450a956cf3c89e15a289
Unitree Go1 Wireless Network Setup for Low Level Control with Windows and Docker




