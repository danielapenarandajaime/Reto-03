import math
class Point:    
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def compute_distance(self, point):
        return math.sqrt((self.x - point.x) ** 2 + (self.y - point.y) ** 2)
    def __str__(self):
        return f"({self.x}, {self.y})"
        

class Line:
    lenght: float
    slope: float

    def __init__(self, start: Point, end: Point): 
        self.start = start
        self.end = end

    def compute_length(self) -> float:
        self.lenght = self.start.compute_distance(self.end)
        return self.lenght
    
    def compute_slope(self) -> float:
        self.slope = (self.start.y - self.end.y) / (self.start.x - self.end.x)
        return self.slope

    def compute_horizontal_cross(self) -> bool:
        if self.start.y>0 and self.end.y<0:
            return True
        elif self.start.y<0 and self.end.y>0:
            return True
        else: return False
    
    def compute_vertical_cross(self) -> bool:
        if self.start.x>0 and self.end.x<0:
            return True
        elif self.start.x<0 and self.end.x>0:
            return True
        else: return False


    

class Rectangle:
    def __init__(self, line1: Line, line2: Line, line3: Line, line4: Line):
        self.line1 = line1
        self.line2 = line2
        self.line3 = line3
        self.line4 = line4

    def width(self):
        return self.line1.compute_length()
    
    def height(self):
        return self.line3.compute_length()

    def compute_area(self):
        return (self.width() * self.height())
    
    def compute_perimeter(self):
        return (2*self.width() +  2* self.height())

    def center(self):
        return Point((self.line1.start.x + self.line1.end.x)/2, (self.line1.start.y + self.line2.start.y)/2)

    def compute_interference_point(self, point: "Point"):
        center = self.center()
        width = self.width()
        height = self.height()
        x_derecha= center.x + (width/2)
        x_izquierda=center.x - (width/2)
        y_arriba=center.y + (height/2)
        y_abajo=center.x - (height/2)
        if point.x<x_derecha and point.x>x_izquierda and point.y<y_arriba and point.y>y_abajo:
                return "The point is inside the rectangle."
        else: return "The point is outside the rectangle."




line10 = Line(Point(10,6), Point(8, -1))
line21 = Line(Point(-9,-7), Point(8, 9))
line1 = Line(Point(10,-7), Point(18, -7))
line2 = Line(Point(10,9), Point(18, 9))
line3 = Line(Point(10,-7), Point(10, 9))
line4 = Line(Point(18,-7), Point(18, 9))
rectangle1 = Rectangle(line1, line2, line3, line4)

print(line10.compute_horizontal_cross())
print(line10.compute_vertical_cross())
print(line21.compute_horizontal_cross())
print(line21.compute_vertical_cross())
print(rectangle1.width(), rectangle1.height(), rectangle1.compute_area(), rectangle1.compute_perimeter(), rectangle1.center(), rectangle1.compute_interference_point(Point(10,6)))