import os
import random
import time
def mkboard():
    global player_stats
    global enemy_distance
    print(f"Distance: {player_stats[0]} Data lost: {player_stats[1]} Replacement data: {player_stats[2]} HDD Power: {player_stats[3]}\n\nEnemy distance: {enemy_distance}\n")
def ckwin():
    pass
def drink():
    global player_stats
    global enemy_distance
    if player_stats[1] == 0:
        print("You dont have any data to replace!")
        return 1
    elif player_stats[2] == 0:
        print("You are out of Replacement data!")
        return 1
    else:
        player_stats[1] = player_stats[1]-2
        player_stats[2] = player_stats[2]-2
        return 0
def sleep():
    global player_stats
    global enemy_stats
    if player_stats[3] == 10:
        print("You turn on your generator!")
        return 1
    else:
        player_stats[3] = player_stats[3] + 2
        return 0
def walk():
    global player_stats
    global enemy_stats
    if player_stats[1] >= 9:
        print("You cannot walk! You dont have enough data!")
        return 1
    elif player_stats[3] <= 1:
        print("You cannot walk! You dont have enough HDD power!")
        return 1
    else:
        player_stats[0] = player_stats[0]+10
        player_stats[1] = player_stats[1]+1
        player_stats[3] = player_stats[3]-2
def sprint():
    global player_stats
    global enemy_stats
    if player_stats[1] >= 7:
        print("You cannot sprint! You dont have enough data!")
        return 1
    elif player_stats[3] <= 3:
        print("You cannot sprint! You dont have enough HDD power!")
        return 1
    else:
        player_stats[0] = player_stats[0]+20
        player_stats[1] = player_stats[1]+2
        player_stats[3] = player_stats[3]-3
def run():
    global player_stats
    global enemy_stats
    if player_stats[1] >= 4:
        print("You cannot run! You dont have enough data!")
        return 1
    elif player_stats[3] <= 5:
        print("You cannot run! You dont have enough HDD power!")
        return 1
    else:
        player_stats[0] = player_stats[0]+30
        player_stats[1] = player_stats[1]+3
        player_stats[3] = player_stats[3]-4
def setup():
    global player_stats
    global enemy_distance
    player_stats = [1, 0, 5, 10]
    enemy_distance = 0
def choose():
    global player_stats
    global enemy_distance
    global choice
    #choice = int(input("(1) Drink water\n(2) Walk\n(3) Sprint\n(4) Run\n(5) Sleep for the night\n(6) Quit\n? "))
    redo = 1
    while redo == 1:
        choice = int(input("(1) Replace data\n(2) Walk\n(3) Sprint\n(4) Run\n(5) Turn on your generator\n(6) Quit\n? "))
        if choice == 1:
            redo = drink()
        elif choice == 2:
            redo = walk()
        elif choice == 3:
            redo = sprint()
        elif choice == 4:
            redo = run()
        elif choice == 5:
            redo = sleep()
        elif choice == 6:
            exit()
        if choice != 1 and choice != 2 and choice != 3 and choice != 4 and choice != 5 and choice != 6:
            print("Invalid choice")
            redo = 1
def enemy_move():
    global player_stats
    global enemy_distance
    choice = random.randint(2,4)
    if choice == 2:
        enemy_distance = enemy_distance+5
    elif choice == 3:
        enemy_distance = enemy_distance+15
    elif choice == 4:
        enemy_distance = enemy_distance+20
def ckwin():
    global player_stats
    global enemy_distance
    if player_stats[0] <= enemy_distance:
        print("The enemy got you!")
        return 1
    elif player_stats[1] >= 10:
        print("You ran out of data!")
        return 2
    elif player_stats[3] <= 0:
        print("Your HDD ran out of power!")
        return 3
    elif player_stats[0] >= 100:
        print("You made it home!")
        return 0
def progress_bar():
    global player_stats
    global enemy_distance
    enemy_bars_int = enemy_distance-1
    bars = ""
    for x in range(0,enemy_bars_int):
        bars = bars+"_"
    bars = bars+"#"
    player_bars_int = ((player_stats[0]-1)-enemy_bars_int)
    for x in range(0,player_bars_int):
        bars = bars+"_"
    bars = bars+"*"
    bars_fun = 100-(player_stats[0])
    for x in range(0,bars_fun-1):
        bars = bars+"_"
    bars = bars+"|\n"
    print(bars)
def move_anim():
    pass
def drink_anim():
    pass
def gen_anim():
    pass
def win_anim():
    pass
setup()
print("You have stolen a Windows product key from Microsoft HQ. You are racing across the internet to activate your computer.")
game = 1
while game == 1:
    os.system("clear")
    progress_bar()
    mkboard()
    win = ckwin()
    #if win == 1 or win == 2 or win == 3 or win == 0:
    #    time.sleep(2)
    #    setup()
    choose()
    win = ckwin()
   # if win == 1 or win == 2 or win == 3 or win == 0:
   #     time.sleep(2)
   #     setup()
    if choice == 5:
        go = random.randint(0,100)
        if go >= 20 and go <= 30:
            enemy_move()
    else:
        enemy_move()
    win = ckwin()
    if win == 1 or win == 2 or win == 3 or win == 0:
        time.sleep(2)
        setup()
