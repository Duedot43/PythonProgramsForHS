from math import sqrt
print ("Right triangle calculator")
base = input("Please input the base length: ")
hight = input("Please input the height: ")
base = int(base)
hight = int(hight)

#Canoolicate

area = 1/2*base*hight
print ("Area is ", area)
cea = (base ** 2)+(hight ** 2)
cea = sqrt(cea)
perm = base+hight+cea
print ("The Permiter is ", perm)
