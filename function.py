'''
    Purpose :- To get familier with python functions
    Author :- Dipayan Dutta
'''
#Defination of Function One
def function_one():
    print "Inside function One"

#Defination of Function Two 
def function_two():
    number = input("Enter number")
    print "Entered Numberd ",number

#Third Function which checks number , number and max_number
    #passed as argument
def check(number,max_number):
    if(number>max_number):
        print "Number is greater than max number"
    elif (number < max_number):
        print "Number is less than max number"
    elif(number == max_number):
        print "Both Number are equal"
    else:
        print "some Thing Else"

#function defination inside another function
#Here i have to just call the function_four to get the addition result
        
def function_four():
    def addition(number1,number2):
        print "Given Number First One",number1
        print "Given Number Second One ",number2
        add = number1 + number2
        print "Addition Result ",add

    number1 = input("Enter first number")
    number2 = input("Enter Second number")
    f_five = addition(number1,number2)
    

function_one()#calling function one
function_two()#calling function two
check(10,20)#calling check function with first cond
check(21,20)#calling check function with second cond
check(20,20)#calling check function with third cond
function_four() #calling function four                   
