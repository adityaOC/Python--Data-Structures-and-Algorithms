
from Geeks.Tools.Geometry.Line import Line
from Geeks.Tools.Geometry.Point import Point

def findIntersection(A,B,C,D):


    #line 1
    a1 = B.y - A.y
    b1 =  A.x - B.x
    c1 = a1 * A.x +  b1 * A.y

    # line 2
    a2 = D.y - C.y
    b2 = C.x - D.x
    c2 = a2 * C.x + b2 * C.y

    determinant = a1*b2 - a2*b1

    if determinant == 0:
        return  None

    else:

        x = (b2 * c1 - b1 * c2) / determinant

        y = (a1 * c2 - a2 * c1) / determinant;

        p = Point(x,y)

        return p


x1 = Point(1,1)
y1 = Point(4,4)
x2 = Point(1,8)
y2 = Point(2,4)

intersectionPOint = findIntersection(x1,y1,x2,y2)
print("Intersection Point is : {},{}".format(intersectionPOint.x,intersectionPOint.y))


