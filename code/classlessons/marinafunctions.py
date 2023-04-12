import math


#GOD module, huge files...
#function
def cir(r):
    return 2 * math.pi * r


def area_of_circel(r):
    return math.pi * r * r;

def volume(r):
    return 4 / 3 * math.pi * r * r * r


r1 = 2
s1 = cir(r1)
print(s1)


### dictionary, key value pairs 

course = {
    
    "name": "software development",
    "duration": "8 weeks"
}



# add key 
course["fee"] = 1000.00
course["name"] = "Course 1"
# to update
course.update({"name": "course 2"})
# to remove element
course.pop("fee")


print(course)

for x in course:
    print(x, course[x])

# for key, values in course.items():
#   print(key, values)

### object oriented 

#class = templates
# instanses of the class, object