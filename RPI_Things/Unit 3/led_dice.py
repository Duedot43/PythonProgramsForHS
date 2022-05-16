from gpiozero import LED,Button
from random import randint
from time import sleep
roll_button = Button()
#1    2
#3 4  5
#6    7
led1 = LED()
led2 = LED()
led3 = LED()
led4 = LED()
led5 = LED()
led6 = LED()
led7 = LED()
combo = {
    1:[led4],
    2:[led6, led2],
    3:[led6, led4, led2],
    4:[led1, led2, led6, led7],
    5:[led1, led2, led4, led6, led7],
    6:[led1, led2, led3, led5, led6, led7]
}
while True:
    roll_button.wait_for_press()
    roll_button.wait_for_release()
    die = randint(1,6)
    print(f"rolled {die}")
    for x in combo[die]:
        x.on()
    sleep(2)
    for x in combo[die]:
        x.off()


