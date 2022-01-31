people = int(input("Pick a number, any number!"))
count = 0
peoplelst = []
listgo = 0
while listgo == 0:
    count = count+1
    peoplelst.append(count)
    if count == people:
        listgo = 1
count = 0
fizzbuzzlst = []
listgo = 0
while listgo == 0:
    count = count+1
    fizzbuzzlst.append(" ")
    if count == people:
        listgo = 1
x = 0
while x != people:
    sets = 0
    thing = peoplelst[x]
    bob = thing % 3
    joe = thing % 5
    print(thing % 3, ".", thing, " %3")
    print(thing % 5, ".", thing, " %5")
    if bob == 0:
        if joe == 0:
            fizzbuzzlst[x] = "FizzBuzz"
            sets = 1
    if bob == 0:
        if sets != 1:
            fizzbuzzlst[x] = "Fizz"
            sets = 1
    if joe == 0:
        if sets != 1:
            fizzbuzzlst[x] = "Buzz"
            sets = 1
    #if sets == 0:
        #fizzbuzzlst[x] = "bug"
    x = x+1
print(fizzbuzzlst)
