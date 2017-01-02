#!/bin/sh

OUTFILE=temp_bedroom.rrd
rrdtool create $OUTFILE --step 300 \
 DS:temp_1:GAUGE:600:50:120 \
 RRA:LAST:0.5:1:1200 \
 RRA:MIN:0.5:12:2400 \
 RRA:MAX:0.5:12:2400 \
 RRA:AVERAGE:0.5:12:2400 \
 RRA:AVERAGE:0.5:1h:3y \
DS:humidity_1:GAUGE:600:0:100 
