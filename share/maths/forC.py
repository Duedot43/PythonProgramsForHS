import math
import os
print("Put the specified number into the equation displayed")
A = float(input("A^2+B^2=C^2\n^^^\n?"));
B = float(input("A^2+B^2=C^2\n    ^^^\n?"));
C = (A*A)+(B*B)
print("Sum ", C);
D = math.sqrt(C);
print("Root ", D);
input()
os.system("python Python/Maths_Calculator.py")
