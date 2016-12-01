#!/usr/bin/python
'''
    Purpose:- Explation of the print statement
              how to print Text on your screen
    Author :- Dipayan Dutta
'''
print "Hello World!" #print statement in python

#printing with variable value

number = 10;
string = "Message";

print "Number Value is ",number
print "String Value is ",string

#now check the variable types as python dont need to decleare data type

print "Number variable type is ",type(number)
print "String variable type is ",type(string)

#to convert datatypes lets say i want to convert number int to number string

number_converted_string = str(number)
print "Number is now string datatype ",number_converted_string
print "data type of number variable is ",type(number_converted_string)

#Reading user input 
#Reding int type inputs

number = input("Please Enter a number ")
print "Entered Number is ",number

#Reading String input 

string = raw_input("Please Enter a string ")
print "Entered String ",string