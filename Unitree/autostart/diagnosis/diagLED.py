import paho.mqtt.client as mqtt
import time
import struct


def alertLED(r,g,b):
    mqttc = mqtt.Client()

    mqttc.connect("192.168.12.1", 1883, 60)

    mqttc.loop_start()

    infot = mqttc.publish("face_light/color", struct.pack('BBB',r,g,b), qos=2)
    time.sleep(1)
    infot = mqttc.publish("face_light/color", struct.pack('BBB',0,0,0), qos=2)
    time.sleep(1)
    mqttc.disconnect
    # time.sleep(1)
