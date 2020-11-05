import random
import re
import json
import datetime

from datetime import date, time, datetime
today = date.today()
#future = datetime.date(birthday)
#diff = future - today
#print(diff.days)


#Questions for our test

#save the answer into a text file
def quiz_answer(answer):
    with open("answers.txt", "a") as file:
        file.write(answer+"\n")

def show():
    with open("answers.txt") as file:
        for line in file:
            print(line)
            
if __name__ =='__main__':
    quiz_answer(input("What is your answer? "))

#Collect user's infomation
user_name = input("What is your name? (First + Last)")
print("Hello ", user_name, ". \n")
# (NEED TO FIX )user_birthday = int(input("What is the month and day of your Birthday? (mm/dd) \n"))
 
#FEATURE: Implement a "master loop" console ...
#Create Main Menu to chose to play or to exit
def main_menu():
    print("Welcome to the World Stats Question test. \n")
    print("Today is ", today)
    #future = datetime.date(user_birthday)
    #diff = future - today
    #print(diff.days)
    #calculate days till your birthday ???
    print("Please select an option below.")
    print("1. Answer World Statistics Questions")
    #option to build a game feature
    print("2. Play Pong Game")
    print("3. Choose Your own adventure Game ")
    print("Enter 0 to Exit the Program")
    choice = input("\n Enter 1, 2, 3, or 0: ")
    if choice == "1":
        world_stat_quiz()
    elif choice =="2":
        print("*** Sorry, that feature is not complete yet. \n")
        main_menu() 
    elif choice =="3":
        print("*** Sorry, that feature is not complete yet. \n")
        main_menu()           
    elif choice == "0":
        print("\n Thanks for visiting")
        quit()

        
def world_stat_quiz():
    score = 0  
    count = 5 #this is the number of questions in the quiz.  
    print("According to the United Nations: ... ") 
    '''
    #FEATURE Create a (dictionary or) list, populate it with several values, retrieve at least one value, and use it in the program.
    answer_list = ['answer1', 'answer2', 'answer3', 'answer4', 'answer5']
    mix = random.choice(answer_list)
    print(mix)
    '''
    #random    Ask question
    answer1 = input("\n What is the percent of the world's population that has access to electricity? \n a. 20% \n b. 50% \n c. 80% \n \n Answer: ").lower() #c
    '''#for loop to check for valid answer
    if answer1 != "a" or "b" or "c":
        answer1 = input("That is not a valid answer, please re-enter your answer a, b, or c: ")
    else:
        print("Your answer has been tallied.")
    '''
    if answer1 == "c":
        score += 1

    answer2 = input("\n In all low income countries, how many girls finish primary school? \n a. 10% \n b. 40% \n c. 60% \n \n Answer: ").lower() #c
    if answer2 == "c":
        score += 1

    answer3 = input("\n Were does the majority of the world's population live? \n a. In Low Income Countries \n b. In Middle Income Countries \n c. In High Income Countries \n \n Answer: ").lower() #b
    if answer3 == "b":
        score += 1

    answer4 = input("\n In the last twenty (20) yeatrs, the proportion of the world's population that lives in extreme poverty has...? \n a. almost doubled \n b. remained approximately the same \n c. almost dropped by half. \n \n Answer: ").lower() #c
    if answer4 == "c":
        score += 1

    answer5 = input("\n What is the life expectancy of the world today? \n a. 50 years \n b. 60 years \n c. 70 years \n \n Answer: ").lower() #c
    if answer5 == "c":
        score += 1

    print("Your final score for the quiz is", score, ". \n")
    #calculate the percentage of correct answers =correctAnswers/totalQuestions
    score_percent = score/count*100

    #Give a score result message
    if score_percent == 100:
        print("You got a perfect score! 100% \n")
        main_menu()
    elif score_percent >= 70:
        print("You scored a ", str(score_percent), "%.  That is impressive. \n")
    elif score_percent >=33:
        print("You scored a ", str(score_percent), "%.  That is actually better than most people. \n")
    else: 
        print("You scored a ", str(score_percent), "%.  A wild chimpanzee making random guesses would likely score higher than you did. \n")
    retry = input("Would you like to re-try the quiz? Y/N ").upper()
    if retry == "Y":
        world_stat_quiz()
    else:
        results = input("Would you like to see the correct answers? Y/N ").upper()
        if results == "Y":
            #Print questions with answers
            print("\n blah blah blah \n")
            main_menu()
        else:
            main_menu()

main_menu()

