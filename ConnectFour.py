#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  13 03:05:21 2018

@author: liyunqiu
"""

# Yunqiu(Julie) Li
# Assignment 3 Connect Four

import random

def drawConnectFourBoard(board):
    #assuming board has at least 1 row.
    boardRow = len(board)
    boardColumn = len(board[0])
    
    for y in range(boardRow - 1 , -1, -1):
        print(str(y+1) + '|', end='')
        for x in range(boardColumn):
            print(board[y][x] + '|', end='')
        print()
    print('  1 2 3 4 5 6 7 ')
    

def inputPlayerLetter():
    # Lets the player type which letter they want to be.
    # Returns a list with the player's letter as the first item, and the computer's letter as the second.
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Do you want to be X or O?')
        letter = input().upper()

    # the first element in the tuple is the player's letter, the second is the computer's letter.
    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']

def whoGoesFirst():
    # Randomly choose the player who goes first.
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'

def playAgain():
    # This function returns True if the player wants to play again, otherwise it returns False.
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')

def makeConnectFourMove(board, letter, move):
    numberOfRow = len(board)
    for y in range(numberOfRow):
        if board[y][move] == ' ':
            board[y][move] = letter
            break
        else:
            continue

def isConnectFourWinner(board, letter):
    boardRow = len(board)
    boardColmun = len(board[0])
    for row in range(boardRow):
        for col in range(boardColmun):
            if letter == board[row][col] \
                and row + 1 < boardRow and letter == board[row +1][col]\
                and row + 2 < boardRow and letter == board[row +2][col]\
                and row + 3 < boardRow and letter == board[row +3][col]:
                    return True
            if letter == board[row][col]\
                and row + 1 < boardRow and col + 1 < boardColmun \
                and letter == board[row +1][col+1]\
                and row + 2 < boardRow and col + 2 < boardColmun \
                and letter == board[row +2][col+2]\
                and row + 3 < boardRow and col + 3 < boardColmun \
                and letter == board[row +3][col+3]:
                    return True
            if letter == board[row][col]\
                and col -1 >= 0 and row + 1 <boardRow\
                and letter == board[row+1][col -1]\
                and col -2 >= 0 and row + 2 <boardRow\
                and letter == board[row+2][col -2]\
                and col -3 >= 0 and row + 3 <boardRow\
                and letter == board[row+3][col -3]:
                    return True
    return False
                

def getBoardCopy(board):
    # Make a duplicate of the board list and return it the duplicate.
    dupeBoard = []

    for i in board:
        dupeBoard.append(i)

    return dupeBoard

def isConnectFourSpaceFree(board, move):
    #only check if the top row[move] is taken.
    return board[len(board)-1][move-1] == ' '
def isSpaceFree(board, move):
    # Return true if the passed move is free on the passed board.
    return board[move] == ' '
def getConnectFourPlayerMove(board):
    move = ' '
    while move not in '1 2 3 4 5 6 7'.split() or not isConnectFourSpaceFree(board, int(move)):
        print('What is your next move? (1-7)')
        move = input()
    return int(move)

def chooseRandomMoveFromList(board, movesList):
    # Returns a valid move from the passed list on the passed board.
    # Returns None if there is no valid move.
    possibleMoves = []
    for i in movesList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)

    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None


def isConnectFourBoardFull(board):
    boardColmun = len(board[0])
    for col in range(boardColmun):
        if (isConnectFourSpaceFree(board, col)):
            return False
    return True


print('Welcome to Tic Tac Toe!')

while True:
    connectFourBoard = []
    connectFourBoardColumn = 7
    connectFourBoardRow = 6
    
    for y in range(connectFourBoardRow):
        connectFourBoard.append([])
        for x in range(connectFourBoardColumn):
            connectFourBoard[y].append(' ')
    drawConnectFourBoard(connectFourBoard)
    # Reset the board
    theBoard = [' '] * 10
    playerLetter, computerLetter = inputPlayerLetter()
    #change to player for testing
    turn = 'player'
    print('The ' + turn + ' will go first.')
    gameIsPlaying = True
    while gameIsPlaying:
        if turn == 'player':
            # Player's turn.
            drawConnectFourBoard(connectFourBoard)
            move = getConnectFourPlayerMove(connectFourBoard)
            makeConnectFourMove(connectFourBoard, playerLetter, move-1)

            if  isConnectFourWinner(connectFourBoard, playerLetter):
                drawConnectFourBoard(connectFourBoard)
                print('Hooray! You have won the game!')
                gameIsPlaying = False
            else:
                if isConnectFourBoardFull(connectFourBoard):
                    drawConnectFourBoard(connectFourBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'computer'
        else:
            # Computer's turn.
            move = random.randint(0, len(connectFourBoard[0])-1)
            makeConnectFourMove(connectFourBoard, computerLetter, move)

            if  isConnectFourWinner(connectFourBoard, computerLetter):
                drawConnectFourBoard(connectFourBoard)
                print('The computer has beaten you! You lose.')
                gameIsPlaying = False
            else:
                if isConnectFourBoardFull(connectFourBoard):
                    drawConnectFourBoard(connectFourBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'player'

    if not playAgain():
        break
