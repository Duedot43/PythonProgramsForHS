from gpiozero import LED,Button
from time import sleep
import multiprocessing
red = LED(13)
yellow = LED(6)
green = LED(5)
button = Button(19)
buzzer = LED(26)
buttonpending = False
def pendbutton():
    global buttonpending
    buttonpending = True
while True:
    if buttonpending:
        buzzer.on()
        sleep(3)
        buzzer.off()
        buttonpending = False
    if buttonpending == False:
        red.off()
        green.on()
        sleep(3)
        green.off()
        yellow.on()
        sleep(1)
        yellow.off()
        red.on()
        sleep(3) 
        button.is_pressed() = pendbutton()