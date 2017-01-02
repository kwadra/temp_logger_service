#!/usr/bin/env python 
import smbus
import time
from datetime import datetime
import requests

BUS_NUMBER=1 
DEVICE_ADDR=0x44
SHT31_MEAS_HIGHREP_STRETCH = 0x2C06
SHT31_MEAS_MEDREP_STRETCH  = 0x2C0D
SHT31_MEAS_LOWREP_STRETCH  = 0x2C10
SHT31_MEAS_HIGHREP        =  0x2400
SHT31_MEAS_MEDREP         =  0x240B
SHT31_MEAS_LOWREP         = 0x2416
SHT31_READSTATUS          = 0xF32D
SHT31_CLEARSTATUS         = 0x3041
SHT31_SOFTRESET           = 0x30A2
SHT31_HEATEREN            = 0x306D
SHT31_HEATERDIS           = 0x3066

# Get I2C bus
bus = smbus.SMBus(BUS_NUMBER)
 
# SHT31 address, 0x44(68)
bus.write_i2c_block_data(DEVICE_ADDR, 0x2C, [0x06])
 
time.sleep(0.5)
 
# SHT31 address, 0x44(68)
# Read data back from 0x00(00), 6 bytes
# Temp MSB, Temp LSB, Temp CRC, Humididty MSB, Humidity LSB, Humidity CRC
data = bus.read_i2c_block_data(DEVICE_ADDR, 0x00, 6)
 
# Convert the data
raw_temp = data[0] * 256 + data[1]
raw_humidity= data[3] * 256 + data[4]
#Celcius
cTemp = -45 + (175 * raw_temp / 65535.0)

#Fahrenheit
fTemp = -49 + (315 * raw_temp / 65535.0)
humidity = (100 * raw_humidity) / 65535.0
 
# Output data to screen
#print ("Raw data: {}".format(data))
print "{} Temp {:.2f}F,{:.2f} %RH".format(datetime.now(), fTemp, humidity)

payload = {'sensor': 'livingroom','temp': "{:.3f}".format(fTemp)
	, 'humidity': "{:.3f}".format(humidity)}
r = requests.get('http://morningsun:5000/log_temp', params=payload)
