#!/bin/sh
source sender.properties
mkdir -p $SAVE_PATH
$EXEC sender.py $TOKEN $SAVE_PATH $TARGET