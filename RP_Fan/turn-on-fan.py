#!/usr/bin/env python

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

GPIO.setwarnings(False)

GPIO.setup(3, GPIO.OUT, initial=GPIO.LOW)

GPIO.output(3, GPIO.HIGH)

