from os import pardir
from pycat.core import Window, Point
from math import sqrt

w = Window()

A = Point(400,200)
B = Point(800,200)

a = A.x
b = B.x
c = (a-b)/2
d = B.x - A.x

C = Point ( (a+b)/2 , sqrt(d**2 - c**2)+A.y  )

ab = w.create_line(A.x, A.y, B.x, B.y)
bc = w.create_line(B.x, B.y, C.x, C.y)
ca = w.create_line(C.x, C.y, A.x, A.y)


w.run()