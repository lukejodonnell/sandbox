# -*- coding: utf-8 -*-
"""
Created on Fri May 15 

@author: Andrew St.Germain
"""

def TicTacToe():
    legalMoves = ["a1","a2","a3","b1","b2","b3","c1","c2","c3"]
    board = createBoard()
    print(board)
    move = askForMove(legalMoves)
    print(move)

def createBoard():
    topLine = "  1 2 3 " + "\n"
    #emptyLine = "         " + "\n"
    spacesLine = "  | |  " + "\n"
    lineLine = " -------" + "\n"
    board = topLine + "a" + spacesLine + lineLine + "b" + spacesLine + lineLine + "c" + spacesLine
    return(board)

def isLegal(move,legalMoves):
    for legalMove in legalMoves:
        if move == legalMove:
            return True
    return False

def updateLegalMoves(move,legalMoves):
    legalMoves.remove(move)

def askForMove(legalMoves):
    move = raw_input("Enter the coordinate of your next move (Ex. a2): ")
    legal = isLegal(move,legalMoves)
    if legal == False:
        print("Move invalid, please enter a valid move.")
        move = askForMove(legalMoves)
    else:
        return(move)




TicTacToe()