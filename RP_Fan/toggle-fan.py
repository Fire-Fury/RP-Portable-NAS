#!/usr/bin/env python

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

GPIO.setwarnings(False)

GPIO.setup(12, GPIO.OUT) # Pin 12 is GPIO 18

GPIO.output(12, not GPIO.input(12))