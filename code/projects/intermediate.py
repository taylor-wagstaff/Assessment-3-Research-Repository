# Intermediate Python for Non-Programmers
# What you should know, by Nick Walter.

#classes in Python. 
# Wanted to understand classes more indepth. Has helped with software projects. 

#to make a class,cannot be empty, pass for empty line
#class attributes, or vairbles, accessed anyhting you want inside the class
#Start with uppercase letter
# class Dog:
#     pass

import random

#we want this dog class to inherit the class animal
class Animal:
     info = "a Living organism"

     def __init__(self, name):
      print("A animal is created")
      #any class is goin to have access to a name
      self.name = name
      self.fur = ""
     

class Dog(Animal):
    # info = "A four legged animal"
    #initialiastion function, runs every time create an object fom the class
    def __init__(self, name):
          #whenever dog is created we run init to animal superclass
          super().__init__(name)
          print("A dog is created")
          #instance varibles, self represents an instance or object of that class
          self.lucky_number = random.randint(1, 10)
          #instance vairble called name
         

    def bark(self):
         #this is a method?
         print(f"woof! my {self.name} is andy and number is {self.lucky_number}")


class Bulldog(Dog):
    pass


    def __init__(self, name):
        super().__init__(name)
        print("bulldog is created")

dog1 = Bulldog("bulldog")



#### Methods
# A method is a function inside of a class
# Method are special when we access or modifiy 
# instance varibles inside of a class
# different outputs / instances. 

#how to access class info, Dot into the class
# print(Dog.info, Dog.x)
# Dog()

#have to declare dog because name is required. 
dog1 = Dog("Fido")

print(dog1.info)



# dog2 = Dog("Sarah")

# dog1.bark()
# dog2.bark()

#accesses self instance. 
# print(dog1.name)
# print(dog2.name)


#init short for initialisation

##
#Super Class.
class Shape:
    side = 1

#square inherits shape
class Square(Shape):
    sides = 4
    #instance
    def __init__(self):
         # default value of zero, can be overwritten
         self.height = 0
    def area(self):
         return self.height * self.height

my_shape = Square()
my_shape.height = 10
print(my_shape.area())



## Instances, When ever to create something from a class
## its called an instance or an object. 

## created an individual objects from my dog class


# instances are object from a class, Inheritance draw from one another. 


#try and accept. 

# print("Before")
# name = "taylor"

# # try and except you can different errors named
# #you can keep moving in the code. 
# try: 
#     #cant divide by 0
#     # 4 / 0
#     print(name)
# except NameError as e:
#     print("this was a name issue")
#     #cant print the actual error as e(short for error)
#     print(e)
# except:
#     print("oops!")
    
# class Errors(Exception):
#     pass


# def upper(word):
#     #condition
#     if len(word) <= 0:
#         #key word raise exception. 
#         raise Errors("The word has to have at least one letter!")
#     return word.upper()

# print(upper(""))



# print("after")


# next section weather Api. See weather.py

# Section: Advanced comparisons and IF statements, control flow. 

age = 90 
height = 170

# and key word, a way to chain together conditionals, all have to be true, can be more than one and
if age >= 8 and height >= 135:
    print("you can ride the ride!")


#or 
if age >= 17 or height >= 160:
    print("you can ride the superide!")

# else if // elif

if height < 120:
    print("you cant ride any rides")
elif height < 135:
    print("you can ride the level-1 rides")
elif height < 200:
    print("you can ride any ride")
else:
    print("too tall to ride the rides :(")

if age % 2 == 0 and age > 100 or age == 0:
    print("you have interesting age")


#switch statements, only availible in  3.10

# direction = input("Which direction? ").lower()


# called match, 

# match direction:
#     case "north":
#         print("Up")
#     case "south":
#         print("Down")
#     case "east":
#         print("Right")
#     case "west":
#         print("Left")
#     #needs an underscore for not valid matches
#     case _:
#       print("not valid")

# functional programming 

class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

students = [Student("Joe", 0.46), Student("Amy", 0.72), Student("Mark", 0.88), Student("Zach", 0.75), Student("Jane", 0.84), Student("Sarah", 0.63)]

# who passed this test and who didnt.

student_results  = []

for student in students:
    # if student.score >= 0.70:
    #     student_results.append(f"{student.name} Passed")
    # else:
    #     student_results.append(f"{student.name} Failed")

    student_results.append(f"{student.name} Passed") if student.score >= 0.70 else student_results.append(f"{student.name} Failed")

# first paramters is what do you want to do with the data
# second is the list you want to do these operations to?
#takes a list the uses a Lambdas function to list names. 
# must be wrapped in a list otherwise displays object. 


map_results = list(map(lambda student: f"{student.name} Passed" if student.score >= 0.70 else f"{student.name} Failed", students))
print(map_results)

#A lambda expression is a way of creating a little function inline, 
# without all the syntax of a def
#The map() function runs a lambda function over the list [1, 2, 3, 4, 5], 
# building a list-like collection of the results, like this:
# >>> list(map(lambda n: n * 2, [1, 2, 3, 4, 5]))


# print(student_results)



# Challenge
# Use map to mulltiply all these numbers by 2

numbers = [1,2,3,4,5]

numbers_result = list(map(lambda n: n * 2, numbers ))
print(numbers_result)