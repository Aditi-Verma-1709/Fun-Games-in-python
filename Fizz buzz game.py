# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""



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
 