# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 21:35:34 2020

@author: HP
"""
#This is a two player game. The computer will show you some jumbled alphabets which belong to a single word from a list specified by you only earlier. If you enter the correct word you will have gained one point and if not, the chance will then be moved to another player.
import random


def choose():
    words=['rainbow','science','water','legislation','element','aditi']
    pick=random.choice(words)
    return pick

def jumble(word):
    jumbled="".join(random.sample(word,len(word)))
    return jumbled

def thank(p1name,p2name,pp1,pp2):
    print(p1name,'Your score is:',pp1)
    print(p2name,'Your score is:',pp2)
    print('Have a nice day',p1name,'and',p2name)
    




def play():
    p1name=input('Player 1,Please enter your name')
    p2name=input('player 2,Please enter your name')
    pp1=0
    pp2=0
    turn=0
    c=0
    while(c==0):
        #Computer,s task
        picked_word=choose()
        #Creating the question
        qn=jumble(picked_word)
        print(qn)
        #Player 1
        if turn%2==0:
            print(p1name,'This is your turn.')
            ans=input('What is on my mind?')
            if ans==picked_word:
                pp1=pp1+1
                print('Your score is:',pp1)
            else:
                print('Better luck next time.I thought:',picked_word)
            c=input('Press 1 to continue and 0 to quit:')
            if c==0:
                thank(p1name,p2name,pp1,pp2)
                break
       #Player 2
        else:
            print(p2name,'This is your turn.')
            ans=input('What is on my mind?')
            if ans==picked_word:
                pp2=pp2+1
                print('Your score is:',pp2)
            else:
                print('Better luck next time.I thought:',picked_word)
            c=input('Press 1 to continue and 0 to quit:')
            if c==0:
                thank(p1name,p2name,pp1,pp2)
                break  
        turn=turn+1    
            
play()
