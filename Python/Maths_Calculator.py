import os
print("\033[1;32;40m --------------Maths Calculator--------------  \n")
choice = input("\033[1;37;40m(1) Calculate for C^2\n(2) Calculate for either A^2 or B^2\n(3) Calculate a letter grade\n(4) Just a calculator\n(5) Calculate a triangle in a 3D space\n(6) Celsius to Fahrenheit\n");
if choice == "1":
    os.system("python share/maths/forC.py")
if choice == "2":
    os.system("python share/maths/forAB.py")
if choice == "3":
    os.system("python share/maths/grade.py")
if choice == "4":
    os.system("python share/maths/calc.py")
if choice == "5":
    os.system("python share/maths/3Dtry.py")
if choice == "6":
    os.system("python share/maths/c2f.py")