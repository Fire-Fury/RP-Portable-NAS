#!/usr/bin/env python

import RPi.GPIO as GPIO
from time import sleep

#Set any warnings off
GPIO.setwarnings(False)

def channelOn():
   GPIO.setmode(GPIO.BOARD)
   GPIO.setup(7, GPIO.OUT) #Pin 7 is GPIO 4

def pulseOn():
    #Turns on the LED
    GPIO.output(7, GPIO.HIGH)

def pulseOff():
    #Turns off the LED
    GPIO.output(7, GPIO.LOW)


channelOn()

for t in range(3):
    pulseOn()
    sleep(0.1)
    pulseOff()
    sleep(0.4)

for y in range(5):
    pulseOn()
    sleep(0.1)
    pulseOff()
    sleep(0.1)
    
pulseOn()

