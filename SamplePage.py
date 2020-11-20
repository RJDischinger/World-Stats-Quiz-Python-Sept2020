import json
import re
import random

print("\n--------------------------------------")
print("This is the WorldStatsQuiz sample page \n")

#regex
def regex_samples():
    print("Here are some REGEX samples that I need to develop")
    string_of_numbers = input("Enter a block of numbers that you want to analyze:")
    even_numbers = re.findall(r'[^13579]', string_of_numbers)
    print("The even numbers in this sequence are:",even_numbers)

    odd_numbers = re.findall(r'[13579]', string_of_numbers)
    print("The odd numbers in this sequence are:",odd_numbers)

responce = input("Do you want to try some number analysis? (Y/N) ").upper()
if responce == "Y":
    print("Let's get started.")
    regex_samples()
else:
    print("Enjoy your stay.")

#Sample function that returns a value
def cube(x):
    y = int(x * x * x)
    return y

number_to_cube = input("What number would you like to cube? ")
result = cube(int(number_to_cube))  
print("The result of", number_to_cube, "cubed is", result,". \n")


print("\n End of Sample Page Stuff \n")

