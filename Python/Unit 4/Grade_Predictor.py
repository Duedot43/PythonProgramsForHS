
count = 0
tstlst = []
listgo = 0
while listgo == 0:
    count = count+1
    ranum = int(input("What is your test grade?\n"))
    tstlst.append(ranum)
    if count == 4:
        listgo = 1
count = 0
asmntlst = []
listgo = 0
while listgo == 0:
    count = count+1
    ranum = int(input("What is your assignment grade?\n"))
    asmntlst.append(ranum)
    if count == 4:
        listgo = 1

tstavg = sum(tstlst)
asmntavg = sum(asmntlst)
