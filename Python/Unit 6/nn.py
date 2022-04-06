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
            blank_spaces .append(1)
        else:
            blank_spaces.append(0)
    #look for how many spaces i can win agenst
    count = 0
    places_i_can_win_list = []
    places_i_can_win = 0
    for x in blank_spaces:
        new_board_list = orig_board_list
        if x == 1:
            new_board_list[count] = "X"
            win = algor(new_board_list[0], new_board_list[1], new_board_list[2], new_board_list[3], new_board_list[4], new_board_list[5], new_board_list[6], new_board_list[7], new_board_list[8])
            if win == 1:
                places_i_can_win_list.append(1)
                places_i_can_win = places_i_can_win+1
            if win != 1:
                places_i_can_win_list.append(0)
            count = count+1
    if places_i_can_win >= 1:
        #see if i can already win this round in the first layer and submit my turn if i can
        count = 0
        for x in places_i_can_win_list:
            if x == 1:
                orig_board_list[count] = "X"
            count = count+1
        return orig_board_list
    if places_i_can_win == 0:
        #determin the players next move
        count = 0
        places_i_can_win_list = []
        places_i_can_win = 0
        for x in blank_spaces:
            new_board_list = orig_board_list
            if x == 1:
                new_board_list[count] = "O"
                win = algor(new_board_list[0], new_board_list[1], new_board_list[2], new_board_list[3], new_board_list[4], new_board_list[5], new_board_list[6], new_board_list[7], new_board_list[8])
                if win == 1:
                    places_i_can_win_list.append(1)
                    places_i_can_win = places_i_can_win+1
                if win != 1:
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
                count = count+1
                #block there move
            return orig_board_list
        if places_i_can_win == 0:
            #my god i dont want to write 9 layers of AI
            pass
