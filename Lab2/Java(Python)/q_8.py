def count_digits(n):
    n = abs(n)
    return len(str(n))
num = int(input("Enter an integer: "))
num_digits = count_digits(num)
print(f"The number of digits in {num} is {num_digits}.")
