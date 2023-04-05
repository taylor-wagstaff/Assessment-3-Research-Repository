import sys

#lesson in Intermediate Python for Non-Programmers

# when i write in the terminal all of them are printed out. 
# al show up as individual arguments 

# for argument in sys.argv:
#     print(argument)

# to manipulate arguments.
# 
total = 1 
# removes.
del(sys.argv[0])
for argument in sys.argv:
    try:
        number = int(argument)
        #total = total * number
        total *= number
    except Exception as e:
        print(e)
        print("Only numbers can be provided")
        sys.exit(1)
    

print(total)