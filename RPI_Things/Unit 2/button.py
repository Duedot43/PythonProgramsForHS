from gpiozero import LED, Button
import multiprocessing
from time import sleep
def button1s():
    button1 = Button(18)
    led1 = LED(6)
    while True:
        print("wait 1")
        button1.wait_for_press()
        print("button1 pressed")
        sleep(.5)
        led1.toggle()
def button2s():
    button2 = Button(4)
    led2 = LED(5)
    while True:
        print("wait2")
        button2.wait_for_press()
        print("button2 pressed")
        sleep(.5)
        led2.toggle()
button1m = multiprocessing.Process(target=button1s)
button2m = multiprocessing.Process(target=button2s)
button1m.start()
button2m.start()
button1m.join()
button2m.join()