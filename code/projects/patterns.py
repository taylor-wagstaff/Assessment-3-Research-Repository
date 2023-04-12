# Python: Design Patterns
# By Jungwoo Ryoo

#Linkedin Learning. 

# Design patterns are well known solutions to regualr problems
# no need to reinvent the wheel
# Systematic reuse of best diesng ideas
#lower cost and high quailty. 

#book: Gang of four, Design Patterns:elements of Reusable Object-Oriented Software

# Characterisitcs, Language Neutral, Dynamic, intentionality incomplete, 
#professional must master design Patterns

# Three different types: Creational, Structural, Behavioral

# Creational. build object systematically
# Flexibility, polymorphism often in use

# Structural. Reltationshoips between software parts. 
#accomplish both functional and nonfunctional goals
# Inheritance a lot


# Behavioral. Object interactions, 
# common goals together.
#interfaces. 

# OOP
# require the use of OOP
# Objects represent all the moving pieces in your solution. 
# eg, Participant - problem Domain
# Regisation - solution domain

# Classes are templates, Cookie cutters to replicate objects
# Attributes, represent properites of an enity
# captures the state of the enity

# Methods represent behavoirs. 

# Inheritance, Parent and child relationships. 
# child class, Keeps the attributes and methods of its parent
# Add new Attibutes or methods of its own
# Overrides the existing methods of its parent

# Class Pet, child: Dog & Cat

# Polymorhism, relies on inheritance
# Allows child classes to be instantiated and treated
# as the same type as thier parent
# enables a parent class to be a placeholder

# Pattern Context:
# Participants, Quality attributes, Forces, Consequences.





# Factory: Is object creations, 
# Needed in uncertainties in types of objects
# Decisions at runtimes. 
# Pet Shop, not sells cats

class Dog:
    
    def __init__(self, name):
      self.name = name

    def speak(self):
       return "Woof!"
    
def get_pet(pet="dog"):
       
    """The factory method"""
    pets = dict(dog=Dog("Hope"))
    return pets[pet]
       


class Cat:
    
    def __init__(self, name):
      self.name = name

    def speak(self):
       return "Meow!"
    
def get_pet(pet="cat"):
       
  """The factory method"""
  pets = dict(dog=Dog("Hope"), cat=Cat("Peace"))
  return pets[pet]
       
       
d = get_pet("dog")
print(d.speak())

c = get_pet("cat")
print(c.speak())