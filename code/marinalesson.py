# print("what is your name?  ")
# name = input("enter your name? ")
# print(f"your name is {name}")

# num1 = [2, 5, 7, 8]
# num2 = 5

# print(num1[2] + num1[1])
# print(num2 - num2)
# print(num2 * num2)
# print(num2 / num2)

# a = 10
# a += 7.5
# print(a)

# print(num1.reverse())
# print(num1.reverse())


# x = input("enter number: ")


# xint = int(x)
# xx = int(x + x)
# xxx = int(x + x + x)


# result = xint + xx + xxx
# print(result)
# ###

# n = input("enter any digit: ")

# nn = (n + n)
# nnn = (n + n + n)
# result2 = int(n) + int(nn) + int(nnn)

# print(result2)

# ##

# current_year = 2023

#ask user to input their year of birth
# user_birth_year_input = input("What year were you born? ")

#convert the raw user input to an int using the int() function and store in new variable
# user_birth_year = int(user_birth_year_input)

#subtract the converted user input from the current year
# user_age = current_year - user_birth_year

# print(user_age)




### March 10th Marina Lesson

import time
import random
# a = 1 
# b = "hello"

# to reorder varibles, you can list varibles are reorder them 
# a, b = b, a

# print(a, b)
# c = b + " " + str(a)
# print(c)

#Cycles, some are limited or infinite. 

# counter = 5 


# while counter >= 0:
#     #causes delay in teminal. 
#     time.sleep(1)
#     counter -= 1;
#     print(counter) #counter = counter -1

# sec = 0 
# while True:
#     time.sleep(1)
#     sec += 1 
#     print(sec)

# start from one to five, can have three arguments, 
# for i in range(1, 5):
#     time.sleep(1)
#     print(i)


fruits = []
fruits = ["Apple", "Pineapple", "Banana", "Lemon"]
print(fruits)
print(fruits[1])

#add items, 
fruits.append("Orange")
fruits.append("Pear")
fruits.append("Apricot")
print(fruits)


#delete the element
fruits.pop(1)
print(fruits)

# select all elements one by one
for fr in fruits:
    print(fr)



# generate random numbers 

numbers = []

for i in range(100):
    answer = random.randint(0, 1000)
    numbers.append(answer)
  

# print(numbers)

#for loop of n in numbers greater than 500
# for n in numbers:
#     if n > 500:
        # print(n)

# max_number = 0

# for n in numbers:
#     #for every index is greater than 0
#     if n > max_number:
#         #it now equals n 
#         max_number = n

# print("max number = ", max_number)

# min_number = 1000
# for n in numbers:
#     if n < min_number:
#         min_number = n

    
# print("min number = ", min_number)



# x = max(numbers)
# print("x", x)


# y = min(numbers)
# print("y", y)


username = input("What is your username?  ")
password = input("What is your password?  ")


# if (username == "Taylor" and password == "000") or (username == "Ruby" and password == "111"):
#         print("login successful")
# elif username == "Fiona" and password == "111":
#         print("login successful")
# else:
#         print("incorrect")

users = ["Taylor", "Ruby"]
passwords = ["0000", "1111"]
GREEN = "\033[32m"
RED = "\033[31m"
for i in range(0, len(users)):
   if(username == users[i] and password == passwords[i]):
       print(GREEN + "login sucessful")
       #exit loops
       exit()

print(RED +"wrong login")

# python is programming language, loosely couped. 
# highyl coupled language when you specific the type.
# class is a blueprint of something
#  