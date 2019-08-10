#!/usr/bin/env python

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

GPIO.setwarnings(False)

GPIO.setup(11, GPIO.OUT) #Pin 11 is GPIO pin 17

fan_on = GPIO.input(11)

if(fan_on):
	print("LED is on")
else:
	print("LED is off")