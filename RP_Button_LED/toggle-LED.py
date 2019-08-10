#!/usr/bin/env python

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

GPIO.setwarnings(False)

GPIO.setup(11, GPIO.OUT) #Pin 11 is GPIO 17

GPIO.output(11, not GPIO.input(11))