import requests
import time
import os
def getvaluntil(srvip, file, valned):
    cl2con = "1"
    while cl2con == "0":
        time.sleep(1)
        res = requests.get("http://" + srvip + "/" + file)
        if res.status_code == 200:
            p2 = int(res.text)
            if p2 == valned:
                cl2con = "1"
                return valned
def getval(srvip, file):
    res = requests.get("http://" + srvip + "/" + file)
    if res.status_code == 200:
        p2 = str(res.text)
        return p2
def setval(srvip, file):
    os.system("curl 'http://" + srvip + "/" + file + "'")
    return 0
def getboard(a1, a2, a3, b1, b2, b3, c1, c2, c3):
#    A     B     C  
#       |     |     
#1      |     |     
#  _____|_____|_____
#       |     |     
#2      |     |     
#  _____|_____|_____
#       |     |     
#3      |     |     
#       |     |     
 
    #generate board
    test = "x"
    board = (f"    A     B     C  \n       |     |     \n1   {a1}  |  {b1}  |  {c1}  \n  _____|_____|_____\n       |     |     \n2   {a2}  |  {b2}  |  {c2}   \n  _____|_____|_____\n       |     |     \n3   {a3}  |  {b3}  |  {c3}  \n       |     |     ")
    return board