from turtle import *

# t = new Turtle()

# #instantiate
# t.forward(100)



bgcolor("lightblue")


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

# draw_sprial()

def draw_cylinder():
 
    x = 100
    y = 90
    for i in range(100):
      speed(0)
      shape("circle")
      forward(x - i)
      left(y)
      circle(120)
      forward(x - i)
      circle(120)
    

draw_cylinder()


exitonclick()
