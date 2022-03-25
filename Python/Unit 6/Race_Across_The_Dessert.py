import random
import os
game = 0
def display_board(stat, stat2):
    board = "Distance:" + stat[0] + ", Thirst:" + stat[1] + ", Water left:" + stat[2] + ", Enegry:" + stat[3] + "\n\nEnemy distance:" + stat2[0] + ", Enemy thirst:" + stat2[1] + ", Enemy water left:" + stat2[2] + ", Enemy enegry:" + stat2[3]
    return board
def drink(stat, bot):
    drinkval = random.randint(20,40)
    value = 0
    if stat[1] == "0":
        if bot == 0:
            print("You cannot drink water!")
        value = value+1
        return stat
    elif stat[2] == "0":
        if bot == 0:
            print("You are out of water!")
        value = value+1
        return stat
    elif int(stat[1]) <= int(drinkval):
        stat[2] = str(int(stat[2]) - int(stat[1]))
        stat[1] = str(int(stat[1]) - int(stat[1]))
        if bot == 0:
            print("You are no longer thursty!")
        value = value+1
        return stat
    elif int(stat[2]) <= int(drinkval):
        stat[2] = str(int(stat[2]) - int(stat[2]))
        stat[1] = str(int(stat[1]) - int(stat[2]))
        if bot == 0:
            print("You are out of water!")
        value = value+1
        return stat

    if value > 1:
        print("ERROR!")
        exit()
    elif value == 0:
        stat[1] = str(int(stat[1]) - drinkval)
        stat[2] = str(int(stat[2]) - drinkval)
        stat[3] = str(int(stat[3])+1)
        return stat
def forward(stat, speed, bot):
    if speed == "2":
        speed_slow = random.randint(10,20)
        enegry_slow = random.randint(3,6)
        thirst_slow = random.randint(1,8)
        if int(int(stat[0])+int(speed_slow)) >= 500:
            if bot == 0:
                print("You escaped! <fancy animation here>")
            return stat
        elif int(int(stat[1])+int(thirst_slow)) >= 97:
            if bot == 0:
                print("You are too thirsty to walk!")
            return stat
        elif int(int(stat[3])-int(enegry_slow)) <= 0:
            if bot == 0:
                print("You do not have enough enegry to continue!")
            return stat
        elif int(stat[3]) >= int(enegry_slow) and int(stat[1]) <= 97 and int(stat[0]) <= 500:
            stat[0] = str(int(stat[0])+int(speed_slow))
            stat[1] = str(int(stat[1])+int(thirst_slow))
            stat[3] = str(int(stat[3])-int(enegry_slow))
            return stat
    if speed == "3":
        speed_slow = random.randint(20,30)
        enegry_slow = random.randint(6,12)
        thirst_slow = random.randint(2,16)
        if int(int(stat[0])+int(speed_slow)) >= 500:
            if bot == 0:
                print("You escaped! <fancy animation here>")
            return stat
        elif int(int(stat[1])+int(thirst_slow)) >= 85:
            if bot == 0:
                print("You are too thirsty to walk!")
            return stat
        elif int(int(stat[3])-int(enegry_slow)) <= 0:
            if bot == 0:
                print("You do not have enough enegry to continue!")
            return stat
        elif int(stat[3]) >= int(enegry_slow) and int(stat[1]) <= 85 and int(stat[0]) <= 500:
            stat[0] = str(int(stat[0])+int(speed_slow))
            stat[1] = str(int(stat[1])+int(thirst_slow))
            stat[3] = str(int(stat[3])-int(enegry_slow))
            return stat
    if speed == "4":
        speed_slow = random.randint(40,60)
        enegry_slow = random.randint(24,48)
        thirst_slow = random.randint(4,32)
        if int(int(stat[0])+int(speed_slow)) >= 500:
            if bot == 0:
                print("You escaped! <fancy animation here>")
            return stat
        elif int(int(stat[1])+int(thirst_slow)) >= 75:
            if bot == 0:
                print("You are too thirsty to walk!")
            return stat
        elif int(int(stat[3])-int(enegry_slow)) <= 0:
            if bot == 0:
                print("You do not have enough enegry to continue!")
            return stat
        elif int(stat[3]) >= int(enegry_slow) and int(stat[1]) <= 75 and int(stat[0]) <= 500:
            stat[0] = str(int(stat[0])+int(speed_slow))
            stat[1] = str(int(stat[1])+int(thirst_slow))
            stat[3] = str(int(stat[3])-int(enegry_slow))
            return stat
def sleep(stat, bot, stat2):
    if bot == 0:
        if int(int(stat[0])-int(stat2[0])) >= 30:
            is_enemy_move = 1
        else:
            is_enemy_move = 0
        stat2[0] = str(int(stat[0])-2)
        if int(stat[3])+30 >= 100:
            stat[3] = 100-int(stat[3])
            print("You have had a full rest!")
        else:
            stat[3] = str(int(stat[3])+30) 
        if is_enemy_move == 1:
            print("The enemy has decided to skip the night they are very close!!")
            ret =  [stat, stat2]
            return ret
def plr_choose(stat, bot, stat2):
    if bot == 0:
        choice = str(input("(1) Drink water.\n(2) Forward slow.\n(3) Forward moderate.\n(4) Forward fast.\n(5) Sleep for the night.\n(6) Quit\n?"))
    if bot == 1:
        choice = random.randint(1,5)

        #choice = 2
        #might want to improve the bot later lol
    if str(choice) == "1":
        statz = drink(stat, bot)
        return statz
    if str(choice) == "2" or str(choice) == "3" or str(choice) == "4":
        statz = forward(stat, str(choice), bot)
        return statz
    if str(choice) == "5":
        sleep(stat, bot, stat2)
def start(plr_stat):
    os.system("clear")
    print("You have stolen a camel to make your way across the dessert to your home.\nBut the Natives you stole the camel from want it back, as its a racing camel!\n Use your resources and out run the Natives to make it home!\nYou have been given a head start of " + str(plr_stat[0]) + ". Good luck!\n")
def reset(who):
    random_head_start = random.randint(10, 20)
    thirst_start = random.randint(0,10)
    plr_stat = [str(random_head_start), str(thirst_start), "100", "100"]
    enm_stat = ["0", "0", "100", "100"]
    if who == 1:
        return plr_stat
    if who == 0:
        return enm_stat
plr_stat = reset(1)
enm_stat = reset(0)
start(plr_stat)
while game == 0:

    print(display_board(plr_stat, enm_stat))
    plr_stat1 = plr_choose(plr_stat, 0, enm_stat)
    if int(len(plr_stat1)) == 2:
        plr_stat = plr_stat[0]
        enm_stat = plr_stat[1]
    else:
        plr_stat = plr_stat1
    enm_stat = plr_choose(enm_stat, 1, enm_stat)
