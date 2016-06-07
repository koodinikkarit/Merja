import httplib
import RPi.GPIO as GPIO
import config
import http_funktiot
from time import sleep


GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.IN)

pressed = False


while True:
	if(GPIO.input(4) == True):
		pressed = False	
	elif(GPIO.input(4) == False and not pressed):
		pressed = True
		print 'moi'

		# these functions are in their own file
		http_funktiot.taistodefault()
		http_funktiot.wakeuptykkikone()
		http_funktiot.wakeupnstreamkone()
		http_funktiot.wakeupkstreamkone()
	sleep(0.05)

