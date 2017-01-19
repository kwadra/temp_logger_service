#!/usr/bin/env python
from flask import Flask, request
from decimal import *
from pprint import pprint
import rrdtool
import logging

app = Flask(__name__)
@app.route('/log_temp')
def log_temp():
    # show the post with the given id, the id is an integer

    temp=Decimal(request.args.get('temp'))
    humidity=Decimal(request.args.get('humidity'))
    sensor=request.args.get('sensor')
    rrdtool.update("temp_{}.rrd".format(sensor), "N:{}:{}".format(temp, humidity))
    return 'Location %s %s %s' %(sensor,temp,humidity)
