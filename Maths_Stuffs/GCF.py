numbers = int(input("How many numbers?\n"))
count = 0
equat = []
listgo = 0
while listgo == 0:
    count = count+1
    ranum = int(input("Please input your number:"))
    equat.append(ranum)
    if count == numbers:
        listgo = 1
equat.sort(reverse=False)
solve = 1
mins = equat[0]
mins = mins+1
while solve == 1:
    yes = 0
    mins = mins-1
    nums = []
    for x in equat:
        num = x%mins
        if int(num) == 0:
            ranum = int(x/mins)
            nums.append(ranum)
            yes = yes+1
    if yes == len(equat):
        print("The GCF is ", mins)
        print(equat)
        print(nums)
        break