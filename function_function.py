'''
Purpose :- Example of Calling Function from another function
Author  :- Dipayan Dutta
'''

#Calc () function Defination
#Inside This function i have two functions
#Namely add (--,--) and sub(--,--)
#Depending on the user choice function will be called


def calc():
    
    number1 = input("Enter first number")#Reads first Number
    number2 = input("Enter Second Number")#Reads Second Number
    
    user_choice = input("Enter 1 to add 2 to subtract") #User Choice for func call
    
    def add(number1 , number2):
        addition = number1 + number2
        print "Addition Result " ,addition

    def sub(number1,number2):
        if (number1> number2):
            sub = number1 - number2
            print "Subtraction Result " ,sub
        elif(number1<number2):
            sub = number2 - number1
            print "Subtraction Result "sub
        else:
            print "Subtraction Result 0"

    if user_choice==1:
        addition = add(number1,number2) #if user choice 1 then call add
    elif user_choice == 2: #if 2 then call sub
        subtract = sub(number1,number2)
    else:#other wise print Message
        print "Invalid Choice"

calc()
