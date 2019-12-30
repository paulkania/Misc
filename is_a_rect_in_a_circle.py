import math as m
from pprint import pprint



class Circle:
    def __init__(self,x,y,r):
            self.x=x
            self.y=y
            self.r=r
class Rectangle:
    def __init__(self,x,y,w,h):
        self.x=x
        self.y=y
        self.corners = [(x,y),(x+w,y),(x,y+h),(x+w,y+h)]

c1= Circle(50,10,30)
r1 = Rectangle(40,20,10,20)

def ispointinside(acircle, arectangle):
    cx = acircle.x
    cy = acircle.y
    rect_coords = arectangle.corners
    circmag = acircle.r
    corners=[]
    res=[]
    for corner in range(4): #or 4 if you want to be more simple...a rect will always have 4
        rx = rect_coords[corner][0]
        ry = rect_coords[corner][1]
        rectmag = m.sqrt((cx-rx)**2 + (cy-ry)**2)
        if rectmag <= circmag:
            corners.append(1)
        else:
            corners.append(0)
        res.append((rectmag,circmag))
    return corners,res


x= ispointinside(c1,r1)
print(x)
