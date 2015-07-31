#!/bin/bash

NAME="esports-wechat"
FLASKDIR=/home/tan/Projects/esports-wechat
VENVDIR=/home/tan/.pyenv/versions/wechat-2.7.9
SOCKFILE=/home/tan/Projects/esports-wechat/sock
USER=tan
GROUP=tan
NUM_WORKERS=3

echo "Starting $NAME"

# activate the virtualenv
cd $VENVDIR
source bin/activate

export PYTHONPATH=$FLASKDIR:$PYTHONPATH

# Create the run directory if it doesn't exist
RUNDIR=$(dirname $SOCKFILE)
test -d $RUNDIR || mkdir -p $RUNDIR

# Start your unicorn
exec gunicorn main:app -b 127.0.0.1:8000 \
  --name $NAME \
  --workers $NUM_WORKERS \
  --user=$USER --group=$GROUP \
  --log-level=debug \
  --bind=unix:$SOCKFILE
