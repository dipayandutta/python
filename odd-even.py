'''
Purpose :- get more familier with odd even number calculation
            using if-else conditional logic of python!
        
Author  :- Dipayan Dutta
'''

#reading a number to check if it is odd or even
number = input ("Enter a numbre to check it is odd or even")

#put a check if user entering a negative number
if (number < 1):
    print "Please enter a positive number"
elif (number %2 == 0):
    print "Even number"
else:
    print "odd Number"