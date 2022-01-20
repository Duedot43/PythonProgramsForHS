from cmath import sqrt
import math
import os
print("Put the specified number into the equation displayed")
A = float(input("A^2+B^2=C^2\n^^^\n?"));
C = float(input("A^2+B^2=C^2\n        ^^^\n?"));
A = A*A
C = C*C
B = C-A
print("B raw", B)
B = sqrt(B);
print("B Solved ", B);
import os
input()
os.system("python Python/Maths_Calculator.py")