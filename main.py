import math
print( "введите длины сторон трапеции: ")
a = float(input("a = "))
b = float(input("b = "))
print( "длины боковых сторон трапеции: ")
c = float(input("c = "))
d = float(input("d = "))
p = (a + b + c + d) / 2
print("полупериметр трапеции = " , b)
s = (a + b) / abs(a - b) * math.sqrt((p - a) * (p - b) * (p - a - c) * (p - a - d))
print( "площадь трапеции = ", s)