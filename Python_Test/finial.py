import os
import random
import roll


def intro():
    # Welcome the player
    global dice, turn
    os.system("clear")
    print("Hello! This is speed yahtzee, the goal of the game is to roll 3 dice and get 3 in a row the dice can be rolled up to 3 times")
    # make the dice variable for all the dice
    dice = [random.randint(1, 6), random.randint(1, 6), random.randint(1, 6)]
    turn = 1
    input("Press ENTER to continue\n")


def disp_dice(die):
    os.system("clear")
    # display the dice using the roll module
    for x in die:
        print(roll.dice(x) + "  ")


def what_keep():
    global dice, turn
    choice = input("What dice would you like to keep? (1~6)\n> ")
    # input validation
    while int(choice) not in dice:  # if that number is not in the dice list it asks again
        choice = input(
            "That is not a valid dice number!\nWhat dice would you like to keep? (1~6)\n> ")
    count = -1
    # re roll the dice
    for x in dice:
        count = count+1
        # only re roll the ones they dont want to keep
        if int(choice) != x:
            dice[count] = random.randint(1, 6)
    # bump up the turn variable
    turn = turn+1


def get_same(dice):
    if dice[0] == dice[1] and dice[1] == dice[2]:
        # if all dice are the same
        return True
    else:
        # if not the same
        return False


def algor(dice):
    global turn
    # if all dice are the same
    if get_same(dice):
        return True
    # if the turn is 3 but the dice arent the same then return False
    if turn == 3 and get_same(dice) == False:
        return False
    # return 3 is there is nothing
    return 3


def win(wins):
    choice = input(f"You {wins}\nPlay again?(Y/N)\n> ")
    # inpud validation for winning
    while str(choice).lower() != "y" and str(choice).lower() != "n":
        print("Invalid input!")  # ask again to get if they want to play agian
        choice = input(f"You {wins}\nPlay again?(Y/N)\n> ")
    if str(choice).lower() == "y":
        # spawn the intro again
        intro()
    else:
        # if they dont want to play again then quit well fine then!
        exit()


game = 1
intro()
while game == 1:
    # game loop
    disp_dice(dice)  # display the dice
    what_keep()  # ask what they want to keep
    algor_out = algor(dice)  # see if they win or not
    if algor_out == True:
        disp_dice(dice)
        win("Win!")
    elif algor_out == False:
        disp_dice(dice)
        win("Loose!")
