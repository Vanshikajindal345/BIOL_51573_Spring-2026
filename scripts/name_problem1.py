#! /usr/bin/env python3

# #problem 1 

 #1: Write a program that asks for the user's name and age, then prints a personalized greeting using string formatting (.format).

#For Andy and 32, the output would be:

# Hello, Andy! You are 32 years old.

# code here
name = input('Enter your name: ')
age  = input('Enter your age: ')

name = name.lower().capitalize()

print('Hello, {}. You are {} years old'.format(name, age))
print(f'Hello, {name}. You are {age} years old')

#Hello, Andy. You are 32 years old
#Hello, Andy. You are 32 years old

# spit out the brackets if we will fill in something but we left iy empty then the input. 
