from gpiozero import LED
from time import sleep
from random import randint
led1 = LED(5)
led2 = LED(6)
led3 = LED(13)
led4 = LED(19)
led5 = LED(26)
try:
    while True:
        ledchoice = randint(1,5)
        if ledchoice == 1:
            theLED = led1
        elif ledchoice == 2:
            theLED = led2
        elif ledchoice == 3:
            theLED = led3
        elif ledchoice == 4:
            theLED = led4
        elif ledchoice == 5:
            theLED = led5
        theLED.on()
        sleep(.5)
        theLED.off()
except KeyboardInterrupt:
    led1.off()
    led2.off()
    led3.off()
    led4.off()
    led5.off()
    exit()