import httplib
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.IN)

pressed = False

def buttonPressed():
	conn = httplib.HTTPConnection("192.168.180.23:1337")
	conn.request("GET", "/api?con=7&cpu=2")
	return True

while True:
	if(GPIO.input(4) == True):
		pressed = False	
	elif(GPIO.input(4) == False and not pressed):
		pressed = True
		print 'moi'
		buttonPressed()
	sleep(0.05)

