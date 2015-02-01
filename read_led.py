#!/usr/bin/python

import RPi.GPIO as GPIO
from time import sleep
from time import strftime
from socket import gethostname
import string, os, sys, sqlite3

#	(ORANGE) 3.3v	[][]	5v (RED)
#	I2C0 SDA	[][]	DO NOT CONNECT
#	I2C0 SCL	[][]	GROUND (BLACK)
#	(GREEN) GPIO 4	[][]	UART TXD
#	DO NOT CONNECT	[][]	UART RXD
#	(YELLOW) GPIO 17[][]	GPIO 18 (ORANGE)
#	(BLUE) GPIO 21	[][]	DO NOT CONNECT
#	(PURPLE) GPIO 22[][]	GPIO 23
#	DO NOT CONNECT	[][]	GPIO 24
#	SPI MOSI	[][]	DO NOT CONNECT
#	SPI MISO	[][]	GPIO 25
#	SPI SCLK	[][]	SP10 CEO N
#	DO NOT CONNECT	[][]	SP10 CE1 N

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

def getLight():
	lightCount = 0
	GPIO.setup(pin4, GPIO.IN)		 # This takes about 1 millisecond per loop cycle
	while (GPIO.input(pin4) == GPIO.LOW):
		lightCount += 1
	GPIO.setup(pin4, GPIO.OUT)
	return(lightCount)

# Run data recording LED init sequence

def ledFlash(i,j):	
	ledCount = 0
	while ledCount < i:
		GPIO.output(pin2, GPIO.HIGH)
		sleep(j)
		GPIO.output(pin2, GPIO.LOW)
		sleep(j)
		ledCount +=1

#

while True:
	print getLight()
	
#
# Main function

#def main():
#
#	timestamp = strftime("%Y-%m-%d %H:%M:%S")
#		
#	ledFlash(2,0.1)
#	light = getLight()
        
#	print "timestamp:    ", str(timestamp)
#	print "light:        ", str(light)

#if __name__ == '__main__':
#	main()

GPIO.cleanup()
