# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 11:49:37 2020

@author: HP
"""


import numpy
board=numpy.array([['-','-','-'],['-','-','-'],['-','-','-']])
p1s= 'X'
p2s='O'





def place(symbol):
    print(numpy.matrix(board))
    while(1):
        
        row=int(input('Enter your row position--1/2/3 :'))
        column=int(input('Enter your column position--1/2/3 :'))
       
      
        if (row>0 and row<4 and column>0 and column<4 and board[row-1][column-1]=='-'):
            break
        else:
            print('Invalid input. Please try again.')
    symbol=board[row-1][column-1]     


def won(symbols):
    check_rows(symbol) or check_columns(symbols) or check_diagonals(symbols)
    


def check_rows(symbols):
    for r in range(3):
        count=0
        for c in range(3):
            if board[r][c]==symbol:
                count=count+1
        if count==3:
            print(symbol,'has won')
            return True
        else:
            return False
    



def check_columns(symbols):
    for c in range(3):
        count=0
        for r in range(3):
            if board[r][c]==symbol:
                count=count+1
        if count==3:
            print(symbol,'has won')
            return True
        else:
            return False    
    


def check_diagonals(symbols):
    if (board[0][0]==board[1][1]==board[2][2]==symbol or board[0][2]==board[1][1]==board[2][0]==symbol):
        print(symbol,'won')
        return True
    else:
        return False
   





    
    

def play():
    for turn in range(9):
        if (turn%2==0):
            print('X turn')
            place(p1s)
            if won(p1s):
                break
        else:
            print('O turn')
            place(p2s)
            if won(p2s):
                break
    if not(won(p1s)) and not(won(p2s)):
        print('It is a draw')
        
play()           
                