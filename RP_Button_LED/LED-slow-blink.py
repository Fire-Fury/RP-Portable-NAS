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

try:
    #Main code
    channelOn()

    while(True):
        pulseOn()
        sleep(0.1)
        pulseOff()
        sleep(0.4)
        
except KeyboardInterrupt:
    #In the event of a keyboard interrupt
    GPIO.cleanup() #clean exit
except:
    #All other exceptions
    GPIO.cleanup() #clean exit
finally:
    GPIO.cleanup() #Ensures a clean exit

