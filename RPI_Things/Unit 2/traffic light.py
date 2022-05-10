from gpiozero import LED,Button
from time import sleep
import multiprocessing
red = LED(13)
yellow = LED(6)
green = LED(5)
button = Button(19)
buzzer = LED(26)
buttonpending = False
def pressed():
    global buttonpending
    buttonpending = True
while True:
    if buttonpending:
        for x in range(0, 4):
            buzzer.on()
            sleep(.5)
            buzzer.off()
            sleep(.5)
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
        button.when_pressed = pressed
