print("Welcome to Virtual Rock Paper Sissors generic humans!");
print("Player 2 turn around while player 1 makes a choice of rock paper or sissors...");
names = input("May i take player ones name?\n");
names2 = input("May i take player twos name?\n");
print("Ok... Player one this is your shot, you need to make the right choice now... Choose! \n (1) rock \n (2) paper \n (3) sissors \n");
choice = input("?");
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n");
print("Now Player 2 take your choice \n (1) rock \n (2) paper \n (3) sissors \n");
choice2 = input("?");
print("Drumroll please...");
print("Player 1 (aka ", names, ") chose ", choice, ".");
print("Player 2 (aka ", names2, ") chose ", choice2, ".");
if choice == choice2:
    print("Tie!");
if choice == "1":
    if choice2 == "2":
        print("Player 2 wins!");
    if choice2 == "3":
        print("Player 1 wins!");
if choice == "2":
    if choice2 == "1":
        print("Player 1 wins!");
    if choice2 == "3":
        print("Player 2 wins!");
if choice == "3":
    if choice2 == "1":
        print("Player 2 wins!");
    if choice2 == "2":
        print("Player 1 wins!");