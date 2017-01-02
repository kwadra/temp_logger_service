#!/bin/sh

ZONE_FILE=/usr/share/zoneinfo/US/Arizona

timezone() {
	cd /etc/
	rm localtime
	ln -s $ZONE_FILE localtime
}

timezone

apt-get update
apt-get install python-smbus git
apt-get remove python-openssl
