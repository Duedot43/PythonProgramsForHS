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
def setvalmagic(srvip, file, lst):
    os.system(f"curl 'http://" + srvip + "/" + file + "", lst)
    return 0
def getboard(a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, d1, d2, d3, d4, d5, d6, d7, d8, d9, d10, e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, f1, f2, f3, f4, f5, f6, f7, f8, f9, f10, g1, g2, g3, g4, g5, g6, g7, g8, g9, g10, h1, h2, h3, h4, h5, h6, h7, h8, h9, h10, i1, i2, i3, i4, i5, i6, i7, i8, i9, i10, j1, j2, j3, j4, j5, j6, j7, j8, j9, j10, ):
#  1  2  3  4  5  6  7  8  9  10
#A .  .  .  .  .  .  .  .  .  .
#B .  .  .  .  .  .  .  .  .  .
#C .  .  .  .  .  .  .  .  .  .
#D .  .  .  .  .  .  .  .  .  .
#E .  .  .  .  .  .  .  .  .  .
#F .  .  .  .  .  .  .  .  .  .
#G .  .  .  .  .  .  .  .  .  .
#H .  .  .  .  .  .  .  .  .  .
#I .  .  .  .  .  .  .  .  .  .
#J .  .  .  .  .  .  .  .  .  .

 
    #generate board
    test = "x"
    board = (f"  1  2  3  4  5  6  7  8  9  10\nA {a1}  {a2}  {a3}  {a4}  {a5}  {a6}  {a7}  {a8}  {a9}  {a10}\nB {b1}  {b2}  {b3}  {b4}  {b5}  {b6}  {b7}  {b8}  {b9}  {b10}\nC {c1}  {c2}  {c3}  {c4}  {c5}  {c6}  {c7}  {c8}  {c9}  {c10}\nD {d1}  {d2}  {d3}  {d4}  {d5}  {d6}  {d7}  {d8}  {d9}  {d10}\nE {e1}  {e2}  {e3}  {e4}  {e5}  {e6}  {e7}  {e8}  {e9}  {e10}\nF {f1}  {f2}  {f3}  {f4}  {f5}  {f6}  {f7}  {f8}  {f9}  {f10}\nG {g1}  {g2}  {g3}  {g4}  {g5}  {g6}  {g7}  {g8}  {g9}  {g10}\nH {h1}  {h2}  {h3}  {h4}  {h5}  {h6}  {h7}  {h8}  {h9}  {h10}\nI {i1}  {i2}  {i3}  {i4}  {i5}  {i6}  {i7}  {i8}  {i9}  {i10}\nJ {j1}  {j2}  {j3}  {j4}  {j5}  {j6}  {j7}  {j8}  {j9}  {j10}")
    return board
def convert(string):
    list1=[]
    list1[:0]=string
    return list1