#!/usr/bin/python

from time import strftime,sleep,time
from socket import gethostname
import string, os, sys, sqlite3, psycopg2, server_cred

def write_log_psql(ts,val):

        conn_string = str("dbname = '"+ server_cred.db_name + "' user = '" + server_cred.username + "' host = '" + server_cred.host_ip + "' password = '" + server_cred.password + "'")
        conn = psycopg2.connect(conn_string)
        curs = conn.cursor()
        #query_string = str("INSERT INTO elec_adu values('" + str(ts) + "','" + str(val) + "');")
        query_string = "INSERT INTO elec_adu values(%s,%s);"
        curs.execute(query_string, (ts,val))
        conn.commit()
        curs.close()
        conn.close()

def main():
	timestamp = strftime("%Y-%m-%d %H:%M:%S")
	write_log_psql(timestamp,999)

if __name__ == '__main__':
        main()

