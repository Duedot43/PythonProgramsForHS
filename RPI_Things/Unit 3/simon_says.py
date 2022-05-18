from gpiozero import LED, Button
from time import sleep
import random
led1 = LED(13)
led2 = LED(5)
led3 = LED(6)
led4 = LED(19)
btn1 = Button(18)
btn2 = Button(23)
btn3 = Button(24)
btn4 = Button(25)
seq = {
            "led":[],
            "btn":[],
            "score":0
        }
def fail():
    global seq
    print("Your score was " + str(seq['score']))
    again = input("Play again?\n> ")
    if again.lower() == 'yes' or again.lower() == 'y':
        seq = {
            "led":[],
            "btn":[],
            "score":0
        }
    else:
        exit()
    
while True:
    rand = random.randint(0,3)
    if rand == 0:
        seq['led'].append(led1)
        seq['btn'].append(btn1)
    elif rand == 1:
        seq['led'].append(led2)
        seq['btn'].append(btn2)
    elif rand == 2:
        seq['led'].append(led3)
        seq['btn'].append(btn3)
    elif rand == 4:
        seq['led'].append(led4)
        seq['btn'].append(btn4)
    for x in seq['led']:
        x.on()
        print("on" + str(x))
        sleep(1)
        x.off()
        print("off " + str(x))
        sleep(1)
    for x in seq['btn']:
        print("wait " + str(x))
        while True:
            if btn1.is_pressed:
                if btn1 == x:
                    print("done")
                    seq['score'] = seq['score']+1
                    break
                else:
                    print("Fail!")
                    fail()
                    break
            if btn2.is_pressed:
                if btn2 == x:
                    print("done")
                    seq['score'] = seq['score']+1
                    break
                else:
                    print("Fail!")
                    fail()
                    break
            if btn3.is_pressed:
                if btn3 == x:
                    print("done")
                    seq['score'] = seq['score']+1
                    break
                else:
                    print("Fail!")
                    fail()
                    break
            if btn4.is_pressed:
                if btn4 == x:
                    print("done")
                    seq['score'] = seq['score']+1
                    break
                else:
                    print("Fail!")
                    fail()
                    break
        sleep(.1)
