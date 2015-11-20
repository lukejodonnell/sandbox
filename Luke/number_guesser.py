import random
import time

def game():
        guess = 50
        info = "null"
	cont = False
        tries = 1
        time.sleep(1)
        print " "
        print "Think of a number in between 1 and 99, and I will guess it"
        time.sleep(2)
        print " "
        print "In just 6 tries!"
        time.sleep(2)
        print " "
        print "Ready."
        for t in range(5):
            print "."
            time.sleep(0.5)
        print "GO!!"
        while info != "right" and tries < 7:
            time.sleep(1)
            print " "
            print "I guess", guess, ":"
            time.sleep(1)
            info = raw_input("is that high, low, or right?")
            time.sleep(0.5)
            while cont == False:
                if info == "high":
                    print "that number is to low"
                    guess = guess - 50 / ( tries * 2 )
                    cont = True
                elif info == "low":
                    print "that number is to high"
                    guess = guess + 50 / ( tries * 2 )
                    cont = True
                elif info == "right":
                    cont = True
                else:
                    print "You need to say either 'high', 'low', or 'right'"
                    cont = False
            cont = False
            tries = tries + 1
        if info == "right":
            print " "
            print "Haaa, in yo Face!"
            time.sleep(0.5)
            print "YEAH!"
        else:
            time.sleep(1)
            print " "
            print "I have failed"
            time.sleep(1)
            print " "
            print ":("
            time.sleep(1)
        doesHe = raw_input("Do you want to play again?")
        if doesHe == "yes" or doesHe == "yeah" or doesHe == "Yes" or doesHe == "Yeah" or doesHe == "you know it" or doesHe == "shut up" or doesHe == "y" or doesHe == "why not?" or doesHe == "why not" or doesHe == "of course" or doesHe == "duh" or doesHe == "!@#$% yeah" or doesHe == "maybe" or doesHe == "meh":
            game()
        else:
            time.sleep(1)
            print ""
            print "O.K. Bye"


game()


