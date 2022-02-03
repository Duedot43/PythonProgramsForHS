import random
numbers = int(input("How many numbers?\n"))
count = 0
peoplelst = []
listgo = 0
while listgo == 0:
    count = count+1
    ranum = int(input("Please input your number:"))
    peoplelst.append(ranum)
    if count == numbers:
        listgo = 1
sortedd = peoplelst.sort(reverse=False)
counts = count-1
print("The lowest number is ", peoplelst[0], " and the highest number is ", peoplelst[counts])