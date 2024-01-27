#best Divisor

#!/bin/python3

import math
import os
import random
import re
import sys

def digit_sum(num):
    return sum(int(digit) for digit in str(num))

def best_divisor(n):
    best = 1
    max_digit_sum = 1
    
    for i in range(2, n + 1):
        if n % i == 0:
            sum_i = digit_sum(i)
            if sum_i > max_digit_sum or (sum_i == max_digit_sum and i < best):
                best = i
                max_digit_sum = sum_i
    
    return best

if __name__ == '__main__':
    n = int(input().strip())
    result = best_divisor(n)
    print(result)

