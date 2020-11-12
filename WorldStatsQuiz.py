import turtle
import json
import re
import random

#questions2 = open ('WorldStatsQuestions.py', 'a')



#regex
string = '1234567890'
good_numbers = re.findall(r'[^567]', string)
print(good_numbers)

odd_numbers = re.findall(r'[^13579]', string)
print(odd_numbers)


