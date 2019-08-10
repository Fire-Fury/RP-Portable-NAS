#!/usr/bin/env python

import RPi.GPIO as GPIO
from time import sleep

#Set any warnings off
GPIO.setwarnings(False)

def channelOn():
   GPIO.setmode(GPIO.BOARD)
   GPIO.setup(11, GPIO.OUT) #Pin 11 is GPIO 17

def pulseOn():
    #Turns on the LED
    GPIO.output(11, GPIO.HIGH)


channelOn()    
pulseOn()

