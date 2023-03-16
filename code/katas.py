# Katas on CodeWars.com

#Write function RemoveExclamationMarks which removes 
#all exclamation marks from a given string.

# def remove_exclamation_marks(s):
#         remove = list(filter(lambda x : x != "!", s))
#         joined = ''.join(remove)
#         return joined



# Grade book
# Complete the function so that it finds the average of the three scores passed to it and returns the letter value associated with that grade.

# Numerical Score	Letter Grade
# 90 <= score <= 100	'A'
# 80 <= score < 90	'B'
# 70 <= score < 80	'C'
# 60 <= score < 70	'D'
# 0 <= score < 60	'F'
# Tested values are all between 0 and 100. Theres is no need to check for negative values or values greater than 100.


# def get_grade(s1, s2, s3):
    # score = (s1 + s2 + s3) / 3
    
    # if score < 60 and score >= 0:
    #     return "F"
    # elif score < 70 and score >= 60:
    #     return "D"
    # elif score < 80 and score >= 70:
    #     return "C"
    # elif score < 90 and score >= 80:
    #     return "B"
    # elif score < 100 and score >= 90:
    #     return "A"
    # else:
    #     return "A"

#Sentence Smash
# Write a function that takes an array of words and smashes them together
# into a sentence and returns the sentence. You can ignore any need to 
# sanitize words or add punctuation, but you should add spaces between 
# each word. Be careful, there shouldn't be a space at the beginning or
# the end of the sentence!
words = ["hello", "world"]

def smash(words):
    return " ".join(words)

