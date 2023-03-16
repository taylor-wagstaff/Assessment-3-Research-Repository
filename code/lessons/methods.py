# lesson for filter method.  for Intermediate programming
# and Reduce, reduces it down to a single value. 

class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    #representation method. ??
    def __repr__(self): #https://docs.python.org/3/library/functions.html#repr
        return f"{self.name}: {self.score}"

students = [Student("Joe", 0.46), Student("Amy", 0.72), Student("Mark", 0.88), Student("Zach", 0.75), Student("Jane", 0.84), Student("Sarah", 0.63)]


#filtering down to ony include things in the list. 

# failing_students = []

# for student in students:
#     if student.score < 0.7:
#         failing_students.append(student)


# filter_list = list(filter(lambda student: student.score < 0.7, students))

# print("filter_list", filter_list)
# print(failing_students)




# Challenge
# Use filter to list all even numbers

# numbers = [1,2,3,4,5]

# filter_numbers = list(filter(lambda number: number % 2 == 0, numbers ))
# print("filter_numbers", filter_numbers)



# reduce method

score_total = 0

for student in students:
    score_total += student.score

# total average score, total divided by length of entries
print(score_total / len(students))

# import reduce function
from functools import reduce

reduce_total = reduce(lambda total, student: student.score + total, students, 0)

print("reduce total", reduce_total / len(students))

#challenge

numbers2 = [1,2,3,4,5]

# if we begin with a number no need to initialise value, if you did, start with 1.
number_total = reduce(lambda total, n: n * total, numbers2)

print(number_total)

##