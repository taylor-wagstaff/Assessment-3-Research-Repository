# Learning Python through LinkedIn Learning.
# Back to basics

# Python for Non-Programmers
# Python from zero by Nick Walter

# Notes:
# can run it almost anywhere, mac, windows etc.

# Print Hello World

print("Hello World")

# Varibles
# Piece of info that could change. 

wallet = 41
print(wallet)

wallet = 32
#can change varibles, change over times

#types are different types of things to place invarible

#int short for interger, no decimal places,can be positive or negative
#Floats have decimal places
# What about infinite numbers?

day = 3 
print(day + 6)

# * is times, + for plus, / for division, basicallly the same as javascript

age = 32
bitcoin = 0.00034

# strings represent text, does python have Regex expressions?


store ='Nick\'s Pizza Shop, the best there is '
print(store)

# you can put backslash to have a comma inside a string 

#place a lowercase f to show varibales, called f string The letter 'f' also indicates that these strings are used for formatting
day = 25 
print(f"Today is the {day}th")

#Python likes underscore for vairble names

# Boolen type is captial True and False, not in string etc. 

light_is_on = True

if light_is_on:
    print("ON!")
else:
    print("Off!")
# if statments have colon followed by indentation. Without curly brace
# Tab or spaces, very important, if things are not tabbed over they wonts run after an if statement
# since else is after if it forwards the vairible name?

# if weight != 196:
#  print("your under weight")
# or if weight < 196: etc...
# if age >= 18:
#  print("Adult")
# else:
# print("child")


# fortune cookie project
# Random Numbers, import module, have to bring that module in

import random

#to import method, type module name followed by .
#module are kinda like inbuilt method like in javascript
#include brackets and range
print(random.randint(1, 10))

answer = random.randint(1, 3)

if answer == 1:
    print("yes")
if answer == 2:
    print("no")
if answer == 3:
    print("maybe")

# Lists, Loops and Dictionaries. 
# new type in Python, ordered lists in Python

fav_movies = [1, 2, 3.6, 4, True, "hello"]
print(fav_movies[0])
#lists can have multiple types.
# zero based counting. 

#for length of lists:
print(len(fav_movies))

#to add items to list: append method. 
fav_movies.append("Iron Man")
#To insert at postion of list: first parameter is index, followed by insertion
fav_movies.insert(1, "batman")

#to delete things, 
del(fav_movies[2])
print(fav_movies)

# For loop in Python, for followed by index(number) followed by in, then range

for number in range(10):
    print("hello")

#number could be called anyhting. 

for movies in fav_movies:
    print(movies)

#Python dictionaries, similar to list, key value pair. 
# curly backets for dictionairy, key in quotes. 

cats = {"jane": 6, "Tom": 14 }
#to locate vakue of key
print(cats["Tom"])
#to change a value
cats["Tom"] = 2
# to delete
del(cats["Tom"])
#length of dictionary
len(cats)


#Working with Strings. 


string = """
Lorem ipsum dolor sit amet, 
consectetur adipiscing elit, 
sed do eiusmod tempor incididunt 
ut labore et dolore magna aliqua. 
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
"""
# length of letters
print(len(string))
#length of words
print(len(string.split()))

# look at every letter
text = "a b c a a b"
print(text.lower().split())
#method for lowercase and spilt the string. 


#inital value, empty object
word_count = {}


for word in text.split():
    #if in varible
    if word in word_count:
        word_count[word] += 1
    else:
      word_count[word] = 1

print(word_count)

# defining a function

def bark():
    print("woof woof!")

# declare function
bark()

def hello(name):
    print(f"Hello {name}!")

hello("John")

# returning information.

def double(number):
    return number * 2

new_number = double(5)

print(new_number)
#### 
def caps(string):
    return string.upper()

upper = caps("fherjwqnfrenq")

print(upper)

#input 

# user_text = input("enter some text: ")
# print(user_text)

# Number guessing game

guess = int(input("What is your guess: "))
correct_number = 5
guess_count = 1
#while, basically combination of if statment and for loop, loop until true

while guess != correct_number:
  guess_count += 1
  guess = int(input("What is your guess: "))

print(f"You got the right answer {correct_number}. it took you {guess_count} times")

#import time
#time.sleep(3) seconds

