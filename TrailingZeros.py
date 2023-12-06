# returns number of trailing zeros of n factorial without using factorial
def zeros(n):
    zero = 0
    x = 5
    while int(n / x) != 0:
        zero += int(n / x)
        x *= 5
    return zero

# TEST
print(zeros(100000))
