import os
import random
def mkboard():
    global player_stats
    global enemy_distance
    print(f"Distance: {player_stats[0]} Thirst: {player_stats[1]} Drinks left: {player_stats[2]} Enegry: {player_stats[3]}\nEnemy distance: {enemy_distance}")
def ckwin():
    pass
def drink():
    pass
def sleep():
    pass
def walk():
    pass
def sprint():
    pass
def run():
    pass
def setup():
    global player_stats
    global enemy_distance
    player_stats = [0, 0, 5, 10]
    enemy_distance = 0
def choose():
    global player_stats
    global enemy_distance
    choice = int(input("(1) Drink water\n(2) Walk\n(3) Sprint\n(4) Run\n(5) Sleep for the night\n(6) Quit\n? "))
    if choice == 1:
        drink()
    if choice == 2:
        walk()
    if choice == 3:
        sprint()
    if choice == 4:
        run()
    if choice == 5:
        sleep()
    if choice == 6:
        exit()
setup()
game = 1
while game == 1:
    mkboard
    choose()
