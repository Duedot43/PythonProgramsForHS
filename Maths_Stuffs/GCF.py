def convert(string):
    list1=[]
    list1[:0]=string
    return list1
def listToString(s): 
    str1 = "" 
    for ele in s: 
        str1 += str(ele)
    return str1
def lts(s): 
    str1 = "" 
    for ele in s: 
        str1 += str(ele + " + ")
    return str1
numbers = int(input("How many numbers?\n"))
topnumlstreal = []
count = 0
equatnum = []
listgo = 0
equatnumreal = []
equatnumlet = []
equatnumletreal = []
topnumlst = []
ogequat = []
while listgo == 0:
    count = count+1
    ranum = str(input("Please input your number:"))
    ogequat.append(ranum)
    ranumlst = convert(ranum)
    equatnum = []
    equatnumlet = []
    counts = -1
    skip = 0
    for x in ranumlst:
        counts = counts+1
        if skip != 1:
            skip = 0
            if x != "^":
                if x.isdigit():
                    equatnum.append(x)
                else:
                    equatnumlet.append(x)
                
            else:
                topnumlst.append(ranumlst[counts+1])
                skip = 1
        else:
            skip = 0
    equatnumstr = listToString(equatnum)
    equatnumreal.append(equatnumstr)
    equatletstr = equatnumlet
    equatnumletreal.append(equatletstr)
    topnumlstreal.append(topnumlst)
    if count == numbers:
        listgo = 1
#equat.sort(reverse=False)
solve = 1
mins = min(equatnumreal)
mins = int(mins)+1
while solve == 1:
    yes = 0
    mins = mins-1
    nums = []
    for x in equatnumreal:
        num = int(x)%int(mins)
        if int(num) == 0:
            ranum = int(int(x)/int(mins))
            nums.append(ranum)
            yes = yes+1
    if yes == len(equatnumreal):
        #print("The GCF is ", mins)
        #print(equatnumreal)
        #print(nums)
        if len(topnumlst) != 0:
            equation = [mins]
            solves = 1
            solvedxlst = []
            while solves == 1:
                countss = -1
                for x in topnumlstreal:
                    countss = countss+1
                    minx = min(x)
                    for y in x:
                        solvedxlst.append(int(y)-int(minx))
                        if int(len(solvedxlst)) == int(len(topnumlst)):
                            break
                    if int(len(solvedxlst)) == int(len(topnumlst)):
                        break
                if int(len(solvedxlst)) == int(len(topnumlst)):
                    break
            if int(len(solvedxlst)) == int(len(topnumlst)):
                print(mins," | ",lts(ogequat))
                second_step = []
                countssss = 0
                while countssss != len(nums):
                    second_step.append(listToString(str(nums[countssss])))
                    let1 = equatnumletreal[countssss]
                    let = listToString(let1)
                    second_step.append(let)
                    second_step.append("^")
                    second_step.append(topnumlst[countssss])
                    countssss = countssss+1
                    if countssss != len(nums):
                        second_step.append(" + ")
                print(minx," | ",listToString(second_step))
                newequat = []
                #for x in range(0,int(len(equatnumreal)+int(len(equatnumletreal)+int(len(topnumlst)*2)))):
                #    print()
                fineq = []
                countsss = 0
                while countsss != len(nums):
                    fineq.append(listToString(str(nums[countsss])))
                    let1 = equatnumletreal[countsss]
                    let = listToString(let1)
                    fineq.append(let)
                    fineq.append("^")
                    fineq.append(listToString(str(solvedxlst[countsss])))
                    countsss = countsss+1
                    if countsss != len(nums):
                        fineq.append(" + ")
                print(listToString(fineq))
                #print(f"I cant re-organize this data so here you go: \n New numbers before the letter {nums}\n letters {equatnumletreal}\n New exponents {solvedxlst}")
                break
        else:
            print("The GCF is ", mins)
            print(equatnumreal)
            print(nums)
            solve = 0
            break

        