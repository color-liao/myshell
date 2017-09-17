#!/bin/bash
######################
#xiaomi3 
#
#tcpdump capture wifi and gprs
#gprs
tcpdump -i netts0710mux10 -X -vv -w /sdcard/gprs-tcp.cap tcp
tcpdump -i netts0710mux10 -X -vv -w /sdcard/gprs-arp.cap arp
#wlan
tcpdump -i wlan0 -X -vv  -w /sdcard/wlan0-tcp.cap tcp

tcpdump -i wlan0 -X -vv -w /sdcard/wlan0-arp.cap arp

#netstat
netstat -pelot


#
#
#
#
#
#
