# elec

## Instructions for set up

* Establish headless wifi connection with pi
* sudo apt-get update -y
* sudo apt-get upgrade -y
* sudo apt-get install postgresql-9.1 libpq-dev python-dev python-pip
* sudo pip install psycopg2
* add a server_cred.py file with the following lines:
    * db_name = ''
    * host_ip = ''
    * username = ''
    * password = ''
