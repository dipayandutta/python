'''
Purpose :- Example program to get familier with
            most frequently used methods present
            in the math module

Author :- Dipayan Dutta
'''

#import every thing from the math module

from math import *

#Calculate the square root of a number
print "Square root of 16 is ",sqrt(16)
print "Square root of 2.3 is ",sqrt(2.3)

#Calculate the e^x

print "e^2 = ",exp(2)

#calculate the value of log 12

print "log 12 = " ,log(12)

#calculate the value of log base 10 values
print "Log 3 base 10 i.e. log10(3) ",log10(3)

#calculate 2 to the power 3 i.e. 2^3
print "2 to the power 3 is ",pow (2,3)

#calculate the value of a sin angle returns in radians
print "Sin of 45 in radians ", sin(45)

#calculate the value of cos angle , returns in radians
print "cos of 45 in radians ", cos(45)

#calculate the value of tan angle , returns in radians
print "Tan of 45 in radians ",tan(45)

#Convert radian value into degree value

print "1 Radian = ", degrees(1), " degree"

#Convert degree value into radian value

print "57.29577 Radians in degree = ",radians(57.59577)

#To print the absolute value

print "Abslute value of 1.23 is ",fabs(1.23)

 #To get the ceiling of a float value say x

print "Ceil of 1.23 is = ",ceil(1.23)

#To get the floot of a float value say x

print "Floor of 1.23 is = ",floor(1.23)

#Calcluate the factorial of a number

print "Factorial of 5 is ",factorial(5)

#Calculate the sum of an array

print "Summation of an array [1,2,3] = ",sum([1,2,3])

#Calculate the floating point summation of an array

print "Floating point summation [1.2,3.4 ] = ",fsum([1.2,3.4])

#To get the value of pi

print "Value of pi = " ,pi

# To get the value of e

print "value of e = ",e

# To get the arc cos , value should be in between -1 to 1

print "Arc Cos of -.45 =",acos(-.45)

# To get the arc sin ,
print "Arc  sin of .45 = ",asin(.45)
