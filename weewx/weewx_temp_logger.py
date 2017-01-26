#!/usr/bin/env python

import sqlite3 
import argparse
import RRDUpdate


parser = argparse.ArgumentParser(description='Log temp/humidity')
parser.add_argument('--name', dest="name",help='Sensor name or location')
parser.add_argument('--working-path', dest="working_path",help='URL')
parser.add_argument('--weewx-archive', dest='archive_db',help="sqlite3 db file")
args = parser.parse_args()


sqlite_file="/usr/local/weewx/archive/weewx.sdb"


query="""
	select dateTime, interval, inTemp, inHumidity from archive order by dateTime desc limit 1;
"""

# Connecting to the database file
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

# 4) Selecting only up to 10 rows that match a certain value in 1 column
c.execute(query)
(time, interval, inTemp, inHumidity) = c.fetchone()
print("{} {}".format(inTemp, inHumidity))


rrd_update=RRDUpdate.RRDUpdate(args.working_path)
rrd_update.log_temp(args.name,  inTemp, inHumidity)

