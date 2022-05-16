from gpiozero import LED,Button
from random import randint
from time import sleep
gpios = {
    "button":[Button()],
    "led":{
        "TL":LED(),
        "TR":LED(),
        "L":LED(),
        "M":LED(),
        "R":LED(),
        "BL":LED(),
        "BR":LED()
    }
}
while True:
    gpios['button'][0].wait_for_press()
    for x in gpios['led']:
        gpios['led'][x].off()
    for x in range(0,5):
        gpios['led']['TL'].off()
        gpios['led']['TR'].off()
        gpios['led']['L'].off()
        gpios['led']['M'].off()
        gpios['led']['R'].off()
        gpios['led']['BL'].off()
        gpios['led']['BR'].off()
        sleep(0.2)
        gpios['led']['TL'].on()
        gpios['led']['TR'].on()
        gpios['led']['M'].on()
        gpios['led']['BL'].on()
        gpios['led']['BR'].on()
        sleep(0.2)
        gpios['led']['TL'].off()
        gpios['led']['TR'].off()
        gpios['led']['M'].off()
        gpios['led']['BL'].off()
        gpios['led']['BR'].off()
        sleep(0.2)
        gpios['led']['M'].on()
        gpios['led']['R'].on()
        gpios['led']['L'].on()
        sleep(0.2)
        gpios['led']['M'].on()
        gpios['led']['R'].on()
        gpios['led']['L'].on()
        sleep(0.2)
        gpios['led']['M'].off()
        gpios['led']['R'].off()
        gpios['led']['L'].off()
    randnum = randint(1,6)
    if randnum == 1:
        gpios['led']['M'].on()
    elif randnum == 2:
        gpios['led']['TL'].on()
        gpios['led']['BR'].on()
    elif randnum == 3:
        gpios['led']['TL'].on()
        gpios['led']['M'].on()
        gpios['led']['BR'].on()
    elif randnum == 4:
        gpios['led']['TL'].on()
        gpios['led']['TR'].on()
        gpios['led']['BL'].on()
        gpios['led']['BR'].on()
    elif randnum == 5:
        gpios['led']['TL'].on()
        gpios['led']['TR'].on()
        gpios['led']['BL'].on()
        gpios['led']['BR'].on()
        gpios['led']['M'].on()
    elif randnum == 6:
        gpios['led']['TL'].on()
        gpios['led']['TR'].on()
        gpios['led']['L'].on()
        gpios['led']['R'].on()
        gpios['led']['M'].on()
        gpios['led']['BR'].on()
        gpios['led']['BL'].on()
        