#Intro
print("Welcome to the High School age calculator!")
age = int(input("How old are you?\n:"))
if age < 15:
    print("You are not old enough to be in high school")
if age >= 15:
    if age < 16:
        print("You are most likely a freshman!")
if age >= 16:
    if age < 17:
        print("You are most likley a sophomore")
if age >= 17:
    if age < 18:
        print("You are most likley a junior")
if age >= 18:
    if age <= 19:
        print("You are most likley a senior")
if age > 19:
    print("You are too old for High School")