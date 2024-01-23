#You are asked to ensure that the first and last names of people begin with a capital letter in their passports. For example, alison heck should be capitalised correctly as Alison Heck.


#Given a full name, your task is to capitalize the name appropriately.



    
More
 
1
#!/bin/python3
2
​
3
import math
4
import os
5
import random
6
import re
7
import sys
8
def capitalize_name(full_name):
9
    # Capitalize the first letter of each word
10
    capitalized_name = ' '.join(word.capitalize() for word in full_name.split())
11
    return capitalized_name
12
​
13
# Read input
14
full_name = input()
15
​
16
# Call the function with the provided name and print the result
17
result = capitalize_name(full_name)
18
print(result)
19
​