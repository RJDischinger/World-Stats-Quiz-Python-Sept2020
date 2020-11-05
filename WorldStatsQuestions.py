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
 

def main_menu():
    print("This is the Main Menu Area")

def world_stat_quiz():
    score = 0  
    print("According to the United Nations: ... ") 
    #random    Ask question
    answer1 = input("\n What is the percent of the world's population that has access to electricity? \n a. 20% \n b. 50% \n c. 80% \n \n Answer: ").lower() #c
    #for loop to check for valid answer
    '''if answer1 != "a" or "b" or "c":
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

    print("Your final score for the quiz is ", score, ".")
    retry = input("Would you like to re-try the quiz? Y/N ").upper()
    if retry == "Y":
        world_stat_quiz()
    else:
        results = input("Would you like to see the correct answers? Y/N ").upper()
        if results == "Y":
            #Print questions with answers
            print("blah blah blah")
            main_menu()
        else:
            main_menu()


world_stat_quiz()
