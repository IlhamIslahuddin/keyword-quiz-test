#keyword question maker

import random
file = open("definitions.txt", "r")
#destination must be changed
search = file.read()
num_of_lines = 1
for characters in search:
    if characters == "\n":
        num_of_lines = num_of_lines + 1
line_number = random.randint(1,num_of_lines)

dfile = open("definitions.txt")
#destination must be changed
definitions = (dfile.readlines())
print (line_number)
random_definition = definitions[line_number-1]
print (random_definition)

kfile = open("keywords.txt")
#destination must be changed
keywords = (kfile.readlines())
print (line_number)
correct_keyword = keywords[line_number-1]
print (correct_keyword)

user_guess = input("what is the correct keyword for the following definition?..."+" "+random_definition+"\n")
print (user_guess)
