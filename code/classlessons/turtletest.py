from turtle import *

# t = new Turtle()

# #instantiate
# t.forward(100)


#classic sprial
# def draw_sprial():
#     x = 200
#     y = 90
#     for i in range(200):
#       forward(x - i)
#       left(y)
    
#circle spiral
# def draw_sprial():
 
#     x = 200
#     y = 90
#     for i in range(200):
#       forward(x - i)
#       left(y + i)
#       circle(120)

# def draw_sprial():
 
#     x = 200
#     y = 90
#     for i in range(200):
#       forward(x - i)
#       left(y)
#       circle(120)
#       speed(0)

#  def draw_cylinder(y:int = 200, x: int = 200):
 
#       for i in range(100):
#         speed(0)
#         shape("circle")
#         forward(x - i)
#         left(y)
#         circle(120)
#         forward(x - i)
#         circle(120)

# draw_sprial()

#creating class and objects for turtle 
bgcolor("lightblue")

class Shape:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
          
    def draw_cylinder(self):
      for i in range(100):
        speed(0)
        shape("circle")
        forward(self.x - i)
        left(self.y)
        circle(120)
        forward(self.y - i)
        circle(120)

    def draw_shape(self):
        for i in range(100):
            forward(self.x + i)
            left(self.y)

    def draw_sprial(self):
      for i in range(200):
        forward(self.x - i)
        left(self.y)
        circle(120)
        speed(0)
       
# name is given to object
draw = Shape(200, 100)

draw.draw_cylinder()
# draw.draw_sprial()
# draw.draw_shape()
# draw.draw_random()




#Chatgpt using the composing class method. 

# class Point:
#     def __init__(self, x: int, y: int):
#         self.x = x
#         self.y = y

# class Line:
#     def __init__(self, start_point: Point, end_point: Point):
#         self.start_point = start_point
#         self.end_point = end_point
    
#     def draw(self):
#         speed("slow")
#         penup()
#         goto(self.start_point.x, self.start_point.y)
#         pendown()
#         goto(self.end_point.x, self.end_point.y)

#contructing or instantiating the object. 

# start_point = Point(0, 0)
# end_point = Point(100, 100)
# my_line = Line(start_point, end_point)
# my_line.draw()





# exitonclick()

# Lesson functional programming, 
# Functions are cleaner, reuseable, easy to test. 

#if import functioning. 
# if __name__ == "__main__":
#       
   