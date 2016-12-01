'''
    Purpose:- To get Familier with the conditional statements
    Author :- Dipayan Dutta
'''

#Taking number input 
number = input("Enter a number")

#now check if the number is greater than 10 or not

if (number<=10):
    print "Number is less than 10 "
#now check if is the number is in between range of 11 to 20
elif (number>11 and number <=20):
    print "Number is in between 11 to 20"

#similarly check range of 20 to 30
elif(number>20 and number<=30):
    print "Number is in between 20 to 30"
    
else:
    print "Number is Greater than 30"