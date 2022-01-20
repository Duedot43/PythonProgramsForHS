import re
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
def Convert(string):
    list1=[]
    list1[:0]=string
    return list1
def encrypt(msg):
    #print(msg)
    di = "0"
    count = "0"
    first = msg[0]
    #enc = encode(first)
    #print (enc)
    encryptedmsg = []
    for x in msg:
        enc = encode(x)
        encryptedmsg.append(enc)

    return encryptedmsg


def encode(letter):
    if letter == "A":
        ret = "E"
        return ret
    if letter == "B":
        ret = "D"
        return ret
    if letter == "C":
        ret = "P"
        return ret
    if letter == "D":
        ret = "W"
        return ret
    if letter == "E":
        ret = "T"
        return ret
    if letter == "F":
        ret = "L"
        return ret
    if letter == "G":
        ret = "R"
        return ret
    if letter == "H":
        ret = "B"
        return ret
    if letter == "I":
        ret = "U"
        return ret
    if letter == "J":
        ret = "N"
        return ret
    if letter == "K":
        ret = "S"
        return ret
    if letter == "L":
        ret = "O"
        return ret
    if letter == "M":
        ret = "F"
        return ret
    if letter == "N":
        ret = "Z"
        return ret
    if letter == "O":
        ret = "G"
        return ret
    if letter == "P":
        ret = "J"
        return ret
    if letter == "Q":
        ret = "K"
        return ret
    if letter == "R":
        ret = "Q"
        return ret
    if letter == "S":
        ret = "V"
        return ret
    if letter == "T":
        ret = "M"
        return ret
    if letter == "U":
        ret = "A"
        return ret
    if letter == "V":
        ret = "X"
        return ret
    if letter == "W":
        ret = "Y"
        return ret
    if letter == "Y":
        ret = "I"
        return ret
    if letter == "X":
        ret = "C"
        return ret
    if letter == "Z":
        ret = "H"
        return ret
    if letter == "a":
        ret = "e"
        return ret
    if letter == "b":
        ret = "d"
        return ret
    if letter == "c":
        ret = "p"
        return ret
    if letter == "d":
        ret = "w"
        return ret
    if letter == "e":
        ret = "t"
        return ret
    if letter == "f":
        ret = "l"
        return ret
    if letter == "g":
        ret = "r"
        return ret
    if letter == "h":
        ret = "b"
        return ret
    if letter == "i":
        ret = "u"
        return ret
    if letter == "j":
        ret = "n"
        return ret
    if letter == "k":
        ret = "s"
        return ret
    if letter == "l":
        ret = "o"
        return ret
    if letter == "m":
        ret = "f"
        return ret
    if letter == "n":
        ret = "z"
        return ret
    if letter == "o":
        ret = "g"
        return ret
    if letter == "p":
        ret = "j"
        return ret
    if letter == "q":
        ret = "k"
        return ret
    if letter == "r":
        ret = "q"
        return ret
    if letter == "s":
        ret = "v"
        return ret
    if letter == "t":
        ret = "m"
        return ret
    if letter == "u":
        ret = "a"
        return ret
    if letter == "v":
        ret = "x"
        return ret
    if letter == "w":
        ret = "y"
        return ret
    if letter == "y":
        ret = "i"
        return ret
    if letter == "x":
        ret = "c"
        return ret
    if letter == "z":
        ret = "h"
        return ret
    if letter == " ":
        ret = "_"
        return ret
    return letter
def decrypt(msg):
    #print(msg)
    di = "0"
    count = "0"
    first = msg[0]
    #enc = encode(first)
    #print (enc)
    decryptedmsg = []
    for x in msg:
        dec = decode(x)
        decryptedmsg.append(dec)
    return decryptedmsg

def decode(letter):
    if letter == "E":
        ret = "A"
        return ret
    if letter == "D":
        ret = "B"
        return ret
    if letter == "P":
        ret = "C"
        return ret
    if letter == "W":
        ret = "D"
        return ret
    if letter == "T":
        ret = "E"
        return ret
    if letter == "L":
        ret = "F"
        return ret
    if letter == "R":
        ret = "G"
        return ret
    if letter == "B":
        ret = "H"
        return ret
    if letter == "U":
        ret = "I"
        return ret
    if letter == "N":
        ret = "J"
        return ret
    if letter == "S":
        ret = "K"
        return ret
    if letter == "O":
        ret = "L"
        return ret
    if letter == "F":
        ret = "M"
        return ret
    if letter == "Z":
        ret = "N"
        return ret
    if letter == "G":
        ret = "O"
        return ret
    if letter == "J":
        ret = "P"
        return ret
    if letter == "K":
        ret = "Q"
        return ret
    if letter == "Q":
        ret = "R"
        return ret
    if letter == "V":
        ret = "S"
        return ret
    if letter == "M":
        ret = "T"
        return ret
    if letter == "A":
        ret = "U"
        return ret
    if letter == "X":
        ret = "V"
        return ret
    if letter == "Y":
        ret = "W"
        return ret
    if letter == "C":
        ret = "X"
        return ret
    if letter == "I":
        ret = "Y"
        return ret
    if letter == "H":
        ret = "Z"
        return ret
    if letter == "e":
        ret = "a"
        return ret
    if letter == "d":
        ret = "b"
        return ret
    if letter == "p":
        ret = "c"
        return ret
    if letter == "w":
        ret = "d"
        return ret
    if letter == "t":
        ret = "e"
        return ret
    if letter == "l":
        ret = "f"
        return ret
    if letter == "r":
        ret = "g"
        return ret
    if letter == "b":
        ret = "h"
        return ret
    if letter == "u":
        ret = "i"
        return ret
    if letter == "n":
        ret = "j"
        return ret
    if letter == "s":
        ret = "k"
        return ret
    if letter == "o":
        ret = "l"
        return ret
    if letter == "f":
        ret = "m"
        return ret
    if letter == "z":
        ret = "n"
        return ret
    if letter == "g":
        ret = "o"
        return ret
    if letter == "j":
        ret = "p"
        return ret
    if letter == "k":
        ret = "q"
        return ret
    if letter == "q":
        ret = "r"
        return ret
    if letter == "v":
        ret = "s"
        return ret
    if letter == "m":
        ret = "t"
        return ret
    if letter == "a":
        ret = "u"
        return ret
    if letter == "x":
        ret = "v"
        return ret
    if letter == "y":
        ret = "w"
        return ret
    if letter == "c":
        ret = "x"
        return ret
    if letter == "i":
        ret = "y"
        return ret
    if letter == "h":
        ret = "z"
        return ret
    if letter == "_":
        ret = " "
        return ret
def stringlist(s):
    listToStr = ''.join(map(str, s))
    return listToStr
def find(string):
    new_text = re.sub(r"[^a-zA-Z0-9 ]", "", string)
    return new_text
   