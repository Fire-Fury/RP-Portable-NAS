#!/usr/bin/env python

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

GPIO.setwarnings(False)

GPIO.setup(7, GPIO.OUT) #Pin 7 is GPIO 4

GPIO.output(7, not GPIO.input(7))

