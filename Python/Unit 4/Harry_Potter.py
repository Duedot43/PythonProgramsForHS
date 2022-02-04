def convert(string):
    list1=[]
    list1[:0]=string
    return list1
def listToString(s): 
    
    # initialize an empty string
    str1 = "" 
    
    # traverse in the string  
    for ele in s: 
        str1 += ele  
    
    # return string  
    return str1
money = str(input("Money?\n"))
money = float(money)/float(100)
money = str(money)
moneylst = convert(money)
dol = []
cent = []
dot = 0
for x in moneylst:
    if str(x) == str("."):
        dot = 1
    if dot != 1:
        dol.append(int(x))
    if dot == 1:
        if str(x) == str("."):
            continue
        if str(x) != str("."):
            cent.append(str(x))
centmath = listToString(cent)
cantmath = int(centmath)
quarters = float(cantmath)/float(25)
quarterslst = convert(quarters)
qrt = []
for x in quarterslst:
    if str(x) == str("."):
        break
    if dot != 1:
        qrt.append(int(x))
