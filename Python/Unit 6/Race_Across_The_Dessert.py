import random
import os
game = 0
def display_board(plr_stat, enm_stat):
    board = "Distance:" + plr_stat[0] + ", Thirst:" + plr_stat[1] + ", Water left:" + plr_stat[2] + ", Enegry:" + plr_stat[3] + "\n\nEnemy distance:" + enm_stat[0] + ", Enemy thirst:" + enm_stat[1] + ", Enemy water left:" + enm_stat[2] + ", Enemy enegry:" + enm_stat[3]
    return board
def drink(plr_stat):
    drinkval = random.randint(20,40)
    value = 0
    if plr_stat[1] == "0":
        print("You cannot drink water!")
        value = value+1
    elif plr_stat[2] == "0":
        print("You are out of water!")
        value = value+1
    elif int(plr_stat[1]) <= int(drinkval):
        plr_stat[2] = str(int(plr_stat[2]) - int(plr_stat[1]))
        plr_stat[1] = str(int(plr_stat[1]) - int(plr_stat[1]))
        print("You are no longer thursty!")
        value = value+1
    elif int(plr_stat[2]) <= int(drinkval):
        plr_stat[2] = str(int(plr_stat[2]) - int(plr_stat[2]))
        plr_stat[1] = str(int(plr_stat[1]) - int(plr_stat[2]))
        print("You are out of water!")
        value = value+1
    if value > 1:
        print("ERROR!")
        exit()
    elif value == 0:
        plr_stat[1] = str(int(plr_stat[1]) - drinkval)
        plr_stat[2] = str(int(plr_stat[2]) - drinkval)
def forward(plr_stat, speed):
    if speed == "2":
        speed_slow = random.randint(10,20)
        enegry_slow = random.randint(3,6)
        if int(plr_stat[3]) >= int(enegry_slow) and int(plr_stat[1]) <= 97 and int(plr_stat[0]) <= 200:
            print("PLACEHOLDER")


def plr_choose(plr_stat):
    choice = str(input("(1) Drink water.\n(2) Forward slow.\n(3) Forward moderate.\n(4) Forward fast.\n(5) Sleep for the night.\n(6) Quit\n?"))
    if choice == "1":
        drink(plr_stat)
    if choice == "2" or choice == "3" or choice == "4":
        forward(plr_stat, choice)

os.system("clear")
random_head_start = random.randint(10, 20)
print("You have stolen a camel to make your way across the dessert to your home.\nBut the Natives you stole the camel from want it back, as its a racing camel!\n Use your resources and out run the Natives to make it home!\nYou have been given a head start of " + str(random_head_start) + ". Good luck!\n")
thirst_start = random.randint(0,10)
plr_stat = [str(random_head_start), str(thirst_start), "100", "100"]
enm_stat = ["0", "0", "100", "100"]
while game == 0:
    print(display_board(plr_stat, enm_stat))
    plr_choose(plr_stat)
