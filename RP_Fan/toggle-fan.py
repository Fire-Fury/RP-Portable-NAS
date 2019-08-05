#!/usr/bin/env python

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

GPIO.setwarnings(False)

GPIO.setup(3, GPIO.OUT) #Pin 3 is GPIO 2

GPIO.output(3, not GPIO.input(3))