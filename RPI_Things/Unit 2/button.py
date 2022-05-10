from gpiozero import LED, Button
import multiprocessing; import os
import time, random
startled = LED(6); startled.on()
button1 = Button(13)
button2 = Button(5)
tim = time.time()
while True:
    print("wait 1")
    mark = False
    if button1.is_pressed:
        print("button1 pressed")
        startled.off()
        mark = True
    if button2.is_pressed:
        print("button2 pressed")
        startled.off()
        mark = True
    if mark:
        print(float(time.time())-float(tim), " seconds")
        again = input("Play again?\nY/N\n> ")
        if again.upper() == "N":
            break
        else:
            time.sleep(random.randint(1,3))
            startled.on()
            tim = time.time()