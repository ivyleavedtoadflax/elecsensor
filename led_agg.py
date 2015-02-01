from time import strftime,sleep,time
from socket import gethostname
import string, os, sys, sqlite3, psycopg2, server_cred

def write_log_psql(ts,day,night,val):

        conn_string = str("dbname = '"+ server_cred.db_name + "' user = '" + serve$
        conn = psycopg2.connect(conn_string)
        curs = conn.cursor()
        query_string = str("INSERT INTO elec values('" + str(ts) + "','" + str(day$
        curs.execute(query_string)
        conn.commit()
        curs.close()
        conn.close()


def get_initial_vals():
        initial = open("/home/pi/read_led/initial.vals","r")
        day = initial.readline()
        night = initial.readline()
        initial.close()


