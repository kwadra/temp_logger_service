#!/bin/sh

PATH=$PATH:/usr/local/bin
WORK_PATH=$1
SENSOR_NAME=$2

transfer=1

if [ ! -z "$WORK_PATH" ]
then
	DIR=$1
else
	echo "Using PWD"
	DIR=$(pwd)
fi

. $DIR/graph_config.sh

transfer() {
	source_file=$1
	shift
	scp -i $KEY_FILE $source_file ${REMOTE_USER}@$REMOTE_HOST:${REMOTE_PATH}
	return $?
}
#daily
OUT_NAME=temp_${SENSOR_NAME}.svg
RRD_FILE=${DIR}/temp_${SENSOR_NAME}.rrd

rrdtool graph $DIR/$OUT_NAME \
--width=800 \
 --imgformat SVG \
--title "${SENSOR_NAME} Temp/Humidity" \
DEF:temp1=$RRD_FILE:temp_1:AVERAGE \
DEF:humid1=$RRD_FILE:humidity_1:AVERAGE \
LINE1:temp1#0000FF:"temperature" \
LINE2:humid1#FF0000:"humidity" \
VDEF:temp1Min=temp1,MINIMUM \
VDEF:temp1Max=temp1,MAXIMUM \
VDEF:humid1Min=humid1,MINIMUM \
VDEF:humid1Max=humid1,MAXIMUM \
COMMENT:"\l" \
COMMENT:"Temp Min/Max/Cur" \
GPRINT:temp1Min:"%6.2lf" \
GPRINT:temp1Max:"%6.2lf" \
GPRINT:temp1:LAST:"%6.2lf%SdegF\l" \
COMMENT:"Humidity Min/Max/Cur" \
GPRINT:humid1Min:"%6.2lf" \
GPRINT:humid1Max:"%6.2lf" \
GPRINT:humid1:LAST:"%6.2lf\l"

rc=$?
echo "rc=${rc}"

if [ ${transfer} -ne 0 ]
then
	transfer $DIR/$OUT_NAME
	rc=$?
	echo "Transfer rc=${rc}"
fi

