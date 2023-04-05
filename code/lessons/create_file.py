#writing files in python

# file = open("cheese.txt", "x")

# file.write("x marks the spot!")

# file.close()

#overwrite
# file = open("cheese.txt", "w")

# file.write("to overwrtie the file")

# file.close()

#Append
# file = open("cheese.txt", "a")

# file.write("to append the file, add to it")

# file.close()


# to read file. 

file = open("cheese.txt", "r")

# file_text = file.read()
# print(file_text)

# have to move back to the top of the file, 
#can read only once.
# beings them into a list for data manipulation.  
lines = file.readlines()
print(lines)

file.close()