#!/usr/bin/python

import RPi.GPIO as GPIO
from time import strftime, sleep, time
import string, os, sys, sqlite3, psycopg2, server_cred

######################### Setup GPIO PINS #########################

# Use Broadcom chip reference for GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Name pins

pin4 = 17       # Photoresistor

GPIO.setup(pin4, GPIO.IN)

# Define functions

def getLight():
	input_value = GPIO.input(pin4)
	# Sleep value can be experimented with, but 0.03 seems to be reasonable
	sleep(0.03)
	if (input_value == 0):
		# 0.001 is the value in kWh that one flash represents
		return(0.001)
	else:
		return(0)
	
def write_log_csv(ts,val):
        log = open("/home/pi/elec/Log_adu.csv", "a")
	log.write("\n" + str(ts) + "," + str(val))
	log.close()

def write_log_psql(ts,val):

        conn_string = str("dbname = '"+ server_cred.db_name + "' user = '" + server_cred.username + "' host = '" + server_cred.host_ip + "' password = '" + server_cred.password + "'")
        conn = psycopg2.connect(conn_string)
        curs = conn.cursor()
	query_string = "INSERT INTO elec_adu values(%s,%s);"
	curs.execute(query_string, (ts,val))
        conn.commit()
        curs.close()
        conn.close()

def main():

	# Set the timeout to be the current time plus 60 seconds

	while True:
		timeout = time() + 60
	# Initiliase accumulator at zero
	# Then run getLight and add to accumulator
		counter = 0
		while timeout > time():
			counter += getLight()

                timestamp = strftime("%Y-%m-%d %H:%M:%S")

	# Try to log to psql database

		try:
			write_log_psql(timestamp,counter)
		except:
			pass

	# Also try to log to csv

		try:
			write_log_csv(timestamp,counter)
		except:
			pass

if __name__ == '__main__':
	main()

GPIO.cleanup()
