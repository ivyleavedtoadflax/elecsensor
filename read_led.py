#!/usr/bin/python

import RPi.GPIO as GPIO
#from time import sleep
from time import strftime,sleep,time
from socket import gethostname
import string, os, sys, sqlite3, psycopg2, server_cred

######################### Setup GPIO PINS #########################

# Use Broadcom chip reference for GPIO
GPIO.setmode(GPIO.BCM)

# Suppress "channel already in use" warning
GPIO.setwarnings(False)

# Name pins

pin2 = 4 	# LED
pin4 = 17       # Photoresistor 

GPIO.setup(pin2, GPIO.OUT)
GPIO.setup(pin4, GPIO.OUT)

# Set initial pin states. Wired led on pin2 the wrong way so start high and go low!

GPIO.output(pin2, GPIO.LOW)
GPIO.output(pin4, GPIO.LOW)

light = 0 # must be numeric

# Define functions

def getLight(thresh):
	lightCount = 0
	GPIO.setup(pin4, GPIO.IN)		 # This takes about 1 millisecond per loop cycle
	while (GPIO.input(pin4) == GPIO.LOW):
		lightCount += 0.001
	GPIO.setup(pin4, GPIO.OUT)
	if lightCount < thresh:
		sleep(0.01) # set a timeout to avoid counting the same blink twice
		return(0.001)
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

def write_log_psql(ts,day,night,val):

        conn_string = str("dbname = '"+ server_cred.db_name + "' user = '" + server_cred.username + "' host = '" + server_cred.host_ip + "' password = '" + server_cred.password + "'")
        conn = psycopg2.connect(conn_string)
        curs = conn.cursor()
        query_string = str("INSERT INTO elec values('" + str(ts) + "','" + str(day) + "','" + str(night) + "','" + str(val) + "');")
        curs.execute(query_string)
        conn.commit()
        curs.close()
        conn.close()

#
def main():

	day = 0
	night = 0  

	while True:
		timeout = time() + 60
	
		counter = 0
		while timeout > time():
			counter += getLight(600)

                timestamp = strftime("%Y-%m-%d %H:%M:%S")
		
		if strftime("%H") in [23, range(1, 6)]:
			day += counter
		else:
			night += counter
		
		try:
			write_log_psql(timestamp,day,night,counter)
		except:
			pass
		#print timestamp + "," + str(day) + "," + str(night) + "," + str(counter)
	

if __name__ == '__main__':
	main()

GPIO.cleanup()
