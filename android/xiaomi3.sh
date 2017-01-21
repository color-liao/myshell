#!/bin/bash
######################
#mobile gprs
tcpdump -i netts0710mux10 -X -vv -w /sdcard/log.cap tcp
tcpdump -i netts0710mux10 -X -vv -w /sdcard/log.cap arp
#wirless
tcpdump -i wlan0 -X -vv  -w /sdcard/wlan0-tcp.cap tcp

tcpdump -i wlan0 -X -vv -w /sdcard/wlan0-arp.cap arp 
