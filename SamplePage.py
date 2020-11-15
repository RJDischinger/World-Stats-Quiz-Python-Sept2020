import json
import re
import random

print("\n--------------------------------------")
print("This is the WorldStatsQuiz sample page \n")

#regex
print("Here are some REGEX samples that I need to develop")
string = '1234567890'
good_numbers = re.findall(r'[^567]', string)
print(good_numbers)

odd_numbers = re.findall(r'[^13579]', string)
print(odd_numbers)

print("\n End of Sample Page Stuff \n")

