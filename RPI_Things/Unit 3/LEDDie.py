from gpiozero import LED,Button
from random import randint
from time import sleep
Button() = B
LED() = TL
LED() = TR
LED() = L
LED() = M
LED() = R
LED() = BL
LED() = BR
while:
    B.wait_for_press()
    for x in 5:
        TL.off()
        TR.off()
        L.off()
        M.off()
        R.off()
        BL.off()
        BR.off()
        sleep(0.2)
        TL.on()
        TR.on()
        M.on()
        BL.on()
        BR.on()
        sleep(0.2)
        TL.off()
        TR.off()
        M.off()
        BL.off()
        BR.off()
        sleep(0.2)
        M.on()
        R.on()
        L.on()
        sleep(0.2)
        M.on()
        R.on()
        L.on()
        sleep(0.2)
        M.off()
        R.off()
        L.off()
    randnum = random.randint(1,6)
    if randnum == 1:
        M.on()
    elif randnum == 2:
        TL.on()
        BR.on()
    elif randnum == 3:
        TL.on()
        M.on()
        BR.on()
    elif randnum == 4:
        TL.on()
        TR.on()
        BL.on()
        BR.on()
    elif randnum == 5:
        TL.on()
        TR.on()
        BL.on()
        BR.on()
        M.on()
    elif randnum == 6:
        TL.on()
        TR.on()
        L.on()
        R.on()
        M.on()
        BR.on()
        BL.on()
        