#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    count= 10
    while count in range (10,0,-1):
        print (count)
        count=1
        print ("Happy New Year!")
    #happy_new_year()
    pass

def square_integers(int_list):
    # code goes here!
    return [x ** 2 for x in int_list]
    pass

def fizzbuzz():
    # code goes here!
    for i in range (1,101):
        if 1 % 3==0 and 1 % 5==0:
           print("FizzBuzz") 
        elif 1% 3==0:
            print("Fizz")
        elif 1% 5==0:
            print("Buzz") 
        else: print (i) 
    # fizzbuzz()
    pass
