import random
print("You will guess the random number from 1 through 20 you will have 4 guesses")
name = str(input("What is your name?\n"))
ranum = random.randint(1,20)
count = 0
while count != 4:
    guess = int(input("Please guess the number:"))
    if guess > 20:
        print("Invalid!")
        exit()
    if guess <= 0:
        print("Invalid!")
        exit()
    if guess == ranum:
        print("Correct that was the right number!")
        print("Nice job", name,"!")
        break
    elif guess != ranum:
        count = count+1
        turns = 4-count
        print("You have", turns, "turns left")
print("The correct number was ", ranum)