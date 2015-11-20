import random
import time

def game():
        secret = random.randint(1, 100)
        guess = 0
        tries = 0
        firstTime = True
        time.sleep(1)
        print " "
        print "I'm the count and I'm thinking of a number"
        time.sleep(2)
        print " "
        print "It's between 1 and 99. You have 6 tries"
        time.sleep(2)
        print " "
        print "Ready."
        for t in range(5):
            print "."
            time.sleep(0.5)
        print "GO!!"
        while guess != secret and tries < 6:
            time.sleep(1)
            print " "
            if firstTime == True:
                guess = input("Just try and guess it.")
                firstTime = False
            else:
                guess = input("Try again.")
            time.sleep(0.5)
            if guess < secret:
                print "that number is to low"
            elif guess > secret:
                print "that number is to high"
            tries = tries + 1
        if guess == secret:
            print " "
            print "Zatz RIGHT!"
            time.sleep(0.5)
            print "yeah"
        else:
            time.sleep(1)
            print " "
            print "That, was you last try"
            time.sleep(1)
            print " "
            print "Sorry"
            time.sleep(1)
            print " "
            print "the right number was", secret
        doesHe = raw_input("Do you want to play again?")
        if doesHe == "yes" or doesHe == "yeah" or doesHe == "Yes" or doesHe == "Yeah" or doesHe == "you know it" or doesHe == "shut up" or doesHe == "y" or doesHe == "why not?" or doesHe == "why not" or doesHe == "of course" or doesHe == "duh" or doesHe == "!@#$% yeah" or doesHe == "maybe" or doesHe == "meh":
            game()
        else:
            time.sleep(1)
            print ""
            print "O.K. Bye"

p = ["_ ","_ ","_ ","_ ","_ ","_ ","_ ","_ ","_ "]

def drawTTTBoard():
        print " "
        print p[0]+p[1]+p[2]
        print p[3]+p[4]+p[5]
        print p[6]+p[7]+p[8]

def resetPlaces():
        looper = 0
        while looper <= 8:
            p[looper] = "_ "
            looper = looper+1
def comTurn():
       cSpace = random.randint(0, 8)
       p[cSpace] = "O "
       drawTTTBoard()

def humanTurn():
        hSpace = input("Which space?")
        if hSpace < 1 or hSpace > 9:
            print "pick a real space loser"
            humanTurn()
        else:
             hSpace = hSpace - 1
             p[hSpace] = "X "
             drawTTTBoard()
def newgame():
        resetPlaces()
        intructions = "n"
        print "Welcome to tic-tac-toe"
        print " "
        time.sleep(0.25)
        instructions = raw_input("Do you want instructions (y,n)")
        if instructions == "y":
            print "This is a text based tic-tac-toe game.  You will always go first.  The board will displayed with an X for X's an O for O's and a _ for blank spaces.  The computer will always pick randomly."
            print " "
            time.sleep(1)
            print "let's start"
            print " " 
            time.sleep(1)
        else:
            print "alright let's go"
            print " "
        drawTTTBoard()
        humanTurn()
        comTurn()

print "which game do you want to play"
gameChoise = raw_input("Tic-Tac-Toe or Numbers?")
if gameChoise == "Tic-Tac-Toe":
    newgame()
else:
    if gameChoise == "numbers":
        game()
    else:
        print "What?"



