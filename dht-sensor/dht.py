#!/usr/bin/python
import sys
import Adafruit_DHT

while True:

    humidity, temperature = Adafruit_DHT.read_retry(11, 7)
	
    print '{0:0.1f} {1:0.1f} %'.format(temperature, humidity)
