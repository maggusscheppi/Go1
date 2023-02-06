#!/bin/bash

# kill all unneccessary proesses to enhance performance and these who got the cam in access
pkill -f wsaudio
pkill -f point_cloud_nod
pkill -f example_point
aplay -D plughw:2,0 bark.wav
