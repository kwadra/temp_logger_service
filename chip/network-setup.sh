#!/bin/sh

ssid=$1
password=$2
nmcli device wifi connect "${ssid}" password ${password} ifname wlan0
