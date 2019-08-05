#!/usr/bin/env python

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

GPIO.setwarnings(False)

GPIO.setup(3, GPIO.OUT)

fan_on = GPIO.input(3)

if(fan_on):
	print("Fan is on")
else:
	print("Fan is off")