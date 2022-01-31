binary = str(input("What would you like to convert?\n"))
def convert(string):
    list1=[]
    list1[:0]=string
    return list1
binarylst = convert(binary)
binarys = len(binarylst)
count = 0
var = []
listgo = 0
while listgo == 0:
    count = count+1
    var.append(" ")
    if count == binarys:
        listgo = 1
#print(count)
thing = 1
counts = 0

while thing == 1:
    binarys = int(binarys)-1
    #counts = int(counts)-1
    count = int(count)-1
    #print(binarylst[count], "*2**", counts)
    why = binarylst[count]
    if why != 1:
        if why != 0:
            print("Invalid!")
            exit()
    var[counts] = int(why) * 2 ** int(counts)
    counts = counts+1
    if count == 0:
        print(sum(i for i in var))
        thing = 0
    