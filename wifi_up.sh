#!/bin/bash

# allow forwarding on the raspberri
sysctl -w net.ipv4.ip_forward=1

# masquerade nano traffic behind raspberry traffic for GSM
iptables -t nat -A POSTROUTING -o wlan2 -j MASQUERADE
iptables -A FORWARD -i eth0 -o wlan2 -j ACCEPT
iptables -A FORWARD -i wlan2 -o eth0 -m state --state RELATED,ESTABLISHED -j ACCEPT

ifconfig wlan2 up

# delete existing default routes for eth0 and wlan0
ip r d default via 192.168.123.1
ip r d default via 192.168.12.1
