import random
#0 ace
#1 "2"
#2 "3"
#3 "4"
#4 "5"
#5 "6"
#6 "7"
#7 "8"
#8 "9"
#9 "jack"
#10 "king"
#11 "queen"
start_cards = {
    0:11,
    1:2,
    2:3,
    3:4,
    4:5,
    5:6,
    6:7,
    7:8,
    8:9,
    9:10,
    10:10,
    11:10

}
alls = {
    "deal":[start_cards[random.randint(0,11)], start_cards[random.randint(0,11)]],
    "play":[start_cards[random.randint(0,11)], start_cards[random.randint(0,11)]]
}
def get_alls(alls, user, xs):
    #user must be deal or play
    output = ""
    count = -1
    for x in alls[user]:
        count = count+1
        if count == 0 and xs:
            output += "X, "
        else:
            output += f"{x}, "
    return output
def plr_move():
    global start_cards, alls
    print(f"You have the cards {get_alls(alls, 'play', False)}")
    print(f"The dealer has the cards {get_alls(alls, 'deal', True)}")
def player_add():
    global start_cards, alls
    alls["play"].append(start_cards[random.randint(0,11)])
def algor(alls):
    play_total = 0
    for x in alls['play']:
        play_total = play_total+x
    deal_total = 0
    for x in alls['deal']:
        deal_total = deal_total+x
    if play_total == 21:
        return [1, "Player wins!"]
    elif deal_total == 21:
        print("Dealer wins!")
        return [2, "Dealer wins!"]
    if deal_total > 21 or play_total > 21:
        return [3, "Someone went over 21!"]
    return [0]
def deal_move():
    global alls, start_cards
    who_big = "play"
    while who_big != "deal":
        deal_total = 0
        for x in alls['deal']:
            deal_total = deal_total+x
        play_total = 0
        for x in alls['play']:
            play_total = play_total+x
        if play_total > deal_total:
            who_big = "play"
        elif deal_total > play_total:
            who_big = "deal"
        if who_big == "play":
            alls['deal'].append(start_cards[random.randint(0,11)])
            print("Dealer is taking a turn")
            return
        else:
            print("dealer stays")
game = 1
while game == 1:
    plr_move()
    choice = input("Stay or move?\n> ")
    while choice.lower() != "stay" and choice.lower() != "move":
        choice = input("Invalid input!\n\nStay or move?\n> ")
    if choice.lower() == "move":
        player_add()
    else:
        deal_move()
    if algor(alls)[0] != 0:
        print(algor(alls)[1])