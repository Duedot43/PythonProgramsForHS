from gpiozero import LED, Button
import multiprocessing
from time import sleep
from random import randint
while True:
    led_start = LED()
    def button1s():
        global led_start, button2m, win
        button1 = Button(18)
        led1 = LED(6)
        button1.wait_for_press()
        button2m.close()
        led1.on()
        led_start.off()
        print("Player 1 wins!")
        win = 0
    def button2s():
        global led_start, button1m, win
        button2 = Button(4)
        led2 = LED(5)
        button2.wait_for_press()
        button1m.close()
        led2.on()
        led_start.off()
        print("Player 2 wins!")
        win = 1
    sleep(randint(2,4))
    led_start.on()
    button1m = multiprocessing.Process(target=button1s)
    button2m = multiprocessing.Process(target=button2s)
    button1m.start()
    button2m.start()
    button1m.join()
    button2m.join()