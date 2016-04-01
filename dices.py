#!/usr/bin/python

# Version 1.0.0 released 01/04/2016 by Le_minaw.
# This work is released under GPL licence.

# This script is used to generate Dungeons and Dragons dices rolls.
# Dices are described as 'ndx', with n the number of dices to roll, d the d letter and x the number of faces a dice has.
# For exemple, '2d8' stands for 2 dices of 8 faces.
# Direct acces from a command line is supported : typing 'python dices.py 2d8' will work.
# It is possible to run the program in interactive mode with the 'interact' parameter. In this mode, the program will generate dice roll as soon as a code is entered, so typing directly '2d8' will perform the dice roll. It will also run in loop, meaning that you can enter another code directly afer a roll performs. Typing 'exit' will likely kill the program.

import sys
import re
from random import randint

def gen(dicesNumber, dicesFaces):
    dices = []
    for i in range(0, dicesNumber):
        dices.append(randint(1,dicesFaces))
    return dices

def prnt(args):
    args = args.split("d")
    if len(args) == 1:
        print gen(1, int(args[0]))
    else:
        print gen(int(args[0]), int(args[1]))
    print "Alea jaceta est."

if __name__ == "__main__":
    regexp = re.compile("^\d+d\d+$")
    if len(sys.argv) == 2:
        if regexp.match(sys.argv[1]) != None:
            prnt(sys.argv[1])
        elif sys.argv[1] == "interact":
            while 1:
                field = raw_input("Dices to gen ('exit' to quit) : ")
                if field == "exit":
                    print "Goodbye, adventurer."
                    exit()
                prnt(field)
        else:
            print "[ERROR] Incorrect argument " + str(sys.argv[1]) + " ! Try 'interact' or '2d10'."
    else:
        print "[ERROR] This script takes exactly one argument ! Given : " + str(len(sys.argv) - 1) + "."
