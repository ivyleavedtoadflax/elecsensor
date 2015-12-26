#!/bin/bash
# Use > 1 to consume two arguments per pass in the loop (e.g. each
# argument has a corresponding value to go with it).
# Use > 0 to consume one or more arguments per pass in the loop (e.g.
# some arguments don't have a corresponding value to go with it such
# as in the --default example).
# note: if this is set to > 0 the /etc/hosts part is not recognized ( may be a bug )
# Based on SO answer here: 
# http://stackoverflow.com/questions/192249/how-do-i-parse-command-line-arguments-in-bash
while [[ $# > 1 ]]
do
key="$1"

case $key in
    -h|--host)
    HOST="$2"
    shift # past argument
    ;;
    -p|--passwordfile)
    PASSWORDFILE="$2"
    shift # past argument
    ;;
    -P|--user)
    PUSER="$2"
    shift # past argument
    ;;
    -q|--query)
    QUERY="$2"
    shift # past argument
    ;;
    -o|--output)
    OUTPUT="$2"
    shift # past argument
    ;;
    *)
            # unknown option
    ;;
esac
shift # past argument or value
done
#echo OUTPUT  = "${OUTPUT}"
#echo PASSWORDFILE = "${PASSWORDFILE}"
#echo HOST = "${HOST}"
#echo USER = "${PUSER}"
# Extract password from server_cred.py file

foo=$(grep 'password\s\=\s\W\K(.*?)\W' "$PASSWORDFILE" -Po)

# Set Postgres password for this session

export PGPASSWORD=${foo%\'}

# Setup query string 

QUERY1='\copy ('"$QUERY"') to '"$OUTPUT"' csv header;'

echo "$QUERY1"

# Send query to server

psql -h "$HOST" -U "$PUSER" -d sensorpi -c "$QUERY1"
