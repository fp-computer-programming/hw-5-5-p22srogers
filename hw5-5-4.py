# Author: SMR(AMDG) 11/02/21
# Inputs
word_1 = str(input("Please enter a word: "))
word_2 = str(input("Please enter another word: "))
word_3 = str(input("Please enter the last word: "))
# Cases
a = word_1.lower()
b = word_2.lower()
c = word_3.lower()
# Print Statements
if(a < b and a < c):
    if(b < c):
        print(a, b, c)
    else:
        print(a, c, b)
elif(b < a and b < c):
    if(a < c):
        print(b, a, c)
    else:
        print(b, c, a)
elif(c < a and c < b):
    if(a < b):
        print(c, a, b)
    else:
        print(c, b, a)
# Tested w/ Alpha, Bravo, Charlie
