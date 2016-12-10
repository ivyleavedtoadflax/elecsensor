#!/bin/bash

puser="other_user"
host="52.48.60.14"
passfile="server_cred.py"
path="/var/www/html/"

# Hourly
sudo ./psql_to_csv.sh -o "$path"hourly.csv -q 'select * from hourly_elec_adu' -p "$passfile" -P "$puser" -h "$host"

# Daily
sudo ./psql_to_csv.sh -o "$path"daily.csv -q 'select * from daily_elec_adu order by day limit 20' -p "$passfile" -P "$puser" -h "$host"

# Weekly
sudo ./psql_to_csv.sh -o "$path"weekly.csv -q 'select * from weekly_elec_adu' -p "$passfile" -P "$puser" -h "$host"

# Monthly
sudo ./psql_to_csv.sh -o "$path"monthly.csv -q 'select * from monthly_elec_adu' -p "$passfile" -P "$puser" -h "$host"

