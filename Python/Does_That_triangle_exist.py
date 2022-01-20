#The game show
height = float(input("What is the height of the triangle?\n"));
legnth = float(input("What is the legnth of the triangle?\n"));
slant = float(input("What is the slanted sides legnth?\n"));
valid = height+legnth
if  valid <= slant:
    print("Invalid!");
    exit();
if height == legnth:
    if height == slant:
        print("Tis' a equilateral triangle.");
if height != legnth:
    if legnth != slant:
            print("Tis' a scalene triangle.");
if height == legnth:
    if height != slant:
        print("Tis' a isosceles triangle.");
if slant == height:
    if height != legnth:
        print("Tis' a isosceles triangle.");
if slant == legnth:
    if height != legnth:
        print("Tis' a isosceles triangle.");