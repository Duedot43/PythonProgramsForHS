import os

#Old code from like 4 years ago
def grade(precent):
    precent = float(precent)
    if precent >float(92):
        return ("A")
    elif precent >float(89):
        return ("A-")
    elif precent >float(86):
        return ("B+")
    elif precent >float(82):
        return ("B")
    elif precent >float(79):
        return ("B-")
    elif precent >float(76):
        return ("C+")
    elif precent >float(72):
        return ("C")
    elif precent >float(69):
        return ("C-")
    elif precent >float(66):
        return ("D+")
    elif precent >float(62):
        return ("D")
    elif precent >float(59):
        return ("D-")
    elif precent <float(58):
        return ("F")

    #Old code from like 4 years ago
count = 0
tstlst = []
listgo = 0
while listgo == 0:
    count = count+1
    ranum = float(input("What is your test grade?\n"))
    tstlst.append(ranum)
    if count == 3:
        listgo = 1
count = 0
asmntlst = []
listgo = 0
while listgo == 0:
    count = count+1
    ranum = float(input("What is your assignment grade?\n"))
    asmntlst.append(ranum)
    if count == 4:
        listgo = 1

tstavg = sum(tstlst)/float(3)
asmntavg = sum(asmntlst)/float(4)
tstlst.sort(reverse=False)
asmntlst.sort(reverse=False)
fingrd = (0.6 * tstavg + 0.4 * (asmntavg*2))
os.system("clear")
fingrd = str(fingrd)
print("Overall" + fingrd +"%", grade(fingrd))
print("Your lowest test score is", tstlst[0], "your highest test score is", tstlst[2])
print("Your lowest assignment score is", asmntlst[0], "your highest test score is", asmntlst[3])