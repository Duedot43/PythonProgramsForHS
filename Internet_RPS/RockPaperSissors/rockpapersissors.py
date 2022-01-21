def logic(choice, choice2):
    if choice == choice2:
        return ("Tie!")
    if choice == "1":
        if choice2 == "2":
            return ("Player 2 wins!")
        if choice2 == "3":
            return ("Player 1 wins!")
    if choice == "2":
        if choice2 == "1":
            return ("Player 1 wins!")
        if choice2 == "3":
            return ("Player 2 wins!")
    if choice == "3":
        if choice2 == "1":
            return ("Player 2 wins!")
        if choice2 == "2":
            return ("Player 1 wins!")
def choice():
    return ("Now Player take your choice \n (1) rock \n (2) paper \n (3) sissors \n")