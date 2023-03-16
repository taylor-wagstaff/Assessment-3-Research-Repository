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

# call the method
cat1.display()
cat1.sound()


# Wildcat inherits Super class Cat
cat2 = WildCat("Luna", 2, False)

cat2.display()
cat2.sound()
cat2.hunt()

#polymorphism, somehting can have more than one form, 