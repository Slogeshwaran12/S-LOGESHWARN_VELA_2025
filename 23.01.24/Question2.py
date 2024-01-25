#WHATS YOUR NAME


def print_full_name(first, last):
    full_name = f'Hello {first} {last}! You just delved into python.'
    print(full_name)
    first_name = input().strip()
last_name = input().strip()

# Call the function with the provided names
print_full_name(first_name, last_name)
