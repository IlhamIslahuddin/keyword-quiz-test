#keyword question maker

import random
def initialise():
    file = open("definitions.txt", "r")
    search = file.read()
    global num_of_lines
    num_of_lines = 1
    for characters in search:
        if characters == "\n":
            num_of_lines = num_of_lines + 1
    global score
    score = 1
    return score

def find_LN():
    global line_number
    line_number = random.randint(1,num_of_lines)
    return line_number

def find_RD():
    dfile = open("definitions.txt")
    definitions = (dfile.readlines())
    global random_definition
    random_definition = definitions[line_number-1]
    return random_definition

def find_CK():
    kfile = open("keywords.txt")
    global keywords
    keywords = (kfile.readlines())
    global correct_keyword
    correct_keyword = keywords[line_number-1]
    return correct_keyword
    
def score_write():
    global score
    score = score + 1
    return score


def guess():
    correct = True
    while correct == True:
        find_LN()
        find_RD()
        find_CK()
        user_guess = str(input("What is the correct keyword (in all caps) for the following definition?...\n"+random_definition+"\n"))
        if (user_guess) == str(correct_keyword[0:len(correct_keyword)-1]):
            print ("Correct! Your current score is:",score)
            score_write()
        else:
            print ("Incorrect. The correct answer was:",correct_keyword[0:len(correct_keyword)-1],"\nGame Over.")
            print ("Your final score is:",score)
            correct = False

initialise()
guess()
