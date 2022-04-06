import os 
import random
def ai():
    global choice
    global round_ct
    global plr_choice_all
    global fir_conf
    win = 0
    avg = 0
    num = 3
    if round_ct == 1:
        how_many = len(plr_choice_all)
        while how_many%3 != 0:
            how_many = how_many-1
        avg = avg+plr_choice_all[0]
        for x in range(1,int(how_many/3)):
            avg = avg+plr_choice_all[num]
            num = num+3
        divide = how_many/3
        avg_plr_choice = avg/divide
        avg_plr_choice = int(avg_plr_choice)
        num = 0
        if avg_plr_choice == 1:
            fir_conf = ai_conf(1, 2, how_many, num)
            return 2
        elif avg_plr_choice == 2:
            fir_conf = ai_conf(1, 3, how_many,num)
            return 3
        elif avg_plr_choice == 3:
            fir_conf = ai_conf(1, 1, how_many,num)
    if round_ct == 2:
        how_many = len(plr_choice_all)
        while how_many%3 != 0:
            how_many = how_many-1
        avg = avg+plr_choice_all[1]
        num = 4
        for x in range(1,int(how_many/3)):
            avg = avg+plr_choice_all[num]
            num = num+3
        divide = how_many/3
        avg_plr_choice = avg/int(divide)
        avg_plr_choice = int(avg_plr_choice)
        num = 1
        if avg_plr_choice == 1:
            fir_conf = ai_conf(1, 2, how_many, 1)
            return 2
        elif avg_plr_choice == 2:
            fir_conf = ai_conf(1, 3, how_many,1)
            return 3
        elif avg_plr_choice == 3:
            fir_conf = ai_conf(1, 1, how_many,1)
            return 1
    if round_ct == 3:
        how_many = len(plr_choice_all)
        while how_many%3 != 0:
            how_many = how_many-1
        avg = avg+plr_choice_all[2]
        num = 5
        for x in range(1,int(how_many/3)):
            avg = avg+plr_choice_all[num]
            num = num+3
        divide = how_many/3
        avg_plr_choice = avg/divide
        avg_plr_choice = int(avg_plr_choice)
        num = 2
        if avg_plr_choice == 1:
            fir_conf = ai_conf(1, 2, how_many, num)
            return 2
        elif avg_plr_choice == 2:
            fir_conf = ai_conf(1, 3, how_many,num)
            return 3
        elif avg_plr_choice == 3:
            fir_conf = ai_conf(1, 1, how_many,num)
            return 1
def advanced_ai():
    global choice
    global round_ct
    global plr_choice_all   
    global fir_conf
    global sec_conf
def stupid_advanced_ai():
    global choice
    global round_ct
    global plr_choice_all
    global plr_win_ct
    global bot_win_ct
    global fir_conf
    global sec_conf
    global thir_conf
def ai_conf(request, bot_choice,how_many,num ):
    global choice
    global round_ct
    global plr_choice_all
    global plr_win_ct
    global bot_win_ct
    win = 0
    if request == 1:
        for x in range(0,int(how_many/3)):
            plr_ch = plr_choice_all[num]
            num = num+3
            if plr_ch == 1:
                if bot_choice == 1:
                    tie = 1
                elif bot_choice == 2:
                    win = win+1
                elif bot_choice == 3:
                    tie = 1
            elif plr_ch == 2:
                if bot_choice == 1:
                    tie = 1
                elif bot_choice == 2:
                    tie = 1
                elif bot_choice == 3:
                    win = win+1
            if plr_ch == 3:
                if bot_choice == 1:
                    win = win+1
                elif bot_choice == 2:
                    tie = 1
                elif bot_choice == 3:
                    tie = 1
        return win/(how_many/3)
def algor():
    global choice
    global bot_choice
    global bot_win_ct
    global plr_win_ct
    if choice == 1:
        if bot_choice == 1:
            print("\nTie!\n")
        if bot_choice == 2:
            print("\nThe bot chose paper!\n\nThe bot wins!\n")
            bot_win_ct = bot_win_ct+1
        if bot_choice == 3:
            print("\nThe bot chose sissors!\n\nYou win!\n")
            plr_win_ct = plr_win_ct+1
    if choice == 2:
        if bot_choice == 1:
            print("\nThe bot chose rock!\n\nYou win!\n")
            plr_win_ct = plr_win_ct+1
        if bot_choice == 2:
            print("\nTie!\n")
        if bot_choice == 3:
            print("\nThe bot chose sissors!\n\nThe bot wins!\n")
            bot_win_ct = bot_win_ct+1
    if choice == 3:
        if bot_choice == 1:
            print("\nThe bot chose rock!\n\nThe bot wins!\n")
            bot_win_ct = bot_win_ct+1
        if bot_choice == 2:
            print("\nThe bot chose paper!\n\nYou win!\n")
            plr_win_ct = plr_win_ct+1
        if bot_choice == 3:
            print("\nTie!\n")
            
plr_choice_all = []
game = 1
plr_win_ct = 0
bot_win_ct = 0
round_ct = 1
trainer_mode = 0
one_ten = [0,0,0]
two_ten = [0,0,0]
three_ten = [0,0,0]
while game == 1:
    if trainer_mode == 0:
        choice = int(input(("Make a choice...\n(1) Rock\n(2) Paper\n(3) Sissors\n? ")))
    else:
        pass
    if int(len(plr_choice_all)) <= 5:
        bot_choice = random.randint(1,3)
    else:
        bot_choice = ai()
        print(fir_conf)
    plr_choice_all.append(choice)
    os.system("clear")
    algor()
    if round_ct >= 3:
        round_ct = 1
    else:
        round_ct = round_ct+1
    