import random
import os
def algor(a1, a2, a3, b1, b2, b3, c1, c2, c3):
        win = "_"
        #branch left
        if a1 == "O":
            if a2 == "O":
                if a3 == "O":
                    win = "O"
            if b2 == "O":
                if c3 == "O":
                    win = "O"
            if b1 == "O":
                if c1 == "O":
                    win = "O"
        #branch right
        if c1 == "O":
            if c2 == "O":
                if c3 == "O":
                    win = "O"
            if b2 == "O":
                if a3 == "O":
                    win = "O"
        #middle up down
        if b1 == "O":
            if b2 == "O":
                if b3 == "O":
                    win = "O"
        #middle left right
        if a2 == "O":
            if b2 == "O":
                if c2 == "O":
                    win = "O"
        #bottom left right
        if a3 == "O":
            if b3 == "O":
                if c3 == "O":
                    win = "O"


        #branch left
        if a1 == "X":
            if a2 == "X":
                if a3 == "X":
                    win = "X"
            if b2 == "X":
                if c3 == "X":
                    win = "X"
            if b1 == "X":
                if c1 == "X":
                    win = "X"
        #branch right
        if c1 == "X":
            if c2 == "X":
                if c3 == "X":
                    win = "X"
            if b2 == "X":
                if a3 == "X":
                    win = "X"
        #middle up down
        if b1 == "X":
            if b2 == "X":
                if b3 == "X":
                    win = "X"
        #middle left right
        if a2 == "X":
            if b2 == "X":
                if c2 == "X":
                    win = "X"
        #bottom left right
        if a3 == "X":
            if b3 == "X":
                if c3 == "X":
                    win = "X"
        wincalc1 = 0
        wincalc2 = 0
        wincalc3 = 0
        wincalc4 = 0
        wincalc5 = 0
        wincalc6 = 0
        wincalc7 = 0
        wincalc8 = 0
        wincalc9 = 0
    
        if a1 != "_":
            wincalc1 = 3
        if a2 != "_":
            wincalc2 = 3
        if a3 != "_":
            wincalc3 = 3
        if b1 != "_":
            wincalc4 = 3
        if b2 != "_":
            wincalc5 = 3
        if b3 != "_":
            wincalc6 = 3
        if c1 != "_":
            wincalc7 = 3
        if c2 != "_":
            wincalc8 = 3
        if c3 != "_":
            wincalc9 = 3
        tieround = wincalc1+wincalc2+wincalc3+wincalc4+wincalc5+wincalc6+wincalc7+wincalc8+wincalc9
        tieround = int(tieround)
        if tieround == 27:
            win = "T"
        if tieround != 27:
            wins = "N"

        #algorithm

        if win == "X":
            win = 1
            win = int(win)
        if win == "O":
            win = 2
            win = int(win)
        if win == "_":
            win = 3
            win = int(win)
        if win == "T":
            win = 0
            win = int(win)
        #print("win=", win)
       
        return win
def ai(a1, a2, a3, b1, b2, b3, c1, c2, c3):
    orig_board_list = [a1, a2, a3, b1, b2, b3, c1, c2, c3]
    blank_spaces = []
    for x in orig_board_list:
        if x == "_":
            blank_spaces.append(1)
        else:
            blank_spaces.append(0)
    #look for how many spaces i can win agenst
    count = 0
    places_i_can_win_list = []
    places_i_can_win = 0
    for x in blank_spaces:
        new_board_list = []
        new_board_list = [a1, a2, a3, b1, b2, b3, c1, c2, c3]
        if x == 1:
            new_board_list[count] = "X"
            win = algor(new_board_list[0], new_board_list[1], new_board_list[2], new_board_list[3], new_board_list[4], new_board_list[5], new_board_list[6], new_board_list[7], new_board_list[8])
            if win == 1:
                places_i_can_win_list.append(1)
                places_i_can_win = places_i_can_win+1
            if win != 1:
                places_i_can_win_list.append(0)
        if x != 1:
            places_i_can_win_list.append(0)
        count = count+1
    if places_i_can_win >= 1:
        #see if i can already win this round in the first layer and submit my turn if i can
        count = 0
        for x in places_i_can_win_list:
            if x == 1:
                orig_board_list[count] = "X"
                return orig_board_list
            count = count+1
    if places_i_can_win == 0:
        #determin the players next move
        blank_spaces = []
        for x in orig_board_list:
            if x == "_":
                blank_spaces.append(1)
            else:
                blank_spaces.append(0)
        count = 0
        places_i_can_win_list = []
        places_i_can_win = 0
        for x in blank_spaces:
            new_board_list = []
            new_board_list = [a1, a2, a3, b1, b2, b3, c1, c2, c3]
            if x == 1:
                new_board_list[count] = "O"
                win = algor(new_board_list[0], new_board_list[1], new_board_list[2], new_board_list[3], new_board_list[4], new_board_list[5], new_board_list[6], new_board_list[7], new_board_list[8])
                if win == 2:
                    places_i_can_win_list.append(1)
                    places_i_can_win = places_i_can_win+1
                if win != 2:
                    places_i_can_win_list.append(0)
            if x != 1:
                places_i_can_win_list.append(0)
            count = count+1
        if places_i_can_win >= 2:
            print("Screw you.")
            return 0
        if places_i_can_win == 1:
            count = 0
            for x in places_i_can_win_list:
                if x == 1:
                    orig_board_list[count] = "X"
                    return orig_board_list
                count = count+1
                #block there move
    #now for the real AI
    blank_spaces = []
    for x in orig_board_list:
        if x == "_":
            blank_spaces.append(1)
        else:
            blank_spaces.append(0)
    new_board_list = []
    new_board_list = [a1, a2, a3, b1, b2, b3, c1, c2, c3]
    count = 0
    new_placements = []
    for x in blank_spaces:
        if x == 1:
            layer = 1
            new_board_list = []
            new_board_list = [a1, a2, a3, b1, b2, b3, c1, c2, c3]
            new_board_list[count] = "X"
            win = algor(new_board_list[0], new_board_list[1], new_board_list[2], new_board_list[3], new_board_list[4], new_board_list[5], new_board_list[6], new_board_list[7], new_board_list[8])
            counte = 0
            if win == 0:
                for e in blank_spaces:
                    if e == 1:
                        orig_board_list[counte] = "X"
                    counte = counte+1
                    #block there move
                return orig_board_list
            new_placements.append(count)
            blank_spaces_new = []
            for x in new_board_list:
                if x == "_":
                    blank_spaces_new.append(1)
                else:
                    blank_spaces_new.append(0)
            counts = 0
            for p in blank_spaces_new:
                if p == 1:
                    new_board_list[counts] = "O"
                    win = algor(new_board_list[0], new_board_list[1], new_board_list[2], new_board_list[3], new_board_list[4], new_board_list[5], new_board_list[6], new_board_list[7], new_board_list[8])
                    if win == 1 or win == 2:
                        if win == 1:
                            orig_board_list[counts] = "X"
                            return orig_board_list
                        if win == 2:
                            orig_board_list[counts] = "X"
                            return orig_board_list
                    blank_spaces_new_new = []

                    ###############################

                    for x in new_board_list:
                        if x == "_":
                            blank_spaces_new_new.append(1)
                        else:
                            blank_spaces_new_new.append(0)
                    countss = 0
                    for t in blank_spaces_new_new:
                        if t == 1:
                            new_board_list[countss] = "X"
                            win = algor(new_board_list[0], new_board_list[1], new_board_list[2], new_board_list[3], new_board_list[4], new_board_list[5], new_board_list[6], new_board_list[7], new_board_list[8])
                            if win == 1 or win == 2:
                                if win == 1:
                                    orig_board_list[countss] = "X"
                                    return orig_board_list
                                if win == 2:
                                    orig_board_list[countss] = "X"
                                    return orig_board_list
                            
                    
                    #####################################

                        ##############################
                            blank_spaces_new_new_new = []
                            for x in new_board_list:
                                if x == "_":
                                    blank_spaces_new_new_new.append(1)
                                else:
                                    blank_spaces_new_new_new.append(0)
                            countsss = 0
                            for h in blank_spaces_new_new_new:
                                if h == 1:
                                    new_board_list[countsss] = "O"
                                    win = algor(new_board_list[0], new_board_list[1], new_board_list[2], new_board_list[3], new_board_list[4], new_board_list[5], new_board_list[6], new_board_list[7], new_board_list[8])
                                    if win == 1 or win == 2:
                                        if win == 1:
                                            orig_board_list[countsss] = "X"
                                            return orig_board_list
                                        if win == 2:
                                            orig_board_list[countsss] = "X"
                                            return orig_board_list
                                    new_board_list[countsss] = "_"
                                countsss = countsss+1

                                ########################################

                            new_board_list[countss] = "_"
                        countss = countss+1
                counts = counts+1
        count = count+1
    bak_move = random.randint(0,8)
    orig_board_list = [a1, a2, a3, b1, b2, b3, c1, c2, c3]
    while "X" == orig_board_list[bak_move] and "O" == orig_board_list[bak_move]:
        bak_move = random.randint(0,8)
    orig_board_list[bak_move] = "X"
    return orig_board_list
def ai_DEMO(a1, a2, a3, b1, b2, b3, c1, c2, c3):
    orig_board_list = [a1, a2, a3, b1, b2, b3, c1, c2, c3]
    os.system("clear")
    print("First it compiles the board data into a single list called orig_board_list this is done for easer sorting.\norig_board_list", orig_board_list)
    input()
    blank_spaces = []
    for x in orig_board_list:
        if x == "_":
            blank_spaces.append(1)
        else:
            blank_spaces.append(0)
    os.system("clear")
    print("Then it looks for free spaces and puts that in a list called blank_spaces\norig_board_list", orig_board_list, "\nblank_spaces", blank_spaces)
    input()
    #look for how many spaces i can win agenst
    count = 0
    places_i_can_win_list = []
    places_i_can_win = 0
    for x in blank_spaces:
        new_board_list = []
        new_board_list = [a1, a2, a3, b1, b2, b3, c1, c2, c3]
        if x == 1:
            new_board_list[count] = "X"
            win = algor(new_board_list[0], new_board_list[1], new_board_list[2], new_board_list[3], new_board_list[4], new_board_list[5], new_board_list[6], new_board_list[7], new_board_list[8])
            if win == 1:
                places_i_can_win_list.append(1)
                places_i_can_win = places_i_can_win+1
            if win != 1:
                places_i_can_win_list.append(0)
        if x != 1:
            places_i_can_win_list.append(0)
        count = count+1
    os.system("clear")
    print("Using those blank spaces it puts an X in each blank spot with a new list called new_board_list then puts it through algor to count how many wins it gets\nif it gets a win it makes its turn in that spot\norig_board_list", orig_board_list, "\nblank_spaces", blank_spaces, "\nnew_board_list", new_board_list, "\nplaces_i_can_win", places_i_can_win, "\nplaces_i_can_win_list", places_i_can_win_list)
    input()
    if places_i_can_win >= 1:
        #see if i can already win this round in the first layer and submit my turn if i can
        count = 0
        for x in places_i_can_win_list:
            if x == 1:
                os.system("clear")
                print("It appears the bot has decided to win!\norig_board_list", orig_board_list, "\nblank_spaces", blank_spaces, "\nnew_board_list", new_board_list, "\nplaces_i_can_win", places_i_can_win, "\nplaces_i_can_win_list", places_i_can_win_list)
                input()
                orig_board_list[count] = "X"
                return orig_board_list
            count = count+1
    if places_i_can_win == 0:
        os.system("clear")
        print("The bot has decided it cant win! it will see if the player has a positility to win if so block that move\norig_board_list", orig_board_list, "\nblank_spaces", blank_spaces, "\nnew_board_list", new_board_list, "\nplaces_i_can_win", places_i_can_win, "\nplaces_i_can_win_list", places_i_can_win_list)
        input()
        #determin the players next move
        blank_spaces = []
        for x in orig_board_list:
            if x == "_":
                blank_spaces.append(1)
            else:
                blank_spaces.append(0)
        os.system("clear")
        print("Then it looks for free spaces and puts that in a list called blank_spaces\norig_board_list", orig_board_list, "\nblank_spaces", blank_spaces)
        input()
        count = 0
        places_i_can_win_list = []
        places_i_can_win = 0
        for x in blank_spaces:
            new_board_list = []
            new_board_list = [a1, a2, a3, b1, b2, b3, c1, c2, c3]
            if x == 1:
                new_board_list[count] = "O"
                win = algor(new_board_list[0], new_board_list[1], new_board_list[2], new_board_list[3], new_board_list[4], new_board_list[5], new_board_list[6], new_board_list[7], new_board_list[8])
                if win == 2:
                    places_i_can_win_list.append(1)
                    places_i_can_win = places_i_can_win+1
                if win != 2:
                    places_i_can_win_list.append(0)
            if x != 1:
                places_i_can_win_list.append(0)
            count = count+1
        os.system("clear")
        print("Using those blank spaces it puts an X in each blank spot with a new list called new_board_list then puts it through algor to count how many wins it gets\nif it gets a win it makes its turn in that spot\norig_board_list", orig_board_list, "\nblank_spaces", blank_spaces, "\nnew_board_list", new_board_list, "\nplaces_i_can_win", places_i_can_win, "\nplaces_i_can_win_list", places_i_can_win_list)
        input()
        if places_i_can_win >= 2:
            os.system("clear")
            print("Screw you.")
            print("The bot has given up!!")
            input()
            return 0
        if places_i_can_win == 1:
            count = 0
            for x in places_i_can_win_list:
                if x == 1:
                    orig_board_list[count] = "X"
                    os.system("clear")
                    print("It appears the bot has decided the player win! It will now blobk this move.\norig_board_list", orig_board_list, "\nblank_spaces", blank_spaces, "\nnew_board_list", new_board_list, "\nplaces_i_can_win", places_i_can_win, "\nplaces_i_can_win_list", places_i_can_win_list)
                    input()
                    return orig_board_list
                count = count+1
                #block there move
    #now for the real AI
    blank_spaces = []
    for x in orig_board_list:
        if x == "_":
            blank_spaces.append(1)
        else:
            blank_spaces.append(0)
    new_board_list = []
    new_board_list = [a1, a2, a3, b1, b2, b3, c1, c2, c3]
    count = 0
    new_placements = []
    for x in blank_spaces:
        if x == 1:
            layer = 1
            new_board_list = []
            new_board_list = [a1, a2, a3, b1, b2, b3, c1, c2, c3]
            new_board_list[count] = "X"
            win = algor(new_board_list[0], new_board_list[1], new_board_list[2], new_board_list[3], new_board_list[4], new_board_list[5], new_board_list[6], new_board_list[7], new_board_list[8])
            counte = 0
            if win == 0:
                for e in blank_spaces:
                    if e == 1:
                        orig_board_list[counte] = "X"
                    counte = counte+1
                    #block there move
                return orig_board_list
            new_placements.append(count)
            blank_spaces_new = []
            for x in new_board_list:
                if x == "_":
                    blank_spaces_new.append(1)
                else:
                    blank_spaces_new.append(0)
            counts = 0
            for p in blank_spaces_new:
                if p == 1:
                    new_board_list[counts] = "O"
                    win = algor(new_board_list[0], new_board_list[1], new_board_list[2], new_board_list[3], new_board_list[4], new_board_list[5], new_board_list[6], new_board_list[7], new_board_list[8])
                    if win == 1 or win == 2:
                        if win == 1:
                            orig_board_list[counts] = "X"
                            os.system("clear")
                            print("The bot has stopped at layer 1\norig_board_list", orig_board_list, "\nblank_spaces", blank_spaces, "\nnew_board_list", new_board_list, "\nplaces_i_can_win", places_i_can_win, "\nplaces_i_can_win_list", places_i_can_win_list, "\nblank_spaces_new", blank_spaces_new, "\ncount", count)
                            input()
                            return orig_board_list
                        if win == 2:
                            orig_board_list[counts] = "X"
                            os.system("clear")
                            print("The bot has stopped at layer 1\norig_board_list", orig_board_list, "\nblank_spaces", blank_spaces, "\nnew_board_list", new_board_list, "\nplaces_i_can_win", places_i_can_win, "\nplaces_i_can_win_list", places_i_can_win_list, "\nblank_spaces_new", blank_spaces_new, "\ncount", count)
                            input()
                            return orig_board_list
                    blank_spaces_new_new = []

                    ###############################

                    for x in new_board_list:
                        if x == "_":
                            blank_spaces_new_new.append(1)
                        else:
                            blank_spaces_new_new.append(0)
                    countss = 0
                    for t in blank_spaces_new_new:
                        if t == 1:
                            new_board_list[countss] = "X"
                            win = algor(new_board_list[0], new_board_list[1], new_board_list[2], new_board_list[3], new_board_list[4], new_board_list[5], new_board_list[6], new_board_list[7], new_board_list[8])
                            if win == 1 or win == 2:
                                if win == 1:
                                    orig_board_list[countss] = "X"
                                    os.system("clear")
                                    print("The bot has stopped at layer 2\norig_board_list", orig_board_list, "\nblank_spaces", blank_spaces, "\nnew_board_list", new_board_list, "\nplaces_i_can_win", places_i_can_win, "\nplaces_i_can_win_list", places_i_can_win_list, "\nblank_spaces_new", blank_spaces_new, "\ncount", count, "\nblank_spaces_new_new", blank_spaces_new_new, "countss", countss)
                                    input()
                                    return orig_board_list
                                if win == 2:
                                    orig_board_list[countss] = "X"
                                    os.system("clear")
                                    print("The bot has stopped at layer 2\norig_board_list", orig_board_list, "\nblank_spaces", blank_spaces, "\nnew_board_list", new_board_list, "\nplaces_i_can_win", places_i_can_win, "\nplaces_i_can_win_list", places_i_can_win_list, "\nblank_spaces_new", blank_spaces_new, "\ncount", count, "\nblank_spaces_new_new", blank_spaces_new_new, "countss", countss)
                                    input()
                                    return orig_board_list
                            
                    
                    #####################################

                        ##############################
                            blank_spaces_new_new_new = []
                            for x in new_board_list:
                                if x == "_":
                                    blank_spaces_new_new_new.append(1)
                                else:
                                    blank_spaces_new_new_new.append(0)
                            countsss = 0
                            for h in blank_spaces_new_new_new:
                                if h == 1:
                                    new_board_list[countsss] = "O"
                                    win = algor(new_board_list[0], new_board_list[1], new_board_list[2], new_board_list[3], new_board_list[4], new_board_list[5], new_board_list[6], new_board_list[7], new_board_list[8])
                                    if win == 1 or win == 2:
                                        if win == 1:
                                            orig_board_list[countsss] = "X"
                                            os.system("clear")
                                            print("The bot has stopped at layer 3\norig_board_list", orig_board_list, "\nblank_spaces", blank_spaces, "\nnew_board_list", new_board_list, "\nplaces_i_can_win", places_i_can_win, "\nplaces_i_can_win_list", places_i_can_win_list, "\nblank_spaces_new", blank_spaces_new, "\ncount", count, "\nblank_spaces_new_new", blank_spaces_new_new, "countss", countss, "\nblank_spaces_new_new_new", blank_spaces_new_new_new, "countsss", countsss)
                                            input()
                                            return orig_board_list
                                        if win == 2:
                                            orig_board_list[countsss] = "X"
                                            os.system("clear")
                                            print("The bot has stopped at layer 3\norig_board_list", orig_board_list, "\nblank_spaces", blank_spaces, "\nnew_board_list", new_board_list, "\nplaces_i_can_win", places_i_can_win, "\nplaces_i_can_win_list", places_i_can_win_list, "\nblank_spaces_new", blank_spaces_new, "\ncount", count, "\nblank_spaces_new_new", blank_spaces_new_new, "countss", countss, "\nblank_spaces_new_new_new", blank_spaces_new_new_new, "countsss", countsss)
                                            input()
                                            return orig_board_list
                                    new_board_list[countsss] = "_"
                                countsss = countsss+1

                                ########################################

                            new_board_list[countss] = "_"
                        countss = countss+1
                counts = counts+1
        count = count+1
    bak_move = random.randint(0,8)
    orig_board_list = [a1, a2, a3, b1, b2, b3, c1, c2, c3]
    while "X" == orig_board_list[bak_move] and "O" == orig_board_list[bak_move]:
        bak_move = random.randint(0,8)
    orig_board_list[bak_move] = "X"
    print("THE BOT HAS DECIDED IT CANNOT MAKE A LOGIC MOVE THIS IS VERY RARE IT WILL PICK A RANDOM SPOT\norig_board_list", orig_board_list, "\nblank_spaces", blank_spaces, "\nnew_board_list", new_board_list, "\nplaces_i_can_win", places_i_can_win, "\nplaces_i_can_win_list", places_i_can_win_list)
    return orig_board_list
#thing = ai("X", "X", "_", "_", "X", "X", "X", "X", "O")
#print(thing)