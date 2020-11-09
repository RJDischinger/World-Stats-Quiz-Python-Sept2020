import random
import re   #REGEX
import json
import datetime 


from datetime import date, time, datetime
date_format = "%m/%d/"
now = datetime.now()
christmas = datetime(now.year, 12, 25)
delta = christmas - now
final = delta.days

today = date.today()

#FEATURE Create and call at least 3 functions, ...
def christmas_greeting():
    if final > 0:
        print(final, "days until Christmas!")
    elif final == 0:
        print ("Merry Christmas!")
    elif final < 0:
        print ("I hope you had a great Christmas.  Have a Happy New Year.")

"""
#def birthday_greeting():
    #future = datetime.date(birthday)
    #user_birthday = datetime(now.year, mm, dd)
    #diff = future - today
    #print(diff.days)
 #call function for date options
    #future = datetime.date(user_birthday)
    #diff = future - today
    #print(diff.days)
    #calculate days till your birthday ???
    
import os
import datetime

def create_daily_dir(string, path='financial'):
    # try to decode date string to a datetime
    try:
        this_date = datetime.datetime.strptime( string, "%Y-%m-%d" ) #format type YYYY-mm-dd
    except:
        this_date = datetime.datetime.strptime( string, "%m-%d-%Y" ) #format type mm-dd-YYYY
    # convert back to the proper format    
    date_str = datetime.datetime.strftime(this_date, '%Y-%m-%d')
    os.makedirs(os.path.join(path, date_str))
"""

#save the answer into a text file
def quiz_answer(answer):
    with open("answers.txt", "a") as file:
        file.write(answer+"\n")

def show():
    with open("answers.txt") as file:
        for line in file:
            print(line)
            
if __name__ =='__main__':
    quiz_answer(input("How are you today? "))

#Collect user's infomation  
def user_info():
    user_name = input("What is your name? (First + Last)")
    print("Hello ", user_name, ". \n")
    christmas_greeting()
    #FEATURE  Use regex to verify month and date inputs
    #use warnings;
    birth_month = input("What is the month of your Birthday? (mm) ").lower()
        #birth_month = "^(0?[1-9]|1[012])$"
    birth_day = input("What is the day of your Birthday? (dd) ").lower()
        #birth_day = "(0[1-9]|[12]\d|3[01])"
    #birthday_greeting()
    main_menu()

#FEATURE: Implement a "master loop" console ...
#Create Main Menu to chose to play or to exit

def opening_menu():
    print("**************************************")
    print("Welcome Visiter \n")
    print("Today is ",today) 
    print(" ")
    user_info_request = input("Would you like to tell us about yourself? Y/N ").lower()
    if user_info_request == "y":
        user_info()
    else:
        print("Enjoy your visit. \n")
        main_menu()

def main_menu():
    print("**************************************")
    print("Welcome to the Main Menu")
    print("------------------------")
    print("Please select an option below.")
    print("1. Answer World Statistics Questions")
    #option to play a game feature
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
        print("\n Thanks for visiting \n")
        quit()

#Questions for our test

def world_stat_quiz():
    score = 0  
    count = 5 #this is the number of questions in the quiz.  
    print("\nAccording to the United Nations: ... ") 
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
        print("Your answer has been tallied.")
    else:
        answer1 = input("That is not a valid answer, please re-enter your answer a, b, or c: ").lower()
    '''
    if answer1 == "c":
        score += 1

    answer2 = input("\n In all low income countries, how many girls finish primary school? \n a. 10% \n b. 40% \n c. 60% \n \n Answer: ").lower() #c
    if answer2 == "c":
        score += 1

    answer3 = input("\n Were does the majority of the world's population live? \n a. In Low Income Countries \n b. In Middle Income Countries \n c. In High Income Countries \n \n Answer: ").lower() #b
    if answer3 == "b":
        score += 1

    answer4 = input("\n In the last twenty (20) years, the proportion of the world's population that lives in extreme poverty has...? \n a. almost doubled \n b. remained approximately the same \n c. almost dropped by half. \n \n Answer: ").lower() #c
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
            #Print the answers to the questions
            print("_______________________________________________________________")
            print("80% percent of the world's population has access to electricity.")
            print("In all low income countries, 60% of girls finish primary school.")
            print("The majority of the world's population lives in Middle Income Countries.")
            print("In the last twenty (20) years, the proportion of the world's population that lives in extreme poverty has almost dropped by half.")
            print("The life expectancy of the world population today is 70 years.")
            print("_______________________________________________________________")
            main_menu()
        else:
            print("")
            main_menu()

opening_menu()
#main_menu()
