from gpiozero import LED, Button
import multiprocessing
from time import sleep
from random import randint
led_start = LED(13)
def button1s(button2m):
    global led_start, win
    button1 = Button(26)
    led1 = LED(6)
    button1.wait_for_press()
    button2m.terminate()
    led1.on()
    led_start.off()
    print("Player 1 wins!")
    win = 0
def button2s(button1m):
    global led_start, win
    button2 = Button(19)
    led2 = LED(5)
    button2.wait_for_press()
    button1m.terminate()
    led2.on()
    led_start.off()
    print("Player 2 wins!")
    win = 1
while True:
    sleep(randint(2,4))
    led_start.on()
    button2m = multiprocessing.Process(target=button2s)
    button1m = multiprocessing.Process(target=button1s, args=(button2m))
    button2m = multiprocessing.Process(target=button2s, args=(button1m))
    button1m.start()
    button2m.start()
    button1m.join()
    button2m.join()