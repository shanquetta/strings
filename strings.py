#!/usr/bin/env python3
"""
Kenzie assignment: Strings!
"""
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Instructions:
# Complete each function below by writing the code for it. main() is already
# set up to test all the functions with a few different inputs, printing 'OK'
# for each function once it returns the correct result.
# The starter code for each function includes a bare 'return' which is just a
# placeholder for your code.

# Your name, plus anyone who helped you with this assignment.
# Give credit where credit is due.
__author__ = "Shanquetta Pelzer, Kano help, realpython.com, Workshop, stackoverflow.com, LinkedIn Learning"

# A. donuts
# Given an int count of a number of donuts, return a string
# of the form 'Number of donuts: <count>', where <count> is the number
# passed in. However, if the count is 10 or more, then use the word 'many'
# instead of the actual count.
# Example:
#   donuts(5) returns 'Number of donuts: 5'
#   donuts(23) returns 'Number of donuts: many'


def donuts(count):
    # your code here
    print("#1 (Donuts) Enter a number: ")
    num = int(input())
    if num < 10:
        print('Number of donuts: ', num)
    elif num > 10:
        print('Number of donuts: many')
donuts(input)


# B. both_ends
# Given a string s, return a string made of the first 2
# and the last 2 characters of the original string.
# However, if the string length is less than 2, return
# an empty string instead.
# Example:
#   'spring' -> 'spng'


def both_ends(s):
    # your code here
    print("#2 (Both_Ends) Enter a word: ")
    str = input()

    # Remove middle characters
    # Use slice + concatenation
    if len(str) < 2:
        print(" ")
    elif len(str) > 2:
        print(str[:2] + str[-2:])
both_ends(str)




# C. fix_start
# Given a string s, return a string where all occurrences
# of its first character have been changed to '*', except
# do not change the first character itself.
# Example:
#   'babble' -> 'ba**le'
# Assume that the string is length 1 or more.
# Hint: s.replace(stra, strb) returns a version of string s
# where all instances of stra have been replaced by strb.


def fix_start(s):
    # your code here
    print("#3 (Fix_Start) Enter a word: ")
    str = input()
    
    first_character = str[:1]
    x = str.replace(first_character, '*').replace('*', first_character, 1)
    print(x)
fix_start(str)


# D. mix_up
# Given strings a and b, return a single string with a and
# b separated by a space '<a> <b>', except swap the first
# 2 characters of each string.
# Example:
#   'mix', 'pod' -> 'pox mid'
#   'dog', 'dinner' -> 'dig donner'
# Assume a and b are length 2 or more.


def mix_up(a, b):
    # your code here
    a = input("#4 (Mix_Up) Enter value 1: ")
    b = input("#4 (Mix_Up) Enter value 2: ")

    x = b[:2] + a[2:]
    y = a[:2] + b[2:]
 
    print(x, y)
    return a, b
    
mix_up(input, input)




# E. verbing
# Given a string, if its length is at least 3, add 'ing' to its
# end unless it already ends in 'ing', in which case add 'ly'
# instead.
# If the string length is less than 3, leave it unchanged.
# Return the resulting string.


def verbing(s):
    # your code here
    print("#5 (Verbing) Enter a string: ")
    str = input()

    if len(str) >= 3 and not str.endswith('ing'):
        print(str + 'ing')
    elif str.endswith('ing'):
        print(str + 'ly')
        return str
verbing(str)


# F. not_bad
# Given a string, find the first occurrence of the substrings
# 'not' and 'bad'. If the 'bad' follows the 'not', replace
# the whole 'not'...'bad' substring with 'good'.
# Return the resulting string.
# Example:
#   'This dinner is not that bad!' -> 'This dinner is good!'


def not_bad(s):

  print("#6 (Not_Bad) Enter a string: ")
  str = input()

  x = str.find("not")
  y = str.find("bad")
  str = str.replace(str[x:y+3], 'good')
  print(str)
  return str
not_bad(str)


# G. front_back
# Consider dividing a string into two halves.
# If the length is even, the front and back halves are the same
# length. If the length is odd, we'll say that the extra
# character goes in the front half.
#   e.g. 'abcde', the front half is 'abc', the back half 'de'.
# Given 2 strings, a and b, return a string of the form:
#   a-front + b-front + a-back + b-back


def front_back(a, b):
    # your code here
    print("#7 (Front_Back) Enter first word: ")
    str_a = input()
    print("Enter second word: ")
    str_b = input()
    
    a_front = str_a[0:len(str_a) // 2 if len(str_a)%2 == 0 else ((len(str_a) // 2)+1):]
    a_back = str_a[len(str_a) // 2 if len(str_a)%2 == 0 else ((len(str_a) // 2)+1):] 
    b_front = str_b[0:len(str_b) // 2]
    b_back = str_b[len(str_b) // 2 if len(str_b)%2 == 0 else ((len(str_b) // 2)+1):]
    print(a_front+b_front+a_back+b_back)
    return a_front + b_front + a_back + b_back
front_back(input, input)
