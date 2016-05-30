import RPi.GPIO as GPIO
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
	sleep(0.05)
