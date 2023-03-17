### object oriented 

#Inheritance
#polymorphism
#encapsulation





class Cat():
    name: None;
    age: None;
    isHappy: None;
    

    #a class constructor, intialise all our attributes
    def __init__(self, name, age, isHappy):
        self.name = name
        self.age = age
        self.isHappy = isHappy

    #methods, self is a varible which allows access to attributes
    def display(self):
        print("****** cat ******")
        print("name", self.name)
        print("age", self.age)
        print("ishappy", self.isHappy)

    def sound(self):
        print("Meow!")

    # def hunt(self):
    #     print("I am hunting")
        


class DomesticCat(Cat):
    owner: None;


    def display(self):
        print("***** domestic *****")
        super().display()
        print("owner", self.owner)

    def __init__(self, owner, name, age, isHappy):
        super().__init__(name, age, isHappy)
        self.owner = owner

    

class WildCat(Cat):
    
    def hunt(self):
        print("I am Hunting....")

    def sound(self):
        print("Meoowww...")



cat1 = DomesticCat("Jane", "Peter", 5, True)
#creating an instance, an object of this class
#<__main__.Cat object at 0x109c87a60>
# cat1.name = "Peter"
# cat1.age = 5
# cat1.isHappy = True


########################################
## main process, 

# from Cat import *

# if __name__ == "__main__"
# call the method
cat1.display()
cat1.sound()


# Wildcat inherits Super class Cat
cat2 = WildCat("Luna", 2, False)

cat2.display()
cat2.sound()
cat2.hunt()

#polymorphism, somehting can have more than one form, 

########################################
##OOPS concept, 

# Encapualtion, Inheritance, Polymorphism, Abstraction, 

# Encapualtion: to protect, something, class is the best example, 
# if you need to access something, use the object. 

# access specifier, public, public and protected. decide flexibilty to your user. 
# private: authroized only, 
# Protected: everywhere can see, only authrozied can use, like read/write only. 

# Inheritance: A:  base, parent, super class, B: derive, child, sub class. three differnt termologies, 
# Single level or simple inheritance. 
# if more inheritance, multi-level if more sub classes. 
# if two base classes, multiple inheritance. 

# hierarchical, two sub classes inherit from one base class. 
# Hybird, combing two subclass together in a single figure. 
# Python is the only language that supports all types of inheritance, 

# Abstraction

# If something is not required, hide, hide complexity from the user

# Polymorphism 

# Proceedural(functional programming) orientated, 
# Object Orientated Programming, method instead of funciton. 
########################################

########################################
### Marina Lesson, 17th of March, Software Development life cycle. 

# planning: which problem are we going to solve, time, price etc, 
# Analysis: Decision is made, mid-level manager, collect requirments, talk to stakeholders. Must be formalised. 
# Design: Which software and hardware architecture, Data model, Wireframes
# Implementation: Already have your structure designed, coding, actually making. 
# Testing & intergration: are your requirements all implementated
# Maintenance: decide, how are you going to improve it. 
########################################
