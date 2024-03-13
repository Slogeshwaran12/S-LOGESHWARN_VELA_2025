#Count

def count_digits(N):

    num_str = str(N)
    num_digits = len(num_str)
    return num_digits

N = int(input())

result = count_digits(N)
print(result)
