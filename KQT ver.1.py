#keyword question maker

import random
file = open("D:\coding\VSCODE\definitions.txt", "r")
search = file.read()
num_of_lines = 1
for characters in search:
    if characters == "\n":
        num_of_lines = num_of_lines + 1
line_number = random.randint(1,num_of_lines)

dfile = open("D:\coding\VSCODE\definitions.txt")
definitions = (dfile.readlines())
print (line_number)
random_definition = definitions[line_number-1]
print (random_definition)

kfile = open("D:\coding\VSCODE\keywords.txt")
keywords = (kfile.readlines())
print (line_number)
correct_keyword = keywords[line_number-1]
print (correct_keyword)

user_guess = input("what is the correct keyword for the following definition?..."+" "+random_definition+"\n")
print (user_guess)
