#!/bin/sh 
gunicorn --config gunicorn_config.py temp_logger:app
