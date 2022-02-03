import random
numbers = int(input("How many numbers?\n"))
count = 0
peoplelst = []
listgo = 0
while listgo == 0:
    count = count+1
    ranum = random.randint(-100,100)
    peoplelst.append(ranum)
    if count == numbers+1:
        listgo = 1
sortedd = peoplelst.sort(reverse=False)
counts = count-1
print("The lowest number is ", peoplelst[0], " and the highest number is ", peoplelst[counts])