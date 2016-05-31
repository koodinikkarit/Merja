import httplib
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.IN)

pressed = False

def buttonPressed():
	conn = httplib.HTTPConnection("taisto.ths.dom:1337")
	conn.request("GET", "/api?con=7&cpu=2")

def wakeuptykkikone():
	conn = httplib.HTTPConnection("wakeup.ths.dom")
	conn.request("GET", "/api/?machine_id=1")
	
def wakeupnstreamkone():
	conn = httplib.HTTPConnection("wakeup.ths.dom")
	conn.request("GET", "/api/?machine_id=2")
	
def wakeupkstreamkone():
	conn = httplib.HTTPConnection("wakeup.ths.dom")
	conn.request("GET", "/api/?machine_id=7")
	

while True:
	if(GPIO.input(4) == True):
		pressed = False	
	elif(GPIO.input(4) == False and not pressed):
		pressed = True
		print 'moi'
		buttonPressed()
	sleep(0.05)

