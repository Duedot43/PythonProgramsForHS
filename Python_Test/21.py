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
def get_alls(alls, user):
    #user must be deal or play
    output = ""
    for x in alls[user]:
        output += f"{x}, "
    return output
def plr_move():
    global start_cards, alls
    print(f"You have {get_alls(alls, 'play')} cards")
    print(f"The dealer has {get_alls(alls, 'deal')} cards")
game = 1
while game == 1:
    pass