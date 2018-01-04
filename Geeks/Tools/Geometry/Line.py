class Line(object):

    def __init__(self, data):
            self.first, self.second = data

    def slope(self):
            '''Get the slope of a line segment'''
            (x1, y1), (x2, y2) = self.first, self.second
            try:
                    return (float(y2)-y1)/(float(x2)-x1)
            except ZeroDivisionError:
                    # line is vertical
                    return None


data = ((1,1), (2,3))

line = Line(data)

m = line.slope()

print (m)
