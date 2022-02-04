import random
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
with open("share/Word_Guess/words.txt", "r") as file:
    allText = file.read()
    words = list(map(str, allText.split()))
  
    # print random string
word = random.choice(words)
turn = 0

wordlst = convert(word)
ammount = len(wordlst)
count = 0
peoplelst = []
listgo = 0
while listgo == 0:
    count = count+1
    peoplelst.append("? ")
    if count == ammount:
        listgo = 1
turn = 0
correctins = 0
while turn != 10:
    if correctins == len(wordlst):
        break
    stri = listToString(peoplelst)
    print(stri)
    guess = str(input("Guess a letter!\n:"))
    guesslst = convert(guess)
    ckthing = -0
    count = -1
    ignoreincorrect = 0
    for x in wordlst:
        count = count +1
        realwrdlow = x.lower()
        guess = guesslst[0]
        guess = guess.lower()
        if str(realwrdlow) == str(guess):
            print("Correct!")
            correctins = correctins+1
            peoplelst[count] = guess
            ignoreincorrect = 1
        if ignoreincorrect != 1:
            if str(realwrdlow) != str(guess):
                ckthing = ckthing+1
                if ckthing == len(wordlst):
                    turn = turn+1
                    print("incorrect! You have ", turn, " strikes!")
                    break
print("The correct word was ", listToString(wordlst), " Confused? Well then look in the share folder and at words.txt then you will see, Windows noob.")


