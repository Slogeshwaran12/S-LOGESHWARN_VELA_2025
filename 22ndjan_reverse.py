#Given a number N reverse the number and print it.

#Example 1: Input: N = 123 Output: 321 Explanation: The reverse of 123 is 321

num =int(input())
temp=num
reverse=0
while num>0:
    remainder=num%10
    reverse=(reverse*10)+remainder
    num=num//10
print(reverse)