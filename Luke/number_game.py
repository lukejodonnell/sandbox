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


game()


