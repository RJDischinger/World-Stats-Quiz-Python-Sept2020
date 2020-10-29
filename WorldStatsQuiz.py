import turtle
import json
import re
#?????
open ("factfulnessQuestions.py", "a")
import random

#regex
string = '1234567890'
good_numbers = re.findall(r' [^567]', string)
print(good_numbers)


#Quiz to test basic world knowledge
#Credited to Hans Rosling, Ola Rosling, and Anna Rosling Ronnlund

answer1 = input("What is the percent of the world's population that has access to electricity? \n a. 10% \n b. 40% \n c. 80% \n \n Answer: ")


#Collect user's infomation
user_name = input("What is your name? (First + Last)")
print("Hello ", user_name, ".")

def get_questions():

    questions = []
    questions.append([answer1, "c"])
    questions.append([answer2, "c"])
    questions.append([answer3, "c"])

    return questions

#Questions  Ask all questions before showing answers.
def ask_questions():

    #Load the questions
    factfulness_questions = get_questions()

    #Randomize the questions asked
    random.shuffle(factfulness_questions)

    score = 0

    for q in get_questions:
        print("Question: " +q[0])

    #user enters guess
    guess = input("Enter a, b, or c: ")

    if guess == q[1]:
        print("Your answer has been stored")
        score += 1
    








#Check to make sure a valid answer is given
test_answer = " "
if test_answer !="a" or test_answer !="b" or test_answer !="c":
    print("Please check your answer.  You chose an invalid response.")
else:
    print("i dont know what to do next")

###Create a loop to check answers: Do not display answers until all questions are answered.
if answer1 == "c" or answer1 == "C" or answer1 == "80%":
    score += 1
    print("Correct!")
    print("Score: ", score)
    print("\n")
else:
    print("Sorry, that is not correct.")
    print("Score: ", score)
    print("\n")

#Score results
#Show the questions with the user's answers and the correct answers

#calculate the percentage of correct answers =correctAnswers/totalQuestions
score_percent = score/10

#Give a score result message
if score_percent == 100:
    print("You got a perfect score!")
elif score_percent >= 70:
    print("You scored a ", + str(score_percent), ".  That is impressive.")
elif score_percent >=33:
    print("You scored a ", str(score_percent), ".  That is actually better than most people.")
else: 
    print("You scored a ", str(score_percent), ".  A wild chimpanzee making random guesses would likely score higher than you did.")


#Create Main Menu to chose to play or to exit
def main_menu():
    print("Welcome to the Factfuilness Question test.")
    print("Please select an option below.")
    print("1. Answer the Questions")
    print("Enter 0 to exit")
    choice = input("Enter 1 or 0: ")
    if choice == "1":
        ask_questions()
    elif choice == "0":
        print("Thanks for visiting")
        quit()

