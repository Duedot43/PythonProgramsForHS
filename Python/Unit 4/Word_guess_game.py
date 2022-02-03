import random
def convert(string):
    list1=[]
    list1[:0]=string
    return list1
with open("share/words.txt", "r") as file:
    allText = file.read()
    words = list(map(str, allText.split()))
  
    # print random string
word = random.choice(words)
turn = 0
while turn != 10:
    wordlst = convert(word)
    

