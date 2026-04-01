#!/usr/bin/env python3

import argparse

###----------------------- accept and parse command line arguments
#create an argument parser object 
# inside the module there are bunch of functions
parser = argparse.ArgumentParser(description="This script calculates the number at a given position \
                                 in the Fibonacci sequence")

#add a positional argument, in this case, the position in the Fibonacci sequence
parser.add_argument("position", help="Position in the Fibonacci sequence", type=int)

# an optional argument in this case, the position in the fibonacci sequence
#if 'store_true' this means assign 'TRUE' if the optional argument is specified
#on the command line, so the default for 'store_true' is actually false
parser.add_argument("-v", "--verbose", help="Print verbose output", action='store_true')
# parse the arguments
args = parser.parse_args()


#prompt the their for their name
#position = input("Please enter a position in the Fibonacci sequence: ")
# we get rid of the sequence because we have the module and function

#initialize the integers
a,b = 0,1

#then we write a loop 
for i in range(int(args.position)):
    a,b = b,a+b

fibonacci_number = a 

if args.verbose:
    print(f"The fibonacci number for {args.position} is {fibonacci_number}.")
else:
    print(fibonacci_number)