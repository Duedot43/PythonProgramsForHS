first = int(input("What is the first number in your grade (->5/10)\n"));
last = int(input("What is the last number in your grade (5/10<-)\n"))
precent = first+last

if precent >.92:
    print ("A")
elif precent >.89:
    print ("A-")
elif precent >.86:
    print ("B+")
elif precent >.82:
    print ("B")
elif precent >.79:
    print ("B-")
elif precent >.76:
    print ("C+")
elif precent >.72:
    print ("C")
elif precent >.69:
    print ("C-")
elif precent >.66:
    print ("D+")
elif precent >.62:
    print ("D")
elif precent >.59:
    print ("D-")
elif precent <.58:
    print ("F")
import os
input()
os.system("python Python/Maths_Calculator.py")