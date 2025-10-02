import math

# print(math.sqrt(16))
# print(math.pow(2,3))
# print(math.pi)

import random
# print(random.random())
# print(random.randint(0,10))
# print(random.choice(["red","blue","black","pink"]))

import datetime

# thisday = datetime.date.today()
# print(thisday)
# timeNow = datetime.datetime.now()
# print(timeNow)

import os
# print(os.name)
# print(os.getcwd())
# os.mkdir("NewFolder")
# print(os.path)

# import sys
# print(sys.version)

# json
import json
data = {
    "name":"xyz",
    "age":22
}


# jsonStr = "{
#     "name":"xyz",
#     "age":22
# }"
# jsonStr = json.dumps(data)
# # print(jsonStr)

# newValue = json.loads(jsonStr)
# # print(newValue)
# print(type(jsonStr))
# print(type(newValue))


# re - regular expression
import re
# text = "my Mobile number 8744664849"
# num = r'\d{10}'

# match = re.search(num,text)
# if match:
#     print("Number found:",match.group())


# password
passw = "MyPassword@123"

pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[#@$%!&^*?<>]).{8,}$'
if re.match(pattern,passw):
    print("Strong Password")
else:
    print("This not strong Password")


from functions import greet

greet()