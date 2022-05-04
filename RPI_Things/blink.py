from gpiozero import LED
from time import sleep
led1 = LED(4)
while True:
    led1.on()
    sleep(1)
    led1.off()
    sleep(1)
    

