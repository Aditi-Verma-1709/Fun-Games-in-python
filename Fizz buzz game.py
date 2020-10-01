# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
/This is a multiplayer game.You have to begin with any integer and replace the integer with fizz if it is divisible by 3, by buzz if it is divisible by 5 and by fizzbuzz if it is divisible by both 3 and 5.


a=1
while (a==1):
 x=input('write a number')
 x=int(x)
 if x%3==0 and x%5==0:
        print(x,'= fizzbuzz')
 else:
        if x%3==0:
            print(x,'= fizz')
        else:
            if x%5==0:
             print(x,'= buzz')
            else:
             print(x,'is neither fizz or buzz')
 
