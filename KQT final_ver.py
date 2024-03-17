#keyword question maker
#destination of text files may need to be changed

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
    score = 0
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
    
def high_score(score):
     highscore = open("high score.txt","r")
     looked = highscore.readlines(0)
     if int(score) >= int(looked[0]):
       overwrite = open("high score.txt","w")
       overwrite.write(str(score))
       print ("| New High Score! ",score," |")
     elif int(score) == int(looked[0]):
         print ("| Tied For High Score. |")
     else:
         print ("|| Current High Score To Beat:",looked[0]," ||")
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
        user_guess = str(input("[ What is the correct keyword for the following definition?... ]\n"+random_definition+"\n"))
        if (user_guess) == str(correct_keyword[0:len(correct_keyword)-1]) or (user_guess.lower()) == str(correct_keyword[0:len(correct_keyword)-1].lower()):
            score_write()
            print ("| Correct! Your current score is:",score," |")
        else:
            print ("|| Incorrect. The correct answer was:",correct_keyword[0:len(correct_keyword)-1],"||""\n|| Game Over. ||")
            print ("|| Your final score is:",score," ||")
            high_score(score)
            correct = False

initialise()
guess()
