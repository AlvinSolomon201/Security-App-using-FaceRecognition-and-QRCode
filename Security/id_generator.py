import math
import random

# function to generate 6 digit ID 
def generateID():
    # Declare a digits variable
    # which stores all digits
    digits = "0123456789"
    ID = ""

   # length of password can be chaged
   # by changing value in range
    for i in range(6) :
        ID += digits[math.floor(random.random() * 10)]

    return ID
