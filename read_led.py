#!/usr/bin/python

import RPi.GPIO as GPIO
from time import sleep
from time import strftime
from socket import gethostname
import string, os, sys, sqlite3

######################### Setup GPIO PINS #########################

# Use Broadcom chip reference for GPIO
GPIO.setmode(GPIO.BCM)

# Suppress "channel already in use" warning
GPIO.setwarnings(False)

# name pins

pin2 = 4 	# LED
pin4 = 17       # Photoresistor 

GPIO.setup(pin2, GPIO.OUT)
GPIO.setup(pin4, GPIO.OUT)

# Set initial pin states. Wired led on pin2 the wrong way so start high and go low!

GPIO.output(pin2, GPIO.LOW)
GPIO.output(pin4, GPIO.LOW)

light = 0 # must be numeric

# Define functions

# Get reading from photoreceptor

def getLight(thresh):
	lightCount = 0
	GPIO.setup(pin4, GPIO.IN)		 # This takes about 1 millisecond per loop cycle
	while (GPIO.input(pin4) == GPIO.LOW):
		lightCount += 1
	GPIO.setup(pin4, GPIO.OUT)
	if lightCount < thresh:
		sleep(0.01) # set a timeout to avoid counting the same blink twice
		return(1)
	else:
		return(0)

# Run data recording LED init sequence

def ledFlash(i,j):	
	ledCount = 0
	while ledCount < i:
		GPIO.output(pin2, GPIO.HIGH)
		sleep(j)
		GPIO.output(pin2, GPIO.LOW)
		sleep(j)
		ledCount +=1

def write_log_csv():
        log = open("/home/pi/read_led/Log.csv", "a")
	log.write("\n" + str(ts) + "," + str(ldr_count))
	log.close()	


#
def main():

	while True:
		getLight(600)

	#timestamp = strftime("%Y-%m-%d %H:%M:00")

# Main function

#def main():
#
#	timestamp = strftime("%Y-%m-%d %H:%M:%S")
#		
#	ledFlash(2,0.1)
#	light = getLight()
        
#	print "timestamp:    ", str(timestamp)
#	print "light:        ", str(light)

if __name__ == '__main__':
	main()

GPIO.cleanup()
