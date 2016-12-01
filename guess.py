'''
    Purpose :- Example program to check while loop
                
'''

import random

magic_number = random.randrange(1,10,1)

input_user = input("Enter number")
check = True 
while(magic_number != input_user):
    if (magic_number <= input_user):
        print "To Small"
        print "Enter Again"
        input_user = input("Enter number")
        print "Magic Number is " , magic_number
    elif(magic_number >= input_user):
        print "To Big"
        print "Enter Again"
        input_user = input("Enter number")
        print "Magic Number is " , magic_number
    elif (magic_number == input_user):
        print "Yes it is "
        break
    