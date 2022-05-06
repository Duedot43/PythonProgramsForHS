from gpiozero import LED,button
from time import sleep
red = LED()
yellow = LED()
green = LED()
button = Button()
buzzer = Buzzer()
def pendbutton():
    global buttonpending
    buttonpending = True
while True:
    button.when_pressed = pendbutton()
    if buttonpending == False:
        buzzer.on()
        sleep(3)
        buzzer.off()
    elif buttonpending == True:
        red.off()
        green.on()
        sleep(3)
        green.off()
        yellow.on()
        sleep(1)
        yellow.off()
        red.on()
        sleep(3)    