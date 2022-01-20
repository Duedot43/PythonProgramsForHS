import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

#pin variables

redlit =  1
grnlit = 2
yelolit = 3

#Redlit GPIO:
GPIO.setup(redlit, GPIO.OUT)
print ("(DEBUG) redlit initialized")
#grnlit GPIO:
GPIO.setup(grnlit, GPIO.OUT)
print ("(DEBUG) grnlit initialized")
#yelolit GPIO:
GPIO.setup(yelolit, GPIO.OUT)
print ("(DEBUG) yelolit initialized")

#Main Prog

#Blink all lights on off for a test
GPIO.output(redlit, True)
GPIO.output(grnlit, True)
GPIO.output(yelolit, True)
print("(DEBUG) all on")
time(1)
GPIO.output(redlit, False)
GPIO.output(grnlit, False)
GPIO.output(yelolit, False)
print("(DEBUG) all off")
while True:
	GPIO.output(redlit, True)
	time(5)
	GPIO.output(redlit, False)
	GPIO.output(yelolit, True)
	time(1)
	GPIO.output(yelolit, False)
	GPIO.output(grnlit, True)
	time(5)
	GPIO.output(grnlit, False)

