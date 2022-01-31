import random
import os
import math
def algor1(p1guess, p1win, win):
    if p1guess > 100:
        print("Invalid!")
        exit()
    if p1guess <= 0:
        print("Invalid!")
        exit()
    if p1guess == win:
        print("Player 1 won this round!")
        p1win = p1win+1
        return p1win
    if p1guess != win:
        print("Player 1 lost this round")
        return p1win
def algor2(p2guess, p2win, win):
    if p2guess > 100:
        print("Invalid!")
        exit()
    if p2guess <= 0:
        print("Invalid!")
        exit()
    if p2guess == win:
        print("Player 2 won this round!")
        p2win = p2win+1
        return p2win
    if p2guess != win:
        print("Player 2 lost this round")
        return p2win
def close(lst, rnum):
    tf = min(lst, key=lambda x:abs(x-rnum))
    return tf
def mklst(num1, num2):
    lst = []
    lst.append(num1)
    lst.append(num2)
    return lst
print("You will guess the random number from 1 through 100 you will have till 5 points")
name = str(input("Player 1 what is your name?\n"))
name2 = str(input("Player 2 what is your name>\n"))
game = 1
p1win = 0
p2win = 0
while game == 1:
    ranum = random.randint(1,100)
    count = 0
    pturn = random.randint(1,2)
    if pturn == 1:
        print("Player 1 its your turn!")
        p1guess = int(input("Guess the number: "))
        print("Player 2 its your turn!")
        p2guess = int(input("Guess the number: "))
        os.system("clear")
        if p1guess != p2guess:
            lst = mklst(p1guess, p2guess)
            win = close(lst, ranum)
            
            p1win = algor1(p1guess, p1win, win)
            p2win = algor2(p2guess, p2win, win)
            if p1win == 5:
                print("Player 1 won!")
                again = int(input("Play again? \n (1) Yes\n(2) No\n?"))
                if again == 1:
                    p1win = 0
                    p2win = 0
                if again == 2:
                    game = 0
                    exit()
            if p2win == 5:
                print("Player 2 won!")
                again = int(input("Play again? \n (1) Yes\n(2) No\n?"))
                if again == 1:
                    p1win = 0
                    p2win = 0
                if again == 2:
                    game = 0
                    exit()
    if pturn == 2:
        print("Player 2 its your turn!")
        p2guess = int(input("Guess the number: "))
        print("Player 1 its your turn!")
        p1guess = int(input("Guess the number: "))
        os.system("clear")
        if p1guess != p2guess:
            lst = mklst(p1guess, p2guess)
            win = close(lst, ranum)
            
            p1win = algor1(p1guess, p1win, win)
            p2win = algor2(p2guess, p2win, win)
            if p1win == 5:
                print("Player 1 won!")
                again = int(input("Play again? \n (1) Yes\n(2) No\n?"))
                if again == 1:
                    p1win = 0
                    p2win = 0
                if again == 2:
                    game = 0
                    exit()
            if p2win == 5:
                print("Player 2 won!")
                again = int(input("Play again? \n (1) Yes\n(2) No\n?"))
                if again == 1:
                    p1win = 0
                    p2win = 0
                if again == 2:
                    game = 0
                    exit()
    