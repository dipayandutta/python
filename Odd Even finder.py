''''
Given an integer,

, perform the following conditional actions:

If N is odd, print Weird
If N is even and in the inclusive range of 2to
, 5 print Not Weird
If N is even and in the inclusive range of6 to20
, print Weird
If N is even and greater than 20 , print Not Weird
''''
n = int(raw_input())

check = {True: "Not Weird", False: "Weird"}

print(check[
        n%2==0 and (
            n in range(2,6) or 
            n > 20)
    ])
