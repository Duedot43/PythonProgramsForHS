from gpiozero import LED
from time import sleep
led1 = LED(4)
while true:
    led1.on()
    sleep(1)
    led1.ofF()
    sleep(1)
    

