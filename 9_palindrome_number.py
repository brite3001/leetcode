import math

x = 123454


# With string
# if str(x) == str(x)[::-1]:
#     print("pal")

# breakdown number


def is_palindrome(x: int):
    if x < 0:
        # Negative numbers are not palindromes
        return False

    if x >= 0 and x <= 9:
        # Single digits are palindromes
        return True

    rev = 0
    i = int(math.log10(x))  # This gets us the number of digits in x
    our_number = x
    # Break the int into a list (without converting to a string)
    while our_number > 0:
        
        our_number, r = divmod(our_number, 10)

        # Building the reverse number by number, by multiplying individual numbers with their 10's position reversed
        rev += r * pow(10, i)
        i -= 1

    return x == rev


print(is_palindrome(x))

