import RPi.GPIO as GPIO
import time
import random
from timeit import default_timer
GPIO.setmode(GPIO.BCM)
#Select a random number betwen 1,5 to use at the time
randtime = random.randint(1,5)

#pin variables

bton1 = 37
bton2 = 35
lit1 = 33
bton1lit = 31
bton2lit = 29

print ("(DEBUG) Random time is", randtime, "executing main program!")
#Button 1 GPIO:
GPIO.setup(bton1, GPIO.IN) 
print ("(DEBUG) Button 1 initialized")
#Button 2 GPIO:
GPIO.setup(bton2, GPIO.IN)
print ("(DEBUG) Button 2 initialized")
#Light GPIO:
GPIO.setup(lit1, GPIO.OUT)
print ("(DEBUG) Light initialized")
GPIO.setup(bton1lit, GPIO.OUT)
print ("(DEBUG) Button 1 light initialized")
GPIO.setup(bton2lit, GPIO.OUT)
print ("(DEBUG) Button 2 lignt initialized")

#Main Program

#Sleep random ammount of time
time(randtime)
GPIO.output(lit1, True)
print ("(DEBUG) printer timer variable should be 0")
print (default_timer())
print ("(DEBUG) starting timer")
start = default_timer()
def input():
	print("(DEBUG) Button one check go burrrr")
	if GPIO.input(bton1) == 0:
		GPIO.output(lit1, False)
		GPIO.output(bton1lit, True)
		print("(DEBUG) Button 1 Pin ", bton1, "Pressed")
		print (default_timer() - start)
		print("Player 1 Wins!")
		print ("Player 1's time is...")
		print (default_timer() - start)
		time(3)
		quit_n_clear()
	print("(DEBUG) Button two check go burrrr")
	if GPIO.input(bton2) == 0:
		GPIO.output(lit1, False)
		GPIO.output(bton2lit, True)
		print("(DEBUG) Button 2 Pin ", bton2, "Pressed")
		print (default_timer() - start)
		print("Player 2 Wins!")
		print("Player 2's time is...")
		print (default_timer() - start)
		time(3)
		quit_n_clear() 
	input()
def quit_n_clear():
	GPIO.output(bton1, False)
	GPIO.output(bton2, False)
	GPIO.output(lit1, False)
	GPIO.output(bton1lit, False)
	GPIO.output(bton2lit, False)
	exit()
