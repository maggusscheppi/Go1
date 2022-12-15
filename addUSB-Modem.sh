#!/bin/bash

# wait for usb0 in ip r

# immediately stop the dchp deamon. Otherwise routes will be discovered in cycles.
sudo service dhcpcd stop

# delete existing default routes for eth0 and wlan0
ip r d default via 192.168.123.1
ip r d default via 192.168.12.1

# allow forwarding on the raspberri
sysctl -w net.ipv4.ip_forward=1

# masquerade nano traffic behind raspberry traffic for GSM
iptables -t nat -A POSTROUTING -o usb0 -j MASQUERADE
iptables -A FORWARD -i eth0 -o usb0 -j ACCEPT
iptables -A FORWARD -i usb0 -o eth0 -m state --state RELATED,ESTABLISHED -j ACCEPT

# now set a defautl route to the  raspberry on each nano, which shall do someting in the internet
