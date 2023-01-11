import paho.mqtt.client as mqtt
import binascii
import struct
import os
from datetime import datetime
from diagLED import alertLED

path='/home/pi/Unitree/autostart/webMonitor/dist/diagnosis'
filename='bms.csv'
pathFilename=path+'/'+filename


def on_connect(client, userdata, flags, rc):
    # print("Connected with result code {0}".format(str(rc)))
    client.subscribe("bms/state")


def on_message(client, userdata, msg):
    # print("Message received-> " + msg.topic)
    # print("Message received-> " + msg.payload)
    myByteArray = bytearray(msg.payload)
    [ver0,ver1,status,soc,current,cycle,temp0,temp1,temp2,temp3,cellV0,cellV1,cellV2,cellV3,cellV4,cellV5,cellV6,cellV7,cellV8,cellV9] = struct.unpack('BBBBiHBBBBHHHHHHHHHH',msg.payload)
    # print("BMS version -> " + str(ver0) + "." + str(ver1))
    # print("BMS status  -> " + str(status))
    # print("BMS SOC     -> " + str(soc) + "%")
    # print("BMS Current -> " + str(current) + "mA")
    # print("BMS Cycles  -> " + str(cycle))
    # print("BMS BAT1    -> " + str(temp0) + u"\xb0" + "C")
    # print("BMS BAT2    -> " + str(temp1) + u"\xb0" + "C")
    # print("BMS MOS     -> " + str(temp2) + u"\xb0" + "C")
    # print("BMS RES     -> " + str(temp3) + u"\xb0" + "C")
    myCellVoltage = cellV0 + cellV1 + cellV2  + cellV3 + cellV4 + cellV5 + cellV6 + cellV7 + cellV8 + cellV9
    # print("BMS Voltage -> " + str(myCellVoltage) + "mV")
    # write data into a log file
    myLogFile = open(pathFilename, "a")
    today = datetime.now()
    # write all available data out into csv
    myLogFile.write(today.isoformat() + "," + str(soc)+","+str(myCellVoltage/1000)+","+str(cycle)+","+str(temp0)+","+str(temp1)+","+str(temp2)+","+str(temp3)+","+str(cellV0)+","+str(cellV1)+","+str(cellV2)+","+str(cellV3)+","+str(cellV4)+","+str(cellV5)+","+str(cellV6)+","+str(cellV7)+","+str(cellV8)+","+str(cellV9)+"\n")
    myLogFile.close
    # now make a decicion to set an alarm
    if 4 == soc:
        alertLED(255,0,0)


# first check, if already a bms.csv exists. if so, rename it. We will create a new one
isExist = os.path.exists(pathFilename)
if isExist:
    # print("file exists")
    # rename that file with a prefix of its last modification date
    m_time = os.path.getmtime(pathFilename)
    os.rename(pathFilename, path+'/'+datetime.fromtimestamp(m_time).isoformat()+'.'+filename)

myLogFile = open(pathFilename, "w")
myLogFile.write("time,SOC[%],Voltage[V],Current[mA],Cycle,temp0[C],temp1[C],temp2[C],temp3[C],cellV0[C],cellV1[C],cellV2[C],cellV3[C],cellV4[C],cellV5[C],cellV6[C],cellV7[C],cellV8[C],cellV9[C]\n")
myLogFile.close()

# print("connecting mqtt client")
client = mqtt.Client("Stick Data")
client.on_connect = on_connect
client.on_message = on_message
client.connect("192.168.12.1", 1883, 60)
try:
    client.loop_forever()
except:
    client.disconnect()
