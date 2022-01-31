print("Welcome to Virtual Rock Paper Sissors generic humans!");
print("Player 2 turn around while player 1 makes a choice of rock paper or sissors...");
names = input("May i take player ones name?\n");
names2 = input("May i take player twos name?\n");
game = 1
p1scr = 0
p2scr = 0
while game == 1:
    print("Ok... Player one this is your shot, you need to make the right choice now... Choose! \n (1) rock \n (2) paper \n (3) sissors \n");
    choice = input("?");
    if choice != "1":
        if choice != "2":
            if choice != "3":
                print("Invalid!")
                exit()
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n");
    print("Now Player 2 take your choice \n (1) rock \n (2) paper \n (3) sissors \n");
    choice2 = input("?");
    if choice2 != "1":
        if choice2 != "2":
            if choice2 != "3":
                print("Invalid!")
                exit()
    print("Drumroll please...");
    print("Player 1 (aka ", names, ") chose ", choice, ".");
    print("Player 2 (aka ", names2, ") chose ", choice2, ".");
    if choice == choice2:
        print("Tie!");
    if choice == "1":
        if choice2 == "2":
            print("Player 2 wins!");
            p2scr = p2scr+1
        if choice2 == "3":
            print("Player 1 wins!");
            p1scr = p1scr+1
    if choice == "2":
        if choice2 == "1":
            print("Player 1 wins!");
            p1scr = p1scr+1
        if choice2 == "3":
            print("Player 2 wins!");
            p2scr = p2scr+1
    if choice == "3":
        if choice2 == "1":
            print("Player 2 wins!");
            p2scr = p2scr+1
        if choice2 == "2":
            print("Player 1 wins!");
            p1scr = p1scr+1
    if p1scr == 3:
        p1scr = 0
        p2scr = 0
        play = str(input("Player 1 wins this round!!\nPlay again? (Y/N)\n"))
        play = play.upper()
        if play == "Y":
            p1scr = 0
            p2scr = 0
        if play != "Y":
            if play.upper() != "N":
                print("Invalid!")
    if p2scr == 3:
        p1scr = 0
        p2scr = 0
        play = str(input("Player 2 wins this round!!\nPlay again? (Y/N)\n"))
        play = play.upper()
        if play == "N":
            exit()
        if play != "N":
            if play.upper() != "Y":
                print("Invalid!")
        