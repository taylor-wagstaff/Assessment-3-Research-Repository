### object oriented 

#class = templates
# instanses of the class, object

#cladd declaration
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




#creating an instance, an object of this class
#<__main__.Cat object at 0x109c87a60>
cat1 = Cat("Peter", 5, True )
# cat1.name = "Peter"
# cat1.age = 5
# cat1.isHappy = True

# call the method
cat1.display()
cat1.sound()



cat2 = Cat("Luna", 2, False)

cat2.display()
cat2.sound()