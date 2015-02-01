#!/usr/bin/python

import RPi.GPIO as GPIO
from time import strftime,sleep,time
from datetime import datetime

######################### Setup GPIO PINS #########################

# Use Broadcom chip reference for GPIO
GPIO.setmode(GPIO.BCM)

# Suppress "channel already in use" warning
GPIO.setwarnings(False)

# Name pins
pin4 = 17       # Photoresistor 

GPIO.setup(pin4, GPIO.OUT)

# Set initial pin states. Wired led on pin2 the wrong way so start high and go low!

GPIO.output(pin4, GPIO.LOW)

# Define functions

def getLight():
	lightCount = 0
	GPIO.setup(pin4, GPIO.IN)		 # This takes about 1 millisecond per loop cycle
	while (GPIO.input(pin4) == GPIO.LOW):
		lightCount += 0.001
	GPIO.setup(pin4, GPIO.OUT)
	return(lightCount)

def write_log_csv(ts,ldr_count):
        log = open("/home/pi/read_led/stream.dat", "a")
	log.write("\n" + str(ts) + "," + str(ldr_count))
	log.close()	

def main():

	while True:
		counter = 0
		counter += getLight()
		timestamp = datetime.now().strftime("%H:%M:%S.%f")
		write_log_csv(timestamp,counter)

if __name__ == '__main__':
	main()

GPIO.cleanup()
