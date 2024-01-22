#Given an integer N, write a program to count the number of digits in N.
#Sample Input 1

#876349
#Sample Output 1

#6

def count_digits(N):

    num_str = str(N)
    num_digits = len(num_str)
    return num_digits

N = int(input())

result = count_digits(N)
print(result)