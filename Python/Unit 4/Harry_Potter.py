def convert(string):
    list1=[]
    list1[:0]=string
    return list1
def listToString(s): 
    
    # initialize an empty string
    str1 = "" 
    
    # traverse in the string  
    for ele in s: 
        str1 += str(ele)
    
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
quarters = str(quarters)
quarterslst = convert(quarters)
qrt = []
for x in quarterslst:
    if str(x) == str("."):
        break

    qrt.append(int(x))
count = 0
newmon = cantmath
while True:
    if int(listToString(qrt)) == 0:
        break
    count = count+1
    newmon = newmon-25
    if int(count) == int(listToString(qrt)):
        break
dime = int(newmon)/10
dimestr = str(dime)
dimelst = convert(dimestr)
dim = []
for x in dimelst:
    if str(x) == str("."):
        break

    dim.append(int(x))
count = 0
while True:
    if int(listToString(dim)) == 0:
        break
    count = count+1
    newmon = newmon-10
    if int(count) == int(listToString(dim)):
        break
nickle = int(newmon)/5
nicklestr = str(nickle)
nicklelst = convert(nicklestr)
nick = []
for x in nicklelst:
    if str(x) == str("."):
        break

    nick.append(int(x))
count = 0
while True:
    if int(listToString(nick)) == 0:
        break
    count = count+1
    newmon = newmon-5
    if int(count) == int(listToString(nick)):
        break
print(f"{listToString(dol)} Dollors {listToString(qrt)} Quarters {listToString(dim)} Dimes {listToString(nick)} Nickles {newmon} Pennies")